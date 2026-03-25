"""
process d2o before upload to bdd
"""
from collections import defaultdict
from typing import Self, Any

import numpy as np
import orjson
import pandas as pd
from sqlalchemy.dialects.postgresql import JSONB, NUMERIC
from tqdm import tqdm

from pydofus3.config import settings
from pydofus3.db_dump.config import db_settings
from pydofus3.db_dump.dump_to_bdd import BDD
from pydofus3.enum_data import TypeData, TypeDataOther


class Processor:
    """
    process d2o before upload to bdd
    """

    def __init__(self, language: str = 'fr'):
        """
        :param language:  i18n language
        """
        self.language: str = language
        self.dtype: dict[str, dict[str, Any]] = defaultdict(dict)
        self.data: dict[str, pd.DataFrame] = self.process()

    def process(self) -> dict[str, pd.DataFrame]:
        """
        load all d2o file present in a dir
        :return: dict with d2o name as key and Dataframe of d2o content as value
        """
        data = {
                data['m_Name'].removesuffix("DataRoot"): pd.DataFrame.from_dict(data['objectsById'], orient="index")
                for path_file in tqdm(list((settings.extract_dir / TypeData.Data).iterdir()), desc="load d2o")
                if not path_file.stem == "catalog" and (data := orjson.loads(path_file.read_bytes()))
                }
        data['i18n'] = pd.DataFrame.from_dict(
            orjson.loads((settings.extract_dir / TypeDataOther.I18n / 'i18n.json').read_bytes()).values())
        self.dtype['i18n'] = {'id': NUMERIC}
        return data

    def add_missing_primary_key(self) -> Self:
        """
        add index as id if no id in dataframe
        :return: return Processor object with data updated
        """
        for value in self.data.values():
            if not 'id' in value.columns:
                value.insert(0, 'id', value.index.astype("Int64"))
        return self

    def add_primary(self) -> Self:
        """
        add field id_m and generate primary key to dataFrame without field id (primary key)
        :return: return Processor object with data updated
        """
        for table in tqdm(self.data.values(), desc="add primary"):
            if "id" not in table.columns or not table["id"].is_unique:
                table.insert(loc=0, column="id_m", value=np.array(range(1, len(table) + 1)))
        return self

    def get_custom_table(self) -> Self:
        """
        for each dataFrame of data_process add column with list of dict in new dataFrame
        (key ref to the id (id_back) and list of dict convert to dataFrame).
        Loop twice to extract sub element of sub element.
        """

        data_to_add = {}
        for _ in range(2):
            for key, value in tqdm((data_to_add.copy() or self.data).items(), desc="custom table"):
                for index, series in value.items():
                    if series.dtype == "object" and isinstance(series.iloc[0], list):
                        if (no_empty := series[series.str.len() > 0]).size == 0:
                            continue
                        if isinstance(no_empty.iloc[0][0], dict):
                            new_name = f"custom_{key}_{index}"
                            table = (
                                    value[[index, "id"] if "id" in value.columns else [index]]
                                    .explode(index)
                                    .dropna()
                                    .reset_index(drop=True)
                            )
                            df = pd.DataFrame(table[index].to_list())
                            if "id" in table.columns:
                                df = df.join(table.add_suffix("_back", axis=1)["id_back"])
                                self.add_id_back(new_name, key)
                            data_to_add[new_name] = df
                        elif isinstance(no_empty.iloc[0][0], list):
                            find_elem = self.find_nested_elem(no_empty)
                            if isinstance(find_elem, dict):
                                new_name = f"customArray_{key}_{index}"
                                value["index"] = value[index].apply(lambda x: list(range(len(x))))
                                table = (
                                        value[[index, "id", "index"] if "id" in value.columns else [index]]
                                        .explode([index, "index"])
                                        .dropna()
                                        .reset_index(drop=True)
                                )
                                if 'id' in table.columns:
                                    table.rename(columns={"id": "id_back"}, inplace=True)
                                    self.add_id_back(new_name, key)
                                data_to_add[new_name] = table
        self.data.update(data_to_add)
        return self

    @staticmethod
    def add_id_back(relation_name:str, key:str)->None:
        if relation_name not in db_settings.relation:
            db_settings.relation[relation_name] = dict()
        db_settings.relation[relation_name]['id_back'] = key

    @staticmethod
    def find_nested_elem(value: pd.Series) -> Any:
        for outer in value:
            for inner in outer:
                if len(inner) > 0:
                    return inner[0]
        return None

    @staticmethod
    def col_split(table: pd.DataFrame, split_conf: list[str], key2: str):
        """
        split column with list to multiple columns
        :param table: a many to many dataFrame
        :param split_conf: list with the name of the new column (1st element in column keep base name)
        :param key2: name of column to split
        :return: dataframe with new column
        """
        if table[key2].dtype == "str":
            table[key2] = table[key2].str.strip().replace('', None).dropna().map(lambda x: list(map(int, x.split(','))))

        for counter, name in enumerate(split_conf, start=1):
            try:
                table[name] = table[key2].apply(lambda x: x[counter])
            except:
                print(1)
        table[key2] = table[key2].apply(lambda x: x[0])
        return table

    def create_many_many(self) -> Self:
        """
        create table many to make many-to-many relationship between two table.
        :return: return Processor object with data updated
        """
        for table_name, value in tqdm(db_settings.relation_many_many.items(), desc="many many"):
            if table_name in self.data:
                for field, many in value.items():
                    columns = [many.key_id_table1, field] + many.key_sup
                    table =  self.data[table_name][columns]
                    if many.split_on:
                        table[field] = table[field].str.strip().replace('',None).str.split(many.split_on)
                    table = (table
                            .rename(columns={many.key_id_table1: table_name + "Id"})
                            .explode(columns[1:])
                            .dropna()
                    )
                    table = self.col_split(table, many.split, field) if many.split else table.astype({field: "int64"})
                    self.data[f"many_{table_name}_{many.table}_{field}"] = table
            else:
                print(f"{table_name} not found in data")
        return self

    def m_flag_extract(self) -> Self:
        """
        extract mflag column and add all field to table
        """
        for key, value in tqdm(self.data.items(), desc="mflag"):
            if 'm_flags' in value.columns:
                value.reset_index(drop=True, inplace=True)
                self.data[key] = pd.concat([value, pd.DataFrame(value.pop('m_flags').tolist())], axis=1)
        return self

    def class_extract(self) -> Self:
        for key, value in tqdm(self.data.items(), desc="type_class"):
            if 'type_class' in value.columns:
                value['class'] = value.pop('type_class').apply(lambda x: x['class'])
        return self

    def i18n_extract(self) -> Self:
        i18n_key = {"fr", 'en', 'de', 'es', 'pt', 'id'}
        for key, value in tqdm(self.data.items(), desc="i18n"):
            for col in value.columns:
                data = value[col].iloc[0] if len(value) > 0 else None
                if isinstance(data, dict) and len(data) == 6 and set(data) == i18n_key:
                    if not key in db_settings.relation:
                        db_settings.relation[key] = {}
                    id_i18n_name = f"{col}_"
                    db_settings.relation[key][id_i18n_name] = 'i18n'
                    value[id_i18n_name] = value[col].apply(lambda x: x['id'])
                    value[col] = value[col].apply(lambda x: x[self.language])
        return self

    def convert_object_to_str(self) -> Self:
        """
        convert object pandas columns to str
        :return: return Processor object with data updated
        """
        for key, value in tqdm(self.data.items(), desc="obj to str"):
            for i, j in enumerate(value.dtypes):
                if j == "object":
                    index = value.columns[i]
                    type_column = str
                    for i_type in value[index]:
                        if i_type is not None:
                            type_column = type(i_type)
                            break

                    if type_column in [list, dict]:
                        self.dtype[key][index] = JSONB
        return self

    def db_dump(self):
        self.add_missing_primary_key().get_custom_table().create_many_many().m_flag_extract().class_extract().i18n_extract().add_primary().convert_object_to_str()
        BDD(self).dump()


if __name__ == '__main__':
    Processor().db_dump()

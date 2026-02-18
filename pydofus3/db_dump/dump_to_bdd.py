"""
dump to database
"""

from typing import TYPE_CHECKING

from sqlalchemy import create_engine, text
from tqdm import tqdm

from pydofus3.config import settings
from .config import db_settings

if TYPE_CHECKING:
    from .process import Processor


class BDD:
    """
    class to dump dofus data to database
    """

    def __init__(self, processor: 'Processor'):
        """
        initialize the dump and database connection
        """
        self.engine = create_engine(str(settings.db_uri))
        self.processor = processor
        self.config = db_settings

    def dump(self) -> None:
        """
        dump d2o data to database and add relation
        """
        self._dump_to_bdd()
        self._create_relation()
        self._create_relation_many()

    def _dump_to_bdd(self) -> None:
        """
        dump d2o data to database
        """
        with self.engine.begin() as conn:
            self._remove_all_foreign_key(conn)
        for table_name, value in tqdm(self.processor.data.items(), desc="dump to bdd"):
            with self.engine.begin() as conn:
                try:
                    value.to_sql(table_name, conn, if_exists="replace", dtype=self.processor.dtype.get(table_name, {}),
                                 index=False)
                    primary_key = "id_m" if 'id_m' in value.columns else 'id'
                    conn.execute(text(f'ALTER TABLE "{table_name}" ADD PRIMARY KEY ({primary_key})'))
                except Exception as e:
                    print([e, table_name])

    def _remove_all_foreign_key(self, conn) -> None:
        """
        Remove all foreign key for a given database
        """
        statement = text(f"""
                         SELECT 'ALTER TABLE ' || quote_ident(table_schema) || '.' || quote_ident(table_name) ||
                                ' DROP CONSTRAINT ' || quote_ident(constraint_name) || ';'
                         FROM information_schema.table_constraints
                         WHERE constraint_type = 'FOREIGN KEY'
                         """)
        for i in [row[0] for row in conn.execute(statement)]:
            try:
                conn.execute(text(i))
            except Exception as e:
                print(e)

    def _create_relation(self) -> None:
        for table_name, foreign_keys in tqdm(self.config.relation.items(), desc="Adding relations"):
            for column_name, referenced_table in foreign_keys.items():
                constraint_name = f"fk_{table_name}_{column_name}"
                statement = self.foreign_key_sql(table_name, constraint_name, column_name, referenced_table)
                with self.engine.begin() as conn:
                    try:
                        conn.execute(text(statement))
                    except Exception as e:
                        print(f"\033[91m{table_name}.{column_name} -> {referenced_table}.id\033[0m Error: {e}")

    def _create_relation_many(self) -> None:
        for table1, value in tqdm(self.config.relation_many_many.items(), desc="bdd add many many"):
            for many_col, many in value.items():
                table = f"many_{table1}_{many.table2}_{many_col}"
                constraint_name_1 = f"fk_{table1}_{table}"
                constraint_name_2 = f"fk_{table}_{many.table2}"
                statement = f"{self.foreign_key_sql(table, constraint_name_1, f"{table1}Id", table1, many.key_id_table1)};{self.foreign_key_sql(table, constraint_name_2, many_col, many.table2, many.key_id_table2)}"
                with self.engine.begin() as conn:
                    try:
                        conn.exec_driver_sql(statement)
                    except Exception as e:
                        print(f"\033[91mFailed to create relations many many for table {table}\033[0m Error: {e}")

    def foreign_key_sql(self, table: str, constraint: str, column: str, ref_table: str, ref_col: str = "id") -> str:
        return f'ALTER TABLE "{table}" ADD CONSTRAINT "{constraint}" FOREIGN KEY ("{column}") REFERENCES "{ref_table}"({ref_col}) NOT VALID'

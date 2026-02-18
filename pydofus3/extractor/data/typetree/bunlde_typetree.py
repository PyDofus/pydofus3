from UnityPy.files import ObjectReader
from UnityPy.files.SerializedFile import SerializedType
from UnityPy.helpers.TypeTreeNode import TypeTreeNode


def get_type_tree(type_tree: SerializedType, script: dict | None = None) -> dict:
    if script and 'm_AssemblyName' in script:
        return {
            'AssemblyName': script['m_AssemblyName'],
            'ClassName': script['m_ClassName'],
            'NameSpace': script['m_Namespace'],
            'nodes': get_node(type_tree.node),
        }
    else:
        return {
            'AssemblyName': type_tree.m_AssemblyName,
            'ClassName': type_tree.m_ClassName,
            'NameSpace': type_tree.m_NameSpace,
            'nodes': get_node(type_tree.node),
        }


def get_node(node: TypeTreeNode) -> dict:
    node_data = {'name': node.m_Name, 'type': node.m_Type}
    if node.m_Children:
        node_data['children'] = [get_node(c) for c in node.m_Children]
    return node_data


def get_type(obj: ObjectReader, script: dict) -> dict:
    """
    get typetree of an object as dict
    """
    return {
        'type': get_type_tree(obj.serialized_type, script),
        'ref_types': [get_type_tree(ref) for ref in obj.assets_file.ref_types],
    }

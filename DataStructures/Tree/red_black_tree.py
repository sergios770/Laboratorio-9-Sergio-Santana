from DataStructures.Tree import rbt_node as bst_node
from DataStructures.List import array_list as lt


RED = 0
BLACK = 1

def new_node(key, value, color=RED):
    """
    Crea un nuevo nodo para un árbol rojo-negro y lo retorna.
    color:0 - rojo  color:1 - negro
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subárbol que cuelga de este nodo
        color: El color inicial del nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    """
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "color": color,
        "type": "RBT",
    }
    return node

def default_compare(key, element_key):
    if key == element_key:
        return 0
    if key > element_key:
        return 1
    return -1

def new_map():
    map = {}
    map["root"] = None
    map["type"] = "RBT"
    map["size"] = 0
    return map



def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    my_bst["root"]["color"] = bst_node.BLACK  # La raíz siempre debe ser negra
    return my_bst

def insert_node(root, key, value):
    if root is None:
        return bst_node.new_node(key, value)  # Nodo nuevo será rojo por defecto

    comparacion = default_compare(key, root["key"])
    if comparacion == 0:
        root["value"] = value
    elif comparacion == 1:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["left"] = insert_node(root["left"], key, value)

    # Correcciones y ajustes para mantener el balance rojo-negro
    if bst_node.is_red(root["right"]) and not bst_node.is_red(root["left"]):
        root = rotate_left(root)
    if bst_node.is_red(root["left"]) and bst_node.is_red(root["left"]["left"]):
        root = rotate_right(root)
    if bst_node.is_red(root["left"]) and bst_node.is_red(root["right"]):
        flip_colors(root)

    root["size"] = 1 + size_root(root["left"]) + size_root(root["right"])
    return root



def size(my_bst):
    return size_root(my_bst["root"])

def size_root(root):
    if root is None:
        return 0
    return 1 + size_root(root["left"]) + size_root(root["right"])

def get(my_bst, key):
    return get_node(my_bst["root"], key)

def get_node(root, key):
    if root is None:
        return None
    comparacion = default_compare(key, root["key"])
    if comparacion == 0:
        return root["value"]
    elif comparacion == 1:
        return get_node(root["right"], key)
    return get_node(root["left"], key)

def contains(my_rbt, key):
    return get(my_rbt, key) is not None

def is_empty(my_rbt):
    return size(my_rbt) == 0

def key_set_node(root, list_keys):
    if root is None:
        return
    key_set_node(root["left"], list_keys)
    lt.add_last(list_keys, root["key"])
    key_set_node(root["right"], list_keys)

def key_set(my_bst):
    list_keys = lt.new_list()
    key_set_node(my_bst["root"], list_keys)
    return list_keys

def value_set_node(root, list_values):
    if root is None:
        return
    value_set_node(root["left"], list_values)
    lt.add_last(list_values, root["value"])
    value_set_node(root["right"], list_values)

def value_set(my_bst):
    list_values = lt.new_list()
    value_set_node(my_bst["root"], list_values)
    return list_values

def height_node(node):
    if node is None:
        return -1
    left_height = height_node(node["left"])
    right_height = height_node(node["right"])
    return 1 + max(left_height, right_height)

def height(my_bst):
    return height_node(my_bst["root"])

def max_key(my_bst):
    return max_key_node(my_bst["root"])

def max_key_node(root):
    if root is None or root["right"] is None:
        return root["key"] if root else None
    return max_key_node(root["right"])

def min_key(my_bst):
    return min_key_node(my_bst["root"])

def min_key_node(root):
    if root is None or root["left"] is None:
        return root["key"] if root else None
    return min_key_node(root["left"])

def delete_min(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_min_tree(my_bst["root"])
        my_bst["size"] -= 1
    return my_bst

def delete_min_tree(root):
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = size_root(root)
    return root

def delete_max(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_max_tree(my_bst["root"])
        my_bst["size"] -= 1
    return my_bst

def delete_max_tree(root):
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    root["size"] = size_root(root)
    return root

def keys(my_bst, key_lo, key_hi):
    list_keys = lt.new_list()
    keys_range(my_bst["root"], key_lo, key_hi, list_keys)
    return list_keys

def keys_range(root, key_lo, key_hi, list_key):
    if root is None:
        return
    key = root["key"]
    if key_lo < key:
        keys_range(root["left"], key_lo, key_hi, list_key)
    if key_lo <= key <= key_hi:
        lt.add_last(list_key, key)
    if key_hi > key:
        keys_range(root["right"], key_lo, key_hi, list_key)

def values(my_bst, key_lo, key_hi):
    list_values = lt.new_list()
    values_range(my_bst["root"], key_lo, key_hi, list_values)
    return list_values

def values_range(root, key_lo, key_hi, list_values):
    if root is None:
        return
    key = root["key"]
    if key_lo < key:
        values_range(root["left"], key_lo, key_hi, list_values)
    if key_lo <= key <= key_hi:
        lt.add_last(list_values, root["value"])
    if key_hi > key:
        values_range(root["right"], key_lo, key_hi, list_values)

def flip_node_color(node_rbt):
    node_rbt["color"] = BLACK if node_rbt["color"] == RED else RED
    return node_rbt

def flip_colors(node_rbt):
    if node_rbt and node_rbt["left"] and node_rbt["right"]:
        flip_node_color(node_rbt)
        flip_node_color(node_rbt["left"])
        flip_node_color(node_rbt["right"])
    return node_rbt

def rotate_left(rbt_node):
    raiz = rbt_node["right"]
    rbt_node["right"] = raiz["left"]
    raiz["left"] = rbt_node
    raiz["color"] = rbt_node["color"]
    rbt_node["color"] = RED
    return raiz

def rotate_right(rbt_node):
    raiz = rbt_node["left"]
    rbt_node["left"] = raiz["right"]
    raiz["right"] = rbt_node
    raiz["color"] = rbt_node["color"]
    rbt_node["color"] = RED
    return raiz
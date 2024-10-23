from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rbt_node
from DataStructures.Utils.utils import handle_not_implemented

def setup_tests():
    empty_tree = rbt.new_map()

    return empty_tree

def setup_one_node():
    one_node = rbt.new_map()
    node = rbt_node.new_node(1,1)
    
    one_node["root"] = node
    one_node["color"] = rbt_node.BLACK
    
    return one_node

def setup_three_nodes():
    three_nodes = rbt.new_map()
    node_1 = rbt_node.new_node(1, 10)
    node_3 = rbt_node.new_node(10, 100)
    node_2 = rbt_node.new_node(5, 50)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3
    
    node_1["color"] = rbt_node.BLACK
    node_2["color"] = rbt_node.BLACK
    node_3["color"] = rbt_node.BLACK

    three_nodes["root"] = node_2

    return three_nodes


def setup_seven_nodes():
    seven_nodes = rbt.new_map()
    node_1 = rbt_node.new_node(10, 100)
    node_2 = rbt_node.new_node(20, 200)
    node_3 = rbt_node.new_node(30, 300)
    node_4 = rbt_node.new_node(40, 400)
    node_5 = rbt_node.new_node(50, 500)
    node_6 = rbt_node.new_node(60, 600)
    node_7 = rbt_node.new_node(70, 700)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3

    node_6["left"] = node_5
    node_6["right"] = node_7
    node_6["size"] = 3

    node_4["left"] = node_2
    node_4["right"] = node_6
    node_4["size"] = 7
    
    node_1["color"] = rbt_node.BLACK
    node_2["color"] = rbt_node.BLACK
    node_3["color"] = rbt_node.BLACK
    node_4["color"] = rbt_node.BLACK
    node_5["color"] = rbt_node.BLACK
    node_6["color"] = rbt_node.BLACK
    node_7["color"] = rbt_node.BLACK


    seven_nodes["root"] = node_4

    return seven_nodes


@handle_not_implemented
def test_new_map():
    empty_rbt = rbt.new_map()

    print(empty_rbt)

    assert empty_rbt["root"] is None
    assert empty_rbt["type"] == "RBT"


@handle_not_implemented
def test_put():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Insertar en un árbol vacío
    rbt.put(empty_rbt, 1, 1)

    assert empty_rbt["root"] is not None
    assert empty_rbt["root"]["value"] == 1

    # Insertar a la izquierda en un árbol con 3 nodos

    rbt.put(three_rbt, 7, 7)

    assert three_rbt["root"]["right"]["left"]["key"] == 7
    assert three_rbt["root"]["right"]["left"]["value"] == 7
    assert three_rbt["root"]["right"]["left"]["size"] == 1
    assert three_rbt["root"]["right"]["size"] == 2
    assert three_rbt["root"]["size"] == 4
    assert three_rbt["root"]["left"]["size"] == 1

    # Insertar a la derecha en un árbol con 3 nodos

    rbt.put(three_rbt, 3, 3)

    assert three_rbt["root"]["left"]["key"] == 3
    assert three_rbt["root"]["left"]["value"] == 3
    assert three_rbt["root"]["left"]["left"]["key"] == 1
    assert three_rbt["root"]["left"]["left"]["value"] == 10
    assert three_rbt["root"]["left"]["left"]["size"] == 1
    assert three_rbt["root"]["left"]["size"] == 2
    assert three_rbt["root"]["size"] == 5
    assert three_rbt["root"]["right"]["size"] == 2

    # Insertar en un árbol con 3 nodos, pero la llave ya existe

    rbt.put(three_rbt, 10, 9)

    assert three_rbt["root"]["right"]["key"] == 10
    assert three_rbt["root"]["right"]["value"] == 9
    assert three_rbt["root"]["right"]["size"] == 2
    assert three_rbt["root"]["size"] == 5
    assert three_rbt["root"]["left"]["size"] == 2

    # Insertar en un árbol con 3 nodos, todo a la izquierda

    rbt.put(three_rbt, 0, 0)

    assert three_rbt["root"]["left"]["left"]["key"] == 0
    assert three_rbt["root"]["left"]["left"]["value"] == 0
    assert three_rbt["root"]["left"]["left"]["size"] == 1
    assert three_rbt["root"]["left"]["right"]["key"] == 3
    assert three_rbt["root"]["left"]["key"] == 1
    assert three_rbt["root"]["left"]["color"] == rbt_node.RED
    assert three_rbt["root"]["left"]["size"] == 3
    assert three_rbt["root"]["size"] == 6
    assert three_rbt["root"]["right"]["size"] == 2

    # Insertar en un árbol con 3 nodos, todo a la derecha

    rbt.put(three_rbt, 15, 15)

    assert three_rbt["root"]["right"]["right"]["key"] == 15
    assert three_rbt["root"]["right"]["right"]["value"] == 15
    assert three_rbt["root"]["right"]["right"]["size"] == 1
    assert three_rbt["root"]["right"]["size"] == 3
    assert three_rbt["root"]["size"] == 7
    assert three_rbt["root"]["left"]["size"] == 3
    
    rbt.put(three_rbt, 14, 16)
    rbt.put(three_rbt, 16, 16)
    
    assert three_rbt["root"]["right"]["right"]["key"] == 16
    assert three_rbt["root"]["right"]["right"]["value"] == 16
    assert three_rbt["root"]["right"]["right"]["size"] == 1
    assert three_rbt["root"]["right"]["key"] == 15
    assert three_rbt["root"]["right"]["left"]["key"] == 10
    assert three_rbt["root"]["right"]["left"]["right"]["key"] == 14
    assert three_rbt["root"]["right"]["size"] == 5
    assert three_rbt["root"]["size"] == 9
    assert three_rbt["root"]["left"]["size"] == 3    



@handle_not_implemented
def test_get():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Obtener un valor de un árbol vacío
    assert rbt.get(empty_rbt, 1) is None

    # Obtener un valor de un árbol con 3 nodos
    assert rbt.get(three_rbt, 1) == 10
    assert rbt.get(three_rbt, 5) == 50
    assert rbt.get(three_rbt, 10) == 100

    # Obtener un valor que no existe en un árbol con 3 nodos
    assert rbt.get(three_rbt, 0) is None
    assert rbt.get(three_rbt, 15) is None

@handle_not_implemented
def test_contains():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Verificar si un árbol vacío contiene un valor
    assert not rbt.contains(empty_rbt, 1)

    # Verificar si un árbol con 3 nodos contiene un valor
    assert rbt.contains(three_rbt, 1)
    assert rbt.contains(three_rbt, 5)
    assert rbt.contains(three_rbt, 10)

    # Verificar si un árbol con 3 nodos no contiene un valor
    assert not rbt.contains(three_rbt, 0)
    assert not rbt.contains(three_rbt, 15)


@handle_not_implemented
def test_size():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Verificar el tamaño de un árbol vacío
    assert rbt.size(empty_rbt) == 0

    # Verificar el tamaño de un árbol con 3 nodos
    assert rbt.size(three_rbt) == 3

    # Verificar el tamaño de un árbol con 7 nodos
    assert rbt.size(seven_rbt) == 7


@handle_not_implemented
def test_is_empty():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Verificar si un árbol vacío está vacío
    assert rbt.is_empty(empty_rbt)

    # Verificar si un árbol con 3 nodos está vacío
    assert not rbt.is_empty(three_rbt)


@handle_not_implemented
def test_key_set():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Verificar el conjunto de llaves de un árbol vacío
    key_set = rbt.key_set(empty_rbt)

    assert key_set["size"] == 0
    assert key_set["elements"] == []

    # Verificar el conjunto de llaves de un árbol con 3 nodos
    key_set = rbt.key_set(three_rbt)

    assert key_set["size"] == 3
    assert key_set["elements"][0] == 1
    assert key_set["elements"][1] == 5
    assert key_set["elements"][2] == 10


@handle_not_implemented
def test_value_set():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Verificar el conjunto de valores de un árbol vacío
    value_set = rbt.value_set(empty_rbt)

    assert value_set["size"] == 0
    assert value_set["elements"] == []

    # Verificar el conjunto de valores de un árbol con 3 nodos
    value_set = rbt.value_set(three_rbt)

    assert value_set["size"] == 3
    assert value_set["elements"][0] == 10
    assert value_set["elements"][1] == 50
    assert value_set["elements"][2] == 100


@handle_not_implemented
def test_min_key():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Verificar la llave mínima de un árbol vacío
    assert rbt.min_key(empty_rbt) is None

    # Verificar la llave mínima de un árbol con 3 nodos
    assert rbt.min_key(three_rbt) == 1

    # Verificar la llave mínima de un árbol con 7 nodos
    assert rbt.min_key(seven_rbt) == 10


@handle_not_implemented
def test_max_key():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Verificar la llave máxima de un árbol vacío
    assert rbt.max_key(empty_rbt) is None

    # Verificar la llave máxima de un árbol con 3 nodos
    assert rbt.max_key(three_rbt) == 10

    # Verificar la llave máxima de un árbol con 7 nodos
    assert rbt.max_key(seven_rbt) == 70

@handle_not_implemented
def test_floor():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Piso de un árbol vacío
    assert rbt.floor(empty_rbt, 1) is None

    # Piso de un árbol con 3 nodos
    assert rbt.floor(three_rbt, 0) is None
    assert rbt.floor(three_rbt, 2) == 1
    assert rbt.floor(three_rbt, 5) == 5
    assert rbt.floor(three_rbt, 10) == 10

    # Piso de un árbol con 7 nodos
    assert rbt.floor(seven_rbt, 5) is None
    assert rbt.floor(seven_rbt, 10) == 10
    assert rbt.floor(seven_rbt, 15) == 10
    assert rbt.floor(seven_rbt, 35) == 30
    assert rbt.floor(seven_rbt, 50) == 50
    assert rbt.floor(seven_rbt, 70) == 70
    assert rbt.floor(seven_rbt, 75) == 70


@handle_not_implemented
def test_ceiling():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Techo de un árbol vacío
    assert rbt.ceiling(empty_rbt, 1) is None

    # Techo de un árbol con 3 nodos
    assert rbt.ceiling(three_rbt, 0) == 1
    assert rbt.ceiling(three_rbt, 2) == 5
    assert rbt.ceiling(three_rbt, 5) == 5
    assert rbt.ceiling(three_rbt, 10) == 10

    # Techo de un árbol con 7 nodos
    assert rbt.ceiling(seven_rbt, 5) == 10
    assert rbt.ceiling(seven_rbt, 10) == 10
    assert rbt.ceiling(seven_rbt, 15) == 20
    assert rbt.ceiling(seven_rbt, 35) == 40
    assert rbt.ceiling(seven_rbt, 50) == 50
    assert rbt.ceiling(seven_rbt, 70) == 70
    assert rbt.ceiling(seven_rbt, 75) is None


@handle_not_implemented
def test_select():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Seleccionar de un árbol vacío
    assert rbt.select(empty_rbt, 1) is None

    # Seleccionar de un árbol con 3 nodos
    assert rbt.select(three_rbt, 1) == 5
    assert rbt.select(three_rbt, 2) == 10
    assert rbt.select(three_rbt, 3) == None

    # Seleccionar de un árbol con 7 nodos
    assert rbt.select(seven_rbt, 1) == 20
    assert rbt.select(seven_rbt, 2) == 30
    assert rbt.select(seven_rbt, 3) == 40
    assert rbt.select(seven_rbt, 4) == 50
    assert rbt.select(seven_rbt, 5) == 60
    assert rbt.select(seven_rbt, 6) == 70
    assert rbt.select(seven_rbt, 7) == None


@handle_not_implemented
def test_rank():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Rango de un árbol vacío
    assert rbt.rank(empty_rbt, 1) == 0

    # Rango de un árbol con 3 nodos
    assert rbt.rank(three_rbt, 1) == 0
    assert rbt.rank(three_rbt, 5) == 1
    assert rbt.rank(three_rbt, 10) == 2
    assert rbt.rank(three_rbt, 0) == 0
    assert rbt.rank(three_rbt, 15) == 3

    # Rango de un árbol con 7 nodos
    assert rbt.rank(seven_rbt, 10) == 0
    assert rbt.rank(seven_rbt, 20) == 1
    assert rbt.rank(seven_rbt, 30) == 2
    assert rbt.rank(seven_rbt, 40) == 3
    assert rbt.rank(seven_rbt, 50) == 4
    assert rbt.rank(seven_rbt, 60) == 5
    assert rbt.rank(seven_rbt, 70) == 6
    assert rbt.rank(seven_rbt, 0) == 0
    assert rbt.rank(seven_rbt, 75) == 7


@handle_not_implemented
def test_height():
    empty_rbt = setup_tests()
    one_rbt = setup_one_node()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Altura de un árbol vacío
    assert rbt.height(empty_rbt) == -1
    
    # Altura de un árbol de 1 nodo
    assert rbt.height(one_rbt) == 0

    # Altura de un árbol con 3 nodos
    assert rbt.height(three_rbt) == 1

    # Altura de un árbol con 7 nodos
    assert rbt.height(seven_rbt) == 2


@handle_not_implemented
def test_keys():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Llaves de un árbol vacío
    keys = rbt.keys(empty_rbt, 1, 10)

    assert keys["size"] == 0
    assert keys["elements"] == []

    # Llaves de un árbol con 3 nodos
    keys = rbt.keys(three_rbt, 1, 10)

    assert keys["size"] == 3
    assert keys["elements"][0] == 1
    assert keys["elements"][1] == 5
    assert keys["elements"][2] == 10

    # Llaves de un árbol con 7 nodos
    keys = rbt.keys(seven_rbt, 1, 100)

    assert keys["size"] == 7
    assert keys["elements"][0] == 10
    assert keys["elements"][1] == 20
    assert keys["elements"][2] == 30
    assert keys["elements"][3] == 40
    assert keys["elements"][4] == 50
    assert keys["elements"][5] == 60
    assert keys["elements"][6] == 70


@handle_not_implemented
def test_values():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()
    seven_rbt = setup_seven_nodes()

    # Valores de un árbol vacío
    values = rbt.values(empty_rbt, 1, 10)

    assert values["size"] == 0
    assert values["elements"] == []

    # Valores de un árbol con 3 nodos
    values = rbt.values(three_rbt, 1, 10)

    assert values["size"] == 3
    assert values["elements"][0] == 10
    assert values["elements"][1] == 50
    assert values["elements"][2] == 100

    # Valores de un árbol con 7 nodos
    values = rbt.values(seven_rbt, 1, 100)

    assert values["size"] == 7
    assert values["elements"][0] == 100
    assert values["elements"][1] == 200
    assert values["elements"][2] == 300
    assert values["elements"][3] == 400
    assert values["elements"][4] == 500
    assert values["elements"][5] == 600
    assert values["elements"][6] == 700

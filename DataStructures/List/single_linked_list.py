def new_single_node(element):
    """ Estructura que contiene la información a guardar en una lista encadenada

        :param element: Elemento a guardar en el nodo
        :type element: any

        :returns: Nodo creado
        :rtype: dict
    """
    node = {'info': element, 'next': None}
    return (node)


def new_list():
    """Crea una nueva linked list vacia

    Returns:
        linked_list: lista creada
    """
    newlist = {
        "first": None,
        "last": None,
        "size": 0     
    }
    
    return newlist


def size(my_list):
    return my_list["size"]


def add_first(my_list, element):
    """Añade un nodo al inicio de la lista

    Args:
        my_list (linked_list): Linked list creada anteriormente
        element (_type_): Elemento que se va a añadir al linked list como cabeza

    Returns:
        linked_list: lista con el nuevo nodo agregado al principio
    """
    node = new_single_node(element)
    node["next"] = my_list["first"]
    my_list["first"] = node
    
    if (my_list["size"]) == 0:
        my_list["last"] = my_list["first"]
    
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    """Añade un nodo al final del linked list

    Args:
        my_list (linked_list): Linked list creada anteriormente
        element (_type_): Elemento que se va a añadir al linked list como ultimo nodo

    Returns:
        linked_list: lista con el nuevo nodo agregado al final
    """
    node = new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
    
    my_list["size"] += 1
    
    return my_list

def is_empty(my_list):
    """Revisa si la lista enlazada esta vacia
    Args:
        my_list (linked_list): Lista enlazada a revisar
    """
    return my_list["size"] == 0

def first_element(my_list):
    """Retorna la informacion del primer nodo en la lista enlazada
    Args:
        my_list (linked_list): Lista enlazada
    Returns:
        _type_: Info del primer nodo. Retorna none si no hay nodos en la lista enlazada
    """
    if my_list["first"] is not None:
        return my_list["first"]["info"]
    else: 
        return None 
        

def last_element(my_list):
    """Retorna la informacion del ultimo nodo en la lista enlazada
    Args:
        my_list (linked_list): Lista enlazada
    Returns:
        _type_: Info del ultimo nodo. Retorna none si no hay nodos en la lista enlazada
    """
    if my_list["last"] is not None: 
        return my_list ["last"]["info"]
    else: 
        return None 
    
def get_element(my_list, pos):
    """Busca la info del nodo en una posicion especifica

    Args:
        my_list (linked_list): Lista enlazada donde se va a buscar el nodo
        pos (int): Posicion de nodo cuya info se quiere saber

    Returns:
        _type_: Info de nodo en la posicion pos
    """
    current_node = my_list["first"]
    pos_search = 0
    
    while pos_search < pos:
        current_node = current_node["next"]
        pos_search += 1 
        
    return current_node["info"]

def delete_element(my_list, pos): 
    """Borra el nodo de la lista enlazada en la posicion ingresada

    Args:
        my_list (linked_list): Lista enlazada
        pos (int): Posicion del nodo que se quiere borrar

    Returns:
        linked_list: Lista enlazada con el nodo borrado
    """
    current_node = my_list["first"]
    prev_node = my_list["first"]
    pos_search = 0 
    
    if pos == 0: 
        my_list["first"] = my_list ["first"]["next"]
        my_list["size"] -= 1 
        
    else: 
        while pos_search < pos:
            prev_node = current_node
            current_node = current_node["next"]
            pos_search += 1 
            
        prev_node["next"] = current_node["next"]
        my_list["size"] -= 1
        
        if pos == my_list["size"]:
            my_list["last"] = prev_node
    
    return my_list


def remove_first(my_list):
    """Remueve el primer nodo en la lista enlazada y retorna la info que este tenia
    Args:
        my_list (linked_list): Lista enlazada 
    Returns:
        _type_: Info de nodo borrado
    """
    if size(my_list) == 0:
        return None
    
    info = first_element(my_list)
    my_list = delete_element(my_list, 0)
    
    return info
    
def remove_last(my_list):
    """Remueve el ultimo nodo en la lista enlazada y retorna la info que este tenia
    Args:
        my_list (linked_list): Lista enlazada 
    Returns:
        _type_: Info de nodo borrado
    """
    if size(my_list) == 0:
        return None
    
    info = last_element(my_list)
    my_list = delete_element(my_list, my_list["size"]-1)
    
    return info

def insert_element(my_list, element, pos):
    """Inserta un nuevo nodo con un elemento especifico en la posicion pos

    Args:
        my_list (linked_list): Lista enlazada donde se va a insertar el nodo
        element (_type_): Elemento que va a tener el nuevo nodo insertado
        pos (_type_): Posicion donde se insertara el nuevo nodo

    Returns:
        linked_list: Lista enlazada con el nuevo nodo
    """
    
    if pos > size(my_list):
        return None
    if pos == size(my_list):
        return add_last(my_list, element)
    if pos == 0:
        return add_first(my_list, element)
    
    new_node = new_single_node(element)
    current_node = my_list["first"]
    prev_node = my_list["first"]
    pos_search = 0
    
    while pos_search < pos:
        prev_node = current_node
        current_node = current_node["next"]
        pos_search += 1 
    
    prev_node["next"] = new_node
    new_node["next"] = current_node
    my_list["size"] += 1
    
    return my_list
    
def is_present(my_list, element, cmp_function):
    """Informa si un elemento está en la lista. Si esta presente, retorna la posición en la que se encuentra
    o menos uno (-1) si no esta presente. Se utiliza la función de comparación pasada por parámetro para comparar 
    los elementos, la cual debe retornan cero si los elementos son iguales.

    Args:
        my_list (linked_list): Lista enlazada que se revisará
        element (_type_): Elemento que se buscará
        cmp_function (function): Función de comparación

    Returns:
        int: posición de elemento en la lista 
    """
    position = -1
    size = my_list["size"]
    
    if size > 0:
        current_node = my_list["first"]
        pos_search = 1
        
        while pos_search  <= size and position == -1:
            if current_node is not None:
                if cmp_function(element, current_node["info"]) == 0:
                    position = pos_search-1
                else:
                    current_node = current_node["next"]
                    pos_search += 1
    
    return position
    
    
def change_info(my_list, pos, new_info):
    """Cambia la info del nodo en posición pos por nueva información

    Args:
        my_list (linked_list): Lista enlazada con el nodo a cambiar info
        pos (int): Posición del nodo cuya info se cambiará
        new_info (_type_): Información que se le asignará al nodo especificado

    Returns:
        linked_list: Lista enlazada con el nodo editado
    """
    if pos > size(my_list):
        return my_list
    
    current_node = my_list["first"]
    pos_search = 0
    
    while pos_search < pos:
        current_node = current_node["next"]
        pos_search += 1
    
    current_node["info"] = new_info
    
    return my_list
    


def exchange(my_list, pos1, pos2):
    """Cambia la informacion entre el nodo en pos1 y el nodo en pos2

    Args:
        my_list (linked_list): Lista enlazada con el nodo a cambiar info
        pos1 (int): Posición del nodo 1 cuya informacion se intercambiará
        pos2 (int): Posición del nodo 2 cuya info se intercambiará

    Returns:
        linked_list: Lista enlazada con los nodos intercambiados
    """
    if pos1 == pos2:
        return my_list
    
    nodo_1 = my_list['first']
    pos_search = 0
    
    while pos_search < pos1:
        nodo_1 = nodo_1['next']
        pos_search += 1
        
    nodo_2 = my_list['first']
    pos_search = 0
   
    while pos_search < pos2:
        nodo_2 = nodo_2['next']
        pos_search += 1
    
    temp = nodo_1['info']
    nodo_1['info'] = nodo_2['info']
    nodo_2['info'] = temp

    return my_list
 
def sub_list(my_list, pos, num_elem): 
    """ Retorna una sub-lista de la lista recibida.

    Retorna una lista que contiene los elementos a partir de la posición pos, con una longitud de num_elem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.
    Args: 
        my_list (linked_list): Lista enlazada con el nodo a cambiar info
        pos (int): Posición del nodo desde el que se va a hacer la sublista 
        num_elem (int): Numero de nodos de los que se quiere crear la sublista
    Returns:
    linked_list: lista enlazada con los elementos dados

    """
    primer_nodo= my_list["first"]
    pos_search = 0
    
    while pos_search < pos:
       primer_nodo= primer_nodo["next"]
       pos_search += 1
        
    nueva_lista = new_list()

    for i in range(num_elem):
        add_last(nueva_lista, primer_nodo["info"])
        primer_nodo = primer_nodo["next"]
    
    return nueva_lista

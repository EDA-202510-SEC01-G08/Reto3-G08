from DataStructures.Tree import rbt_node as rb
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al

def new_map():
    return {"root": None}

def rotate_left(node_rbt):
    new_right =  node_rbt["right"]["left"]
    new_root = node_rbt["right"]
    node_rbt["right"] = new_right
    new_root["left"] = node_rbt
    return new_root

def rotate_right(node_rbt):
    new_root = node_rbt["left"]
    new_left = new_root["right"]
    node_rbt["left"] = new_left
    new_root["right"] = node_rbt

def flip_node_color(node_rbt):
    if rb.is_red(node_rbt):
        node_rbt["color"] = "BLACK"
    else:
        node_rbt["color"] = "RED"
    return node_rbt

def flip_colors(node_rbt):
    node_rbt["color"] = "RED"
    node_rbt["left"]["color"] = "BLACK"
    node_rbt["right"]["color"] = "BLACK"
    return node_rbt

def put(my_rbt, key, value):

    if my_rbt["root"] is None:
        my_rbt["root"] = {"key": key, "value": value, "color": "RED", "left": None, "right": None}
        my_rbt["root"]["color"] = "BLACK"
    else:
        insert_node(my_rbt["root"], key, value)
    return my_rbt

def insert_node(root, key, value):
    
    if key < root["key"]:
        if root["left"] is None:
            root["left"] = {"key": key, "value": value, "color": "RED", "left": None, "right": None}
        else:
            insert_node(root["left"], key, value)
    
    elif key > root["key"]:
        if root["right"] is None:
            root["right"] = {"key": key, "value": value, "color": "RED", "left": None, "right": None}
        else:
            insert_node(root["right"], key, value)
    else:
        root["value"] = value 

def get(my_rbt, key):
    if my_rbt["root"] is None:
        return None
    else:
        return get_node(my_rbt["root"], key)
    
def get_node(root, key):
    if root is None:
        return None
    if key < root["key"]:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"], key)
    else:
        return root["value"]

def contains(my_rbt, key):
    if get(my_rbt, key) is not None:
        return True
    else:
        return False
    
def size(my_rbt):
    if is_empty(my_rbt):
        return 0
    else:
        return size_tree(my_rbt["root"])

def size_tree(root):
    if root is None:
        return 0
    else:
        return 1 + size_tree(root["left"]) + size_tree(root["right"])

def is_empty(my_rbt):
    if my_rbt["root"] is None:
        return True
    else:
        return False
    
def key_set(my_rbt):
    if is_empty(my_rbt):
        return sl.new_list()
    else:
        list = sl.new_list()
        return key_set_tree(my_rbt["root"], list)

def key_set_tree(root, list):
    if root is None:
        return sl.new_list()
    key_set_tree(root["left"], list)
    sl.add_last(list, root["key"])
    key_set_tree(root["right"], list)
    return list

def value_set(my_rbt):
    if is_empty(my_rbt):
        return sl.new_list()
    else:
        list = sl.new_list()
        return value_set_tree(my_rbt["root"], list)

def value_set_tree(root, list):
    if root is None:
        return sl.new_list()
    value_set_tree(root["left"], list)
    sl.add_last(list, root["value"])
    value_set_tree(root["right"], list)
    return list

def get_min(my_rbt):
    if is_empty(my_rbt):
        return None
    else:
        return get_min_node(my_rbt["root"])

def get_min_node(root):
    if root is None:
        return None
    while root["left"] is not None:
        root = root["left"]
    return root["key"]

def get_max(my_rbt):
    if is_empty(my_rbt):
        return None
    else:
        return get_max_node(my_rbt["root"])

def get_max_node(root):
    if root is None:
        return None
    while root["right"] is not None:
        root = root["right"]
    return root["key"]
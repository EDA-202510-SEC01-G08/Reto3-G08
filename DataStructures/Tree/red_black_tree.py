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
        rb.change_color(node_rbt, "BLACK")
    else:
        rb.change_color(node_rbt, "RED")
    return node_rbt

def flip_colors(node_rbt):
    rb.change_color(node_rbt["left"], "BLACK")
    rb.change_color(node_rbt["right"], "BLACK")
    rb.change_color(node_rbt, "RED")
    return node_rbt

def put(my_rbt, key, value):

    if my_rbt["root"] is None:
        my_rbt["root"] = {"key": key, "value": value, "color": "RED", "left": None, "right": None}
        rb.change_color(my_rbt["root"], "BLACK")
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
    if key < rb.get_key(root):
        return get_node(root["left"], key)
    elif key > rb.get_key(root):
        return get_node(root["right"], key)
    else:
        return rb.get_value(root)

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
    sl.add_last(list, rb.get_key(root))
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
    sl.add_last(list, rb.get_value(root))
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
    return rb.get_key(root)

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
    return rb.get_key(root)

def delete_min(my_rbt): 
    if is_empty(my_rbt):
        return None
    else:   
        my_rbt["root"] = delete_min_node(my_rbt["root"])
        if my_rbt["root"] is not None:
            rb.change_color(my_rbt["root"], "BLACK")
    return my_rbt

def delete_min_node(root):
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_node(root["left"])
    return root

def delete_max(my_rbt):
    if is_empty(my_rbt):
        return None
    else:   
        my_rbt["root"] = delete_max_node(my_rbt["root"])
        if my_rbt["root"] is not None:
            rb.change_color(my_rbt["root"], "BLACK")
    return my_rbt

def delete_max_node(root):
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_node(root["right"])
    return root

def floor(my_rbt, key):
    if is_empty(my_rbt):
        return None
    else:
        return floor_key(my_rbt["root"], key)

def floor_key(root, key):
    if root is None:
        return None
    if key == rb.get_key(root):
        return rb.get_key(root)
    if key < rb.get_key(root):
        return floor_key(root["left"], key)
    if floor_key(root["right"], key) is not None:
        return floor_key(root["right"], key)
    else:
        return rb.get_key(root)
    
def ceiling(my_rbt, key):
    if is_empty(my_rbt):
        return None
    else:
        return ceiling_key(my_rbt["root"], key)

def ceiling_key(root, key):
    if root is None:
        return None
    if key == rb.get_key(root):
        return rb.get_key(root)
    if key > rb.get_key(root):
        return ceiling_key(root["right"], key)
    if ceiling_key(root["left"], key) is not None:
        return ceiling_key(root["left"], key)
    else:
        return rb.get_key(root)
    
def select(my_rbt, pos):
    if is_empty(my_rbt):
        return None
    else:
        return select_key(my_rbt["root"], pos)

def select_key(root, key):
    if root is None:
        return None
    if key == size_tree(root["left"]):
        return rb.get_key(root)
    if key < size_tree(root["left"]):
        return select_key(root["left"], key)
    else:
        return select_key(root["right"], key - size_tree(root["left"]) - 1)

def rank(my_rbt, key):
    if is_empty(my_rbt):
        return None
    else:
        return rank_keys(my_rbt["root"], key)

def rank_keys(root, key):
    if root is None:
        return 0
    if key < rb.get_key(root):
        return rank_keys(root["left"], key)
    elif key > rb.get_key(root):
        return 1 + size_tree(root["left"]) + rank_keys(root["right"], key)
    else:
        return size_tree(root["left"])

def height(my_rbt):
    if is_empty(my_rbt):
        return 0
    else:
        return height_tree(my_rbt["root"])

def height_tree(root):
    if root is None:
        return 0
    else:
        left_height = height_tree(root["left"])
        right_height = height_tree(root["right"])
        return 1 + max(left_height, right_height)
    
def keys(my_rbt, key_initial, key_final):
    if is_empty(my_rbt):
        return None
    else:
        return keys_range(my_rbt["root"], key_initial, key_final)
    
def keys_range(root, key_initial, key_final):
    if root is None:
        return sl.new_list()
    if key_initial > rb.get_key(root):
        return keys_range(root["right"], key_initial, key_final)
    elif key_final < rb.get_key(root):
        return keys_range(root["left"], key_initial, key_final)
    else:
        list = sl.new_list()
        sl.add_last(list, rb.get_key(root))
        left_keys = keys_range(root["left"], key_initial, key_final)
        right_keys = keys_range(root["right"], key_initial, key_final)
        sl.add_all(list, left_keys)
        sl.add_all(list, right_keys)
        return list
    
def values(my_rbt, key_initial, key_final):
    if is_empty(my_rbt):
        return None
    else:
        return values_range(my_rbt["root"], key_initial, key_final)

def values_range(root, key_initial, key_final):
    if root is None:
        return sl.new_list()
    if key_initial > rb.get_key(root):
        return values_range(root["right"], key_initial, key_final)
    elif key_final < rb.get_key(root):
        return values_range(root["left"], key_initial, key_final)
    else:
        list = sl.new_list()
        sl.add_last(list, rb.get_value(root))
        left_values = values_range(root["left"], key_initial, key_final)
        right_values = values_range(root["right"], key_initial, key_final)
        sl.add_all(list, left_values)
        sl.add_all(list, right_values)
        return list
from DataStructures.List import array_list as ar
from DataStructures.List import single_linked_list as sl

def new_queue():
    new_queue = sl.new_list()
    return new_queue

def enqueue(my_queue, element):
    return sl.add_last(my_queue, element)

def dequeue(my_queue):
    return sl.remove_first(my_queue)

def is_empty(my_queue):
    return sl.is_empty(my_queue)
    
def peek(my_queue):
    return sl.first_element(my_queue)

def size(my_queue):
    return sl.size(my_queue)
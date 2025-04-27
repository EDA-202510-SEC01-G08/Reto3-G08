import time
import csv
import os
from datetime import datetime as dt
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as ar
from DataStructures.List import single_linked_list as sl
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc

csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('_file')) + '/Data/Crime_in_LA/Crime_in_LA'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = lp.new_map(5, 0.5, 109345121)
    
    fecha_occ = rbt.new_map()
    fecha_rptd = rbt.new_map()
    area_name = rbt.new_map()
    edad = rbt.new_map()
    genero = bst.new_map()

    lp.put(catalog, "fecha_occ", fecha_occ)
    lp.put(catalog, "fecha_rptd", fecha_rptd)
    lp.put(catalog, "area_name", area_name)
    lp.put(catalog, "edad", edad)
    lp.put(catalog, "genero", genero)

    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    rbt_fecha_occured = lp.get(catalog, "fecha_occ")
    rbt_fecha_rptd = lp.get(catalog, "fecha_rptd")
    rbt_area_name = lp.get(catalog, "area_name")
    rbt_edad = lp.get(catalog, "edad")
    bst_genero = lp.get(catalog, "genero")

    file = data_dir + filename
    imput_file = csv.DictReader(open(file, encoding='utf-8'))
    count = 0
    first_five = ar.new_list()
    last_five = ar.new_list()
    for crime in imput_file:
        map_un_dato = sc.new_map(15, 4, 109345121)
        sc.put(map_un_dato, "DR_NO", crime["DR_NO"])
        sc.put(map_un_dato, "Date Rptd", crime["Date Rptd"])
        sc.put(map_un_dato, "DATE OCC", crime["DATE OCC"])
        sc.put(map_un_dato, "TIME OCC", crime["TIME OCC"])
        sc.put(map_un_dato, "AREA", crime["AREA"])
        sc.put(map_un_dato, "AREA NAME", crime["AREA NAME"])
        sc.put(map_un_dato, "Rptd Dist No", crime["Rptd Dist No"])
        sc.put(map_un_dato, "Part 1-2", crime["Part 1-2"])
        sc.put(map_un_dato, "Crm Cd", crime["Crm Cd"])
        sc.put(map_un_dato, "Crm Cd Desc", crime["Crm Cd Desc"])
        sc.put(map_un_dato, "Vict Age", crime["Vict Age"])
        sc.put(map_un_dato, "Vict Sex", crime["Vict Sex"])
        sc.put(map_un_dato, "Status", crime["Status"])
        sc.put(map_un_dato, "Status Desc", crime["Status Desc"])
        sc.put(map_un_dato, "LOCATION", crime["LOCATION"])

        if rbt.contains(rbt_fecha_occured, crime["DATE OCC"]) == False:
            rbt.put(rbt_fecha_occured, crime["DATE OCC"], ar.new_list())
        if rbt.contains(rbt_fecha_rptd, crime["Date Rptd"]) == False:
            rbt.put(rbt_fecha_rptd, crime["Date Rptd"], ar.new_list())
        if rbt.contains(rbt_area_name, crime["AREA NAME"]) == False:
            rbt.put(rbt_area_name, crime["AREA NAME"], ar.new_list())
        if rbt.contains(rbt_edad, crime["Vict Age"]) == False:
            rbt.put(rbt_edad, crime["Vict Age"], ar.new_list())
        if bst.contains(bst_genero, crime["Vict Sex"]) == False:
            bst.put(bst_genero, crime["Vict Sex"], ar.new_list())

        ar.add_last(rbt.get(rbt_fecha_occured, crime["DATE OCC"]), map_un_dato)
        ar.add_last(rbt.get(rbt_fecha_rptd, crime["Date Rptd"]), map_un_dato)
        ar.add_last(rbt.get(rbt_area_name, crime["AREA NAME"]), map_un_dato)
        ar.add_last(rbt.get(rbt_edad, crime["Vict Age"]), map_un_dato)
        ar.add_last(rbt.get(bst_genero, crime["Vict Sex"]), map_un_dato)

        datos_listas = [crime["DR_NO"],
                        crime["Date Rptd"],
                        crime["DATE OCC"],
                        crime["AREA NAME"],
                        crime["Crm Cd"]]

        if count < 5:
            ar.add_last(first_five, datos_listas)
        elif count >= 5:
            ar.add_last(last_five, datos_listas)
            if ar.size(last_five) > 5:
                ar.remove_first(last_five)

        count += 1

    return count, first_five, last_five

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

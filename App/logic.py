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
from datetime import datetime as dt

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
    start_time = get_time()
    with open(filename, encoding='utf-8') as file:

        rbt_fecha_occured = lp.get(catalog, "fecha_occ")
        rbt_fecha_rptd = lp.get(catalog, "fecha_rptd")
        rbt_area_name = lp.get(catalog, "area_name")
        rbt_edad = lp.get(catalog, "edad")
        bst_genero = lp.get(catalog, "genero")

        input_file = csv.DictReader(file)
        count = 0
        first_five = ar.new_list()
        last_five = ar.new_list()

        for row in input_file:
            map_una_fila = sc.new_map(15, 4, 109345121)
            sc.put(map_una_fila, "DR_NO", row["DR_NO"])
            sc.put(map_una_fila, "Date Rptd", dt.strptime(row["Date Rptd"], "%m/%d/%Y %H:%M:%S %p"))
            sc.put(map_una_fila, "DATE OCC", dt.strptime(row["DATE OCC"], "%m/%d/%Y %H:%M:%S %p"))
            sc.put(map_una_fila, "TIME OCC", row["TIME OCC"])
            sc.put(map_una_fila, "AREA", row["AREA"])
            sc.put(map_una_fila, "AREA NAME", row["AREA NAME"])
            sc.put(map_una_fila, "Rptd Dist No", row["Rpt Dist No"])
            sc.put(map_una_fila, "Part 1-2", row["Part 1-2"])
            sc.put(map_una_fila, "Crm Cd", row["Crm Cd"])
            sc.put(map_una_fila, "Crm Cd Desc", row["Crm Cd Desc"])
            sc.put(map_una_fila, "Vict Age", row["Vict Age"])
            sc.put(map_una_fila, "Vict Sex", row["Vict Sex"])
            sc.put(map_una_fila, "Status", row["Status"])
            sc.put(map_una_fila, "Status Desc", row["Status Desc"])
            sc.put(map_una_fila, "LOCATION", row["LOCATION"])

            if rbt.contains(rbt_fecha_occured, dt.strptime(row["DATE OCC"], "%m/%d/%Y %H:%M:%S %p")) == False:
                rbt.put(rbt_fecha_occured, dt.strptime(row["DATE OCC"], "%m/%d/%Y %H:%M:%S %p"), ar.new_list())
            if rbt.contains(rbt_fecha_rptd, dt.strptime(row["Date Rptd"], "%m/%d/%Y %H:%M:%S %p")) == False:
                rbt.put(rbt_fecha_rptd, dt.strptime(row["Date Rptd"], "%m/%d/%Y %H:%M:%S %p"), ar.new_list())
            if rbt.contains(rbt_area_name, row["AREA NAME"]) == False:
                rbt.put(rbt_area_name, row["AREA NAME"], ar.new_list())
            if rbt.contains(rbt_edad, row["Vict Age"]) == False:
                rbt.put(rbt_edad, row["Vict Age"], ar.new_list())
            if bst.contains(bst_genero, row["Vict Sex"]) == False:
                bst.put(bst_genero, row["Vict Sex"], ar.new_list())

            ar.add_last(rbt.get(rbt_fecha_occured, dt.strptime(row["DATE OCC"], "%m/%d/%Y %H:%M:%S %p")), map_una_fila)
            ar.add_last(rbt.get(rbt_fecha_rptd, dt.strptime(row["Date Rptd"], "%m/%d/%Y %H:%M:%S %p")), map_una_fila)
            ar.add_last(rbt.get(rbt_area_name, row["AREA NAME"]), map_una_fila)
            ar.add_last(rbt.get(rbt_edad, row["Vict Age"]), map_una_fila)
            ar.add_last(rbt.get(bst_genero, row["Vict Sex"]), map_una_fila)

            datos_listas = [row["DR_NO"],
                            row["Date Rptd"],
                            row["DATE OCC"],
                            row["AREA NAME"],
                            row["Crm Cd"]] # se usa lista nativa para facilitar el uso de tabulate

            if count < 5:
                ar.add_last(first_five, datos_listas)
            elif count >= 5:
                ar.add_last(last_five, datos_listas)
                if ar.size(last_five) > 5:
                    ar.remove_first(last_five)

            count += 1
        end_time = get_time()
        elapsed_time = str(round(delta_time(start_time, end_time),2)) + " ms"
        primer_tabla = ar.new_list()
        ar.add_last(primer_tabla, elapsed_time)
        ar.add_last(primer_tabla, count)
        return primer_tabla, first_five, last_five

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

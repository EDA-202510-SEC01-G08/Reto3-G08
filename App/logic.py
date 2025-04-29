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
            sc.put(map_una_fila, "AREA", int(row["AREA"]))
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


def req_1(catalog, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()

    fecha_1 = dt.strptime(fecha_i, "%m/%d/%Y")
    fecha_2 = dt.strptime(fecha_f, "%m/%d/%Y")

    fechas = lp.get(catalog, "fecha_occ")
    lista_valores = rbt.values(fechas, fecha_1, fecha_2)
    lista = ar.new_list()
    for list in lista_valores["elements"]:
        for hash in list["elements"]:
            ar.add_last(lista, hash)
            
    if lista["size"] == 0:
        return None
    else:
        lista_no_ordenada = ar.new_list()
        for index in range(lista["size"]):
            dato = ar.get_element(lista, index)
            hash_un_dato = sc.new_map(3, 4, 109345121)
            sc.put(hash_un_dato, "fecha", sc.get(dato, "DATE OCC"))
            sc.put(hash_un_dato, "area", sc.get(dato, "AREA"))
            sc.put(hash_un_dato, "index", index)
            ar.add_last(lista_no_ordenada, hash_un_dato)
        
        lista_sorted = ar.merge_sort(lista_no_ordenada, sort_crit_1)
        lista_index = ar.new_list()
        for i in lista_sorted["elements"]:
            ar.add_last(lista_index, sc.get(i, "index"))
        
        
        lista_final = ar.new_list()
        for index in lista_index["elements"]:
            lista_un_dato = [sc.get(ar.get_element(lista, index), "DR_NO"),
                             sc.get(ar.get_element(lista, index), "DATE OCC"),
                             sc.get(ar.get_element(lista, index), "TIME OCC"),
                             sc.get(ar.get_element(lista, index), "AREA NAME"),
                             sc.get(ar.get_element(lista, index), "Crm Cd"),
                             sc.get(ar.get_element(lista, index), "LOCATION")]
            ar.add_last(lista_final, lista_un_dato)
            
    end_time = get_time()
    time = str(round(delta_time(start_time, end_time), 2)) + "ms" 

    return lista_final, time
    
def sort_crit_1(record_1, record_2):
    fecha_a = sc.get(record_1, "fecha")
    fecha_b = sc.get(record_2, "fecha")

    if fecha_a > fecha_b:
        return True
    elif fecha_a < fecha_b:
        return False
    elif fecha_a == fecha_b:
        area_1 = sc.get(record_1, "area")
        area_2 = sc.get(record_2, "area")
        if area_1 > area_2:
            return True
        else:
            return False


def req_2(catalog, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()

    fecha_1 = dt.strptime(fecha_i, "%m/%d/%Y")
    fecha_2 = dt.strptime(fecha_f, "%m/%d/%Y")

    fechas = lp.get(catalog, "fecha_rptd")

    lista_valores = rbt.values(fechas, fecha_1, fecha_2)
    lista = ar.new_list()
    
    for list in lista_valores["elements"]:
        for hash in list["elements"]:
            status = sc.get(hash, "Status")
            gravedad = sc.get(hash, "Part 1-2")
            if status != "IC" and gravedad == "1":
                ar.add_last(lista, hash)
    if lista["size"] == 0:
        return None
    else:
        lista_no_ordenada = ar.new_list()
        for index in range(lista["size"]):
            dato = ar.get_element(lista, index)
            hash_un_dato = sc.new_map(3, 4, 109345121)
            sc.put(hash_un_dato, "fecha_rptd", sc.get(dato, "Date Rptd"))
            sc.put(hash_un_dato, "area_name", sc.get(dato, "AREA NAME"))
            sc.put(hash_un_dato, "index", index)
            ar.add_last(lista_no_ordenada, hash_un_dato)
    
        lista_sorted = ar.merge_sort(lista_no_ordenada, sort_crit_2)
        lista_index = ar.new_list()
        for i in lista_sorted["elements"]:
            ar.add_last(lista_index, sc.get(i, "index"))
        
        lista_final = ar.new_list()
        for index in lista_index["elements"]:
            lista_un_dato = [sc.get(ar.get_element(lista, index), "DR_NO"),
                             sc.get(ar.get_element(lista, index), "DATE OCC"),
                             sc.get(ar.get_element(lista, index), "TIME OCC"),
                             sc.get(ar.get_element(lista, index), "AREA"),
                             sc.get(ar.get_element(lista, index), "Rptd Dist No"),
                             sc.get(ar.get_element(lista, index), "Part 1-2"),
                             sc.get(ar.get_element(lista, index), "Crm Cd"),
                             sc.get(ar.get_element(lista, index), "Status"),
                             sc.get(ar.get_element(lista, index), "Date Rptd"),
                             sc.get(ar.get_element(lista, index), "AREA NAME"),]
            ar.add_last(lista_final, lista_un_dato)
        
        if ar.size(lista_final) > 10:
            lista_final_2 = ar.new_list()
            for k in range(-5,5):
                ar.add_last(lista_final_2, ar.get_element(lista_final, k))
            lista_final = lista_final_2

    end_time = get_time()
    time = str(round(delta_time(start_time, end_time),2)) + "ms" 
    return lista_final, time

def sort_crit_2(record_1, record_2):
    fecha_a = sc.get(record_1, "fecha_rptd")
    fecha_b = sc.get(record_2, "fecha_rptd")

    if fecha_a > fecha_b:
        return True
    elif fecha_a < fecha_b:
        return False
    elif fecha_a == fecha_b:
        area_1 = sc.get(record_1, "area_name")
        area_2 = sc.get(record_2, "area_name")
        if area_1 > area_2:
            return True
        else:
            return False

def req_3(catalog, N, area_name):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()

    rbt_area = lp.get(catalog, "area_name")
    crimes_in_area = rbt.get(rbt_area, area_name)
    total_crimes = ar.size(crimes_in_area)
    if total_crimes == 0:
        return None
    else:
        lista_datos = ar.new_list()
        for i in range(ar.size(crimes_in_area)):
            dato = ar.get_element(crimes_in_area, i)
            map_un_dato = sc.new_map(2,4,109345121)
            sc.put(map_un_dato, "fecha", sc.get(dato, "Date Rptd"))
            sc.put(map_un_dato, "index", i)
            ar.add_last(lista_datos, map_un_dato)
        lista_datos_sorted = ar.merge_sort(lista_datos, sort_crit_3)

        lista_indices = ar.new_list()
        for i in lista_datos_sorted["elements"]:
            ar.add_last(lista_indices, sc.get(i, "index"))
    
        lista_completa = ar.new_list()
        for index in lista_indices["elements"]:
            lista_un_dato = [sc.get(ar.get_element(crimes_in_area, index), "DR_NO"),
                             sc.get(ar.get_element(crimes_in_area, index), "DATE OCC"),
                             sc.get(ar.get_element(crimes_in_area, index), "TIME OCC"),
                             sc.get(ar.get_element(crimes_in_area, index), "AREA"),
                             sc.get(ar.get_element(crimes_in_area, index), "Rptd Dist No"),
                             sc.get(ar.get_element(crimes_in_area, index), "Part 1-2"),
                             sc.get(ar.get_element(crimes_in_area, index), "Crm Cd"),
                             sc.get(ar.get_element(crimes_in_area, index), "Status"),
                             sc.get(ar.get_element(crimes_in_area, index), "LOCATION")]
            ar.add_last(lista_completa, lista_un_dato)
        lista_final = ar.sub_list(lista_completa, 0, N)
    end_time = get_time()
    time = str(round(delta_time(start_time, end_time),2)) + "ms"
    return lista_final, time, total_crimes
    
def sort_crit_3(record_1, record_2):
    fecha_a = sc.get(record_1, "fecha")
    fecha_b = sc.get(record_2, "fecha")

    if fecha_a > fecha_b:
        return True
    else:
        return False

def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog, n, start_date, end_date):
    
    start_date = dt.strptime(start_date, "%Y-%m-%d")
    end_date = dt.strptime(end_date, "%Y-%m-%d")

    rbt_fecha_occ = lp.get(catalog, "fecha_occ")
    
    crimes_in_range = rbt.values(rbt_fecha_occ, start_date, end_date)
    # Array que contiene arrays de mapas, cada mapa es una fila de datos
    # Se crea una lista para almacenar los crímenes no resueltos

    crimes_ic = ar.new_list() 
    for array in crimes_in_range["elements"]:
        for mapa in array["elements"]:
            if sc.get(mapa, "Status") == "IC":
                ar.add_last(crimes_ic, mapa)

    #crimes_ic es un array que tiene mapas, cada mapa es una fila que está en el rango y que tiene como status IC

    area_crime_count = rbt.new_map()
    # Creo un arbol que tiene como llave el area y voy sumando la cantidad de crimenes que hay en cada area
    for mapa in crimes_ic["elements"]:
        area = int(sc.get(mapa, "AREA"))
        area_name = sc.get(mapa, "AREA NAME")
        if rbt.contains(area_crime_count, area) == False:
            rbt.put(area_crime_count, area, lp.new_map(5, 0.5, 109345121))
            lp.put(rbt.get(area_crime_count, area), "area_name", area_name)
            lp.put(rbt.get(area_crime_count, area), "crime_count", 0)
            lp.put(rbt.get(area_crime_count, area), "first_crime_date", None)
            lp.put(rbt.get(area_crime_count, area), "last_crime_date", None)
            lp.put(rbt.get(area_crime_count, area), "area", area)
        lp.put(rbt.get(area_crime_count, area), "crime_count", lp.get(rbt.get(area_crime_count, area), "crime_count") + 1)
        crime_date = sc.get(mapa, "DATE OCC")
        if lp.get(rbt.get(area_crime_count, area), "first_crime_date") is None or crime_date < lp.get(rbt.get(area_crime_count, area), "first_crime_date"):
            lp.put(rbt.get(area_crime_count, area), "first_crime_date", crime_date)
        if lp.get(rbt.get(area_crime_count, area), "last_crime_date") is None or crime_date > lp.get(rbt.get(area_crime_count, area), "last_crime_date"):
            lp.put(rbt.get(area_crime_count, area), "last_crime_date", crime_date)

    # Ahora la idea es sacar el values del arbol que me va a dar un stack con los mapas y 
    # ordenar el stack por la cantidad de crimenes que hay en cada area con merge_sort

    mapas_area = rbt.value_set(area_crime_count)
    # lista que contiene los mapas de cada area

    # Sort the areas using merge_sort and the custom sort criteria
    sorted_areas = ar.merge_sort(mapas_area, area_sort_criteria_5)

    # Get the top N areas
    top_n_areas_maps = ar.sub_list(sorted_areas, 0, n)

    return top_n_areas_maps


def area_sort_criteria_5(mapa_1, mapa_2):

    if lp.get(mapa_1, "crime_count") > lp.get(mapa_2, "crime_count"):
        return True
    elif lp.get(mapa_1, "crime_count") == lp.get(mapa_2, "crime_count"):
        if lp.get(mapa_1, "area_name") < lp.get(mapa_2, "area_name"):
            return True
        else:
            return False
    else:
        return False


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

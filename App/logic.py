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
            sc.put(map_una_fila, "AREA", row["AREA"])
            sc.put(map_una_fila, "AREA NAME", row["AREA NAME"])
            sc.put(map_una_fila, "Rptd Dist No", row["Rpt Dist No"])
            sc.put(map_una_fila, "Part 1-2", row["Part 1-2"])
            sc.put(map_una_fila, "Crm Cd", row["Crm Cd"])
            sc.put(map_una_fila, "Crm Cd Desc", row["Crm Cd Desc"])
            sc.put(map_una_fila, "Vict Age", int(row["Vict Age"]))
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
            if rbt.contains(rbt_edad, int(row["Vict Age"])) == False:
                rbt.put(rbt_edad, int(row["Vict Age"]), ar.new_list())
            if bst.contains(bst_genero, row["Vict Sex"]) == False:
                bst.put(bst_genero, row["Vict Sex"], ar.new_list())

            ar.add_last(rbt.get(rbt_fecha_occured, dt.strptime(row["DATE OCC"], "%m/%d/%Y %H:%M:%S %p")), map_una_fila)
            ar.add_last(rbt.get(rbt_fecha_rptd, dt.strptime(row["Date Rptd"], "%m/%d/%Y %H:%M:%S %p")), map_una_fila)
            ar.add_last(rbt.get(rbt_area_name, row["AREA NAME"]), map_una_fila)
            ar.add_last(rbt.get(rbt_edad,int(row["Vict Age"])), map_una_fila)
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


def req_4(catalog, N, edad_i, edad_f):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()

    edad_inicial = int(edad_i)
    edad_final = int(edad_f)

    edades = lp.get(catalog, "edad")

    lista_valores = rbt.values(edades, edad_inicial, edad_final)

    graves = ar.new_list()
    menores = ar.new_list()

    for list in lista_valores["elements"]:
        for hash in list["elements"]:
            gravedad = sc.get(hash, "Part 1-2")
            if gravedad == "Part 1":
                ar.add_last(graves, hash)
            elif gravedad == "Part 2":
                ar.add_last(menores, hash)

    if graves["size"] == 0 or menores["size"] == 0:
        return None
    
    graves_ordenados = ar.merge_sort(graves, sort_crit_4)
    menores_ordenados = ar.merge_sort(menores, sort_crit_4)

    crimenes_ordenados = graves_ordenados["elements"] + menores_ordenados["elements"]

    respuesta = ar.new_list()

    for crimen in crimenes_ordenados[:N]:
        info = {
            "ID Reporte": sc.get(crimen, "DR_NO"),
            "Fecha Ocurrencia": sc.get(crimen, "DATE OCC"),
            "Hora Ocurrencia": sc.get(crimen, "TIME OCC"),
            "Área": sc.get(crimen, "AREA"),
            "Subárea": sc.get(crimen, "AREA NAME"),
            "Gravedad": sc.get(crimen, "Part 1-2"),
            "Código Crimen": sc.get(crimen, "Crm Cd"),
            "Edad Víctima": sc.get(crimen, "Vict Age"),
            "Estado Caso": sc.get(crimen, "Status"),
            "Dirección": sc.get(crimen, "LOCATION")
        }
        ar.add_last(respuesta, info)

    end_time = get_time()
    tiempo_carga = delta_time(start_time, end_time)

    total_crimenes = ar.size(crimenes_ordenados)
    return tiempo_carga, total_crimenes, respuesta

def sort_crit_4(record_1, record_2):
    edad_1 = int(sc.get(record_1, "Vict Age"))
    edad_2 = int(sc.get(record_2, "Vict Age"))

    if edad_1 > edad_2:
        return True
    elif edad_1 < edad_2:
        return False
    else:
        fecha_a = sc.get(record_1, "DATE OCC")
        fecha_b = sc.get(record_2, "DATE OCC")
        
        # Convertir las fechas para comparar correctamente
        fecha_1 = dt.strptime(fecha_a, "%m/%d/%Y")
        fecha_2 = dt.strptime(fecha_b, "%m/%d/%Y")

        if fecha_1 < fecha_2:
            return True
        else:
            return False
  
def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    
    pass


def req_6(catalog,N,genero, mes):
    """
    Retorna el resultado del requerimiento 6
     start_time = get_time()
"""
    crímenes_por_area = ar.new_list()
    
    # Obtener lista de listas de crímenes por género
    crimenes_genero = bst.values(catalog, genero, genero)

    i = 0
    while i < ar.size(crimenes_genero):
        lista = ar.get(crimenes_genero, i)
        j = 0
        while j < ar.size(lista):
            crimen = ar.get(lista, j)

            fecha = sc.get(crimen, "DATE OCC")
            area = sc.get(crimen, "AREA NAME")

            # Validación mínima sin try
            if fecha is not None and fecha.count("/") == 2 and area is not None:
                partes = fecha.split("/")
                mes_crimen = int(partes[0])
                año_crimen = int(partes[2])

                if mes_crimen == mes:
                    # Revisar si ya existe el área
                    k = 0
                    encontrado = False
                    while k < ar.size(crímenes_por_area):
                        area_info = ar.get(crímenes_por_area, k)
                        if area_info["area"] == area:
                            area_info["crimenes"] += 1

                            # Verificar si el año ya está en su lista
                            ya_registrado = False
                            l = 0
                            while l < ar.size(area_info["años"]):
                                año_registrado = ar.get(area_info["años"], l)
                                if año_registrado == año_crimen:
                                    ya_registrado = True
                                l += 1
                            if not ya_registrado:
                                ar.add_last(area_info["años"], año_crimen)
                            encontrado = True
                        k += 1
                    
                    # Si no estaba el área, se agrega
                    if not encontrado:
                        nueva_area = {
                            "area": area,
                            "nombre_area": area,
                            "crimenes": 1,
                            "años": ar.new_list()
                        }
                        ar.add_last(nueva_area["años"], año_crimen)
                        ar.add_last(crímenes_por_area, nueva_area)

            j += 1
        i += 1

    # Ordenar
    areas_ordenadas = ar.merge_sort(crímenes_por_area, sort_crit_6)

    # Extraer solo los primeros N
    respuesta = ar.new_list()
    contador = 0
    while contador < N and contador < ar.size(areas_ordenadas):
        area_info = ar.get(areas_ordenadas, contador)

        # Crear años como tuplas (crímenes, año)
        años = ar.new_list()
        m = 0
        while m < ar.size(area_info["años"]):
            año = ar.get(area_info["años"], m)
            tupla = (area_info["crimenes"], año)
            ar.add_last(años, tupla)
            m += 1

        ar.add_last(respuesta, {
            "area": area_info["area"],
            "nombre_area": area_info["nombre_area"],
            "cantidad_crímenes": area_info["crimenes"],
            "años": años
        })
        contador += 1

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)

    return tiempo, respuesta


def sort_crit_6(r1, r2):
    c1 = r1["crimenes"]
    c2 = r2["crimenes"]

    if c1 < c2:
        return True
    elif c1 > c2:
        return False
    else:
        a1 = ar.size(r1["años"])
        a2 = ar.size(r2["años"])
        if a1 < a2:
            return True
        elif a1 > a2:
            return False
        else:
            return r1["nombre_area"] < r2["nombre_area"]


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

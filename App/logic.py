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
    time = delta_time(start_time, end_time)

    return ar.size(crimenes_ordenados), respuesta, time

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


def req_6(catalog, sexo, mes, N):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6

    # Crear una lista vacía para almacenar la información de crímenes por área
    crímenes_por_area = ar.new_list()
    
    # Obtener el árbol de crímenes filtrados por sexo
    crimenes_sexo = rbt.values(catalog, sexo)
    
    # Recorrer los crímenes filtrados por sexo
    for lista in crimenes_sexo["elements"]:
        for hash in lista["elements"]:
            area = sc.get(hash, "AREA NAME")
            fecha_crimen = sc.get(hash, "DATE OCC")
            
            # Obtener el mes y el año del crimen
            mes_crimen, dia_crimen, año_crimen = map(int, fecha_crimen.split("/"))
            
            # Verificar si el crimen ocurrió en el mes dado
            if mes_crimen == mes:
                # Buscar si el área ya está en la lista
                area_encontrada = False
                for i in range(ar.size(crímenes_por_area)):
                    area_info = ar.get(crímenes_por_area, i)
                    if area_info["area"] == area:
                        # Si el área ya existe, actualizamos la cantidad de crímenes y los años
                        area_info["crímenes"] += 1
                        if año_crimen not in area_info["años"]:
                            area_info["años"].append(año_crimen)
                        area_encontrada = True
                        
                # Si el área no fue encontrada, la agregamos a la lista
                if not area_encontrada:
                    area_info = {
                        "area": area,
                        "nombre_area": sc.get(hash, "AREA NAME"),
                        "crímenes": 1,
                        "años": [año_crimen]
                    }
                    ar.add_last(crímenes_por_area, area_info)

    # Ordenar las áreas utilizando la función de ordenación
    areas_ordenadas = ar.merge_sort(crímenes_por_area, sort_crit_6)
    
    # Limitar el número de áreas a N
    areas_ordenadas = areas_ordenadas[:N]
    
    # Generar la respuesta utilizando una lista de ar
    respuesta = ar.new_list()
    for area_info in areas_ordenadas:
        # Convertir la lista de años en una lista de tuplas (crímenes, año)
        años_info = [(area_info["crímenes"], año) for año in area_info["años"]]
        
        ar.add_last(respuesta, {
            "area": area_info["area"],
            "nombre_area": area_info["nombre_area"],
            "cantidad_crímenes": area_info["crímenes"],
            "años": años_info
        })
    
    return respuesta


def sort_crit_6(record_1, record_2):
    # Obtener la cantidad de crímenes de cada área
    crimenes_1 = record_1["crímenes"]
    crimenes_2 = record_2["crímenes"]
    
    # Primero, comparamos por la cantidad de crímenes (de menor a mayor)
    if crimenes_1 < crimenes_2:
        return True
    elif crimenes_1 > crimenes_2:
        return False
    else:
        # Si los crímenes son iguales, comparamos por la cantidad de años en los que ocurrieron crímenes
        años_1 = len(record_1["años"])  # El tamaño de la lista de años
        años_2 = len(record_2["años"])  # El tamaño de la lista de años
        
        if años_1 < años_2:
            return True
        elif años_1 > años_2:
            return False
        else:
            # Si los años son iguales, comparamos lexicográficamente por el nombre del área
            nombre_area_1 = record_1["nombre_area"]
            nombre_area_2 = record_2["nombre_area"]
            
            if nombre_area_1 < nombre_area_2:
                return True
            else:
                return False



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

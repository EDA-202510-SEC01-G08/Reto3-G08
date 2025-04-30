import sys
from App import logic as lg
from DataStructures.List import array_list as ar
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Tree import red_black_tree as rbt
import tabulate as tb
import csv  
from DataStructures.List import array_list as ar


def new_logic():
    return lg.new_logic()
    
def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):

    file = input("Ingrese el nombre del archivo a cargar: ")
    file_path = f"Data/Crime_in_LA/Crime_in_LA_{file}.csv" 

    data = lg.load_data(control, file_path)
    headers_generales = ["Tiempo de carga", "N° de registros"]
    print(tb.tabulate([data[0]["elements"]], headers_generales, tablefmt="pretty"))    
    print(f"\nLos primeros 5 registros son:\n")
    primeros = data[1]["elements"]
    headers = ["DR_NO", "Date Rptd", "DATE OCC", "AREA NAME", "Crm Cd"]  
    print(tb.tabulate(primeros, headers, tablefmt="pretty"))
    print(f"\nLos últimos 5 registros son:\n")
    primeros = data[2]["elements"] 
    print(tb.tabulate(primeros, headers, tablefmt="pretty"))


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1

    fecha_i = input("\nIngrese la fecha inical del rango en formato mm/dd/yyyy: ")
    fecha_f = input("\nIngrese la fecha final del rango en formato mm/dd/yyyy: ")
    result = lg.req_1(control, fecha_i, fecha_f)
    if result == None:
        print(f"\nNo se encontraron crimenes entre {fecha_i} - {fecha_f}")
    else:
        headers = ["Identificador del reporte", "Fecha", "Hora", "Nombre del Area", "Codigo del crimen", "Direccion"]
        print(result[1])
        print(f"\nLos crimenes encontrados entre {fecha_i} - {fecha_f} son:\n")
        data = result[0]["elements"]
        print(tb.tabulate(data, headers, tablefmt="pretty"))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    fecha_i = input("\nIngrese la fecha inical del rango en formato mm/dd/yyyy: ")
    fecha_f = input("\nIngrese la fecha final del rango en formato mm/dd/yyyy: ")
    result = lg.req_2(control, fecha_i, fecha_f)
    if result == None:
        print(f"\nNo se encontraron crimenes resueltos entre {fecha_i} - {fecha_f}")
    else:
        time = result[1]
        data = result[0]
        headers = ["Identificador del crimen", "Fecha", "Hora", "Area", "Subarea", "Gravedad", "Código del crimen", "Estado del caso", "fecha rptd", "area nombre"]
        if ar.size(data) < 5:
            print(print(tb.tabulate(data["elements"], headers, tablefmt="pretty")))
        else:
            primeros = ar.sub_list(data, 5, 5)["elements"][::-1]
            ultimos = ar.sub_list(data, 0, 5)["elements"][::-1]
            print(time)
            print(f"\nLos primeros 5 crimenes resueltos entre {fecha_i} - {fecha_f} son:\n")
            print(tb.tabulate(primeros, headers, tablefmt="pretty"))
            print(f"\nLos ultimos 5 crimenes resueltos entre {fecha_i} - {fecha_f} son:\n")
            print(tb.tabulate(ultimos, headers, tablefmt="pretty"))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    n = int(input("Ingrese el número de datos que deseas analizar: "))
    area_name = input("Ingrese el área por la cual quiere filtrar: ")
    result = lg.req_3(control, n, area_name)
    if result == None:
        print("No se encontraron crimenes en el área buscada: ")
    else:
        print(result[1])
        print(result[2])
        headers = ["Identificador del crimen", "Fecha", "Hora", "Area", "Subarea", "Gravedad", "Codigo del crimen", "Estado del caso", "Dirección", "Fecha de reporte", "Nombre del Area"]
        data = result[0]["elements"]
        print(f"\nLos {n} crimenes mas recientemente reportados en {area_name} son:\n")
        print(tb.tabulate(data, headers, tablefmt="pretty"))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    n = int(input("Ingrese el número de registros a mostrar: "))
    edad_i = input("Ingrese la edad inicial: ")
    edad_f = input("Ingrese la edad final: ")

    if int(edad_i) > int(edad_f):
        print("\nLa edad inicial no puede ser mayor que la edad final.")
        return
    
    resultado = lg.req_4(control, n, edad_i, edad_f)
    print(f"Resultado de req_4: {resultado}")

    if resultado is None:
        print(f"\nNo se encontraron registros para el rango de edades {edad_i} - {edad_f}.")
        return
    
    else:
            # Información detallada de los crímenes
        headers = ["ID Reporte", "Fecha del Crimen", "Hora del Crimen", "Área", 
                "Subárea", "Gravedad", "Código Crimen", "Edad Víctima", 
                "Estado del Caso", "Dirección"]
        info = []

            # Mostrar todos los registros encontrados
        for mapa in resultado["elements"]:
            info.append([
                    lp.get(mapa, "id_reporte"),
                    lp.get(mapa, "fecha_crimen"),
                    lp.get(mapa, "hora_crimen"),
                    lp.get(mapa, "area"),
                    lp.get(mapa, "subarea"),
                    lp.get(mapa, "gravedad"),
                    lp.get(mapa, "codigo_crimen"),
                    lp.get(mapa, "edad_victima"),
                    lp.get(mapa, "estado_caso"),
                    lp.get(mapa, "direccion")
                ])
        print(f"\nLos registros encontrados para el rango de edades {edad_i} - {edad_f} son:\n")
        print(tb.tabulate(info, headers, tablefmt="pretty"))

def print_req_5(control):
    
    n = int(input("Ingrese el número de datos que deseas analizar: "))
    start_date = input("Ingrese la fecha inical del rango en formato yyyy-mm-dd: ")
    end_date = input("Ingrese la fecha final del rango en formato yyyy-mm-dd: ")

    result = lg.req_5(control, n, start_date, end_date)
    info = []
    for mapa in result["elements"]:
        area = int(lp.get(mapa, "area"))
        area_name = lp.get(mapa, "area_name")
        crime_count = lp.get(mapa, "crime_count")
        first_crime_date = lp.get(mapa, "first_crime_date")
        last_crime_date = lp.get(mapa, "last_crime_date")
        info.append([area, area_name, crime_count, first_crime_date, last_crime_date])

    headers = ["Area", "Nombre del area", "Cantidad de crimenes", "Fecha del primer crimen", "Fecha del último crimen"]
    print(f"\nLas {n} áreas con mayor cantidad de crímenes sin resolver entre {start_date} y {end_date} son:\n")
    print(tb.tabulate(info, headers, tablefmt="pretty"))



def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """
    N = int(input("Ingrese el número de registros a mostrar: "))
    sexo = input("Ingrese el sexo a filtrar (M/F): ").strip().upper()
    mes = int(input("Ingrese el mes a filtrar (como un número del 1 al 12): "))

    # Llamar a la función del requerimiento 6
    result, tiempo_carga = lg.req_6(control, N, sexo, mes)

    if ar.size(result) == 0:
        print(f"\nNo se encontraron registros para el sexo '{sexo}' en el mes '{mes}'.")
    else:
        # Mostrar el tiempo de carga y el número total de áreas
        headers_generales = ["Tiempo de carga (ms)", "Número total de áreas"]
        print(tb.tabulate([[tiempo_carga, ar.size(result)]], headers_generales, tablefmt="pretty"))

        # Mostrar los detalles de las áreas
        headers = ["Área", "Nombre del Área", "Cantidad de Crímenes", "Años con Crímenes"]
        info = []

        for area_data in result["elements"]:
            area = lp.get(area_data, "area")
            area_name = lp.get(area_data, "area_name")
            crime_count = lp.get(area_data, "crime_count")
            year_count = rbt.value_set(lp.get(area_data, "year_count"))["elements"]
            info.append([area, area_name, crime_count, year_count])

        print(f"\nLas {N} áreas más seguras para el sexo '{sexo}' en el mes '{mes}' son:\n")
        print(tb.tabulate(info, headers, tablefmt="pretty"))




def print_req_7(control): 
    N = int(input("Ingrese el número de datos que deseas analizar: "))
    victim_sex_input = input("Ingrese el sexo de la víctima (M/F): ")
    victim_sex = victim_sex_input.upper().replace(" ", "")
    age_start = int(input("Ingrese la edad mínima de la víctima: "))
    age_end = int(input("Ingrese la edad máxima de la víctima: "))

    result = lg.req_7(control, N, victim_sex, age_start, age_end)
    lista_de_mapas = result[0]
    tiempo = result[1]

    headers = ["Código del crimen", "Nº de crímenes", "Nº de crímenes ocurridos por edad (crímenes, edad)", "Nº de crímenes ocurridos por año (crímenes, año)"]
    info = []
    for mapa in lista_de_mapas["elements"]:
        crime_code = int(lp.get(mapa, "crime_code"))
        crime_count = int(lp.get(mapa, "crime_count"))
        edades = rbt.value_set(lp.get(mapa, "age_count"))
        years = rbt.value_set(lp.get(mapa, "year_count"))

        info.append([crime_code, crime_count, edades["elements"], years["elements"]])

    print(f"\nLos {N} crimenes con mayor cantidad de víctimas entre {age_start} y {age_end} años son:\n")
    print(tb.tabulate(info, headers, tablefmt="pretty"))
    print(f"\nEl tiempo de ejecución del requerimiento 7 es: {tiempo} segundos\n")

    



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

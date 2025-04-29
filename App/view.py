import sys
from App import logic as lg
from DataStructures.List import array_list as ar
from DataStructures.Map import map_linear_probing as lp
import tabulate as tb
import csv  

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
        headers = ["Identificador del crimen", "Fecha", "Hora", "Area", "Subarea", "Gravedad", "Código del crimen", "Estado del caso", "Fevha de reporte"]
        if ar.size(data) < 5:
            print(print(tb.tabulate(data["elements"], headers, tablefmt="pretty")))
        else:
            primeros = ar.sub_list(data, 5, 5)["elements"]
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
        headers = ["Identificador del crimen", "Fecha", "Hora", "Area", "Subarea", "Gravedad", "Codigo del crimen", "Estado del caso", "Dirección"]
        data = result[0]["elements"]
        print(f"\nLos {n} crimenes mas recientemente reportados en {area_name} son:\n")
        print(tb.tabulate(data, headers, tablefmt="pretty"))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


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
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


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

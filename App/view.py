import sys
from App import logic as lg
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
    file_path = f"Data/Crime_in_LA/{file}" 

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
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    N = input("Ingrese el número de registros a mostrar: ")
    edad_i = input("Ingrese la edad inicial: ")
    edad_f = input("Ingrese la edad final: ")

    if int(edad_i) > int(edad_f):
        print("\nLa edad inicial no puede ser mayor que la edad final.")
    else:
        # La función req_4 retorna el tiempo de carga, el número total de crímenes y los resultados
        tiempo_carga, total_crimenes, result = lg.req_4(control, N, edad_i, edad_f)

        if result is None or ar.size(result[1]["elements"]) == 0:
            print(f"\nNo se encontraron registros para el rango de edades {edad_i} - {edad_f}.")
        else:
            # Número total de crímenes que cumplen el criterio
            headers_generales = ["Tiempo de carga (s)", "Número total de crímenes"]
            print(tb.tabulate([[tiempo_carga, total_crimenes]], headers_generales, tablefmt="pretty"))

            # Información detallada de los crímenes
            headers = [
                "ID Reporte", "Fecha del Crimen", "Hora del Crimen", "Área", 
                "Subárea", "Gravedad", "Código Crimen", "Edad Víctima", 
                "Estado del Caso", "Dirección"
            ]

            if ar.size(result[1]["elements"]) <= int(N):
                print(f"\nLos registros encontrados para el rango de edades {edad_i} - {edad_f} son:\n")
                print(tb.tabulate(result[1]["elements"], headers, tablefmt="pretty"))
            else:
                primeros_5 = ar.sub_list(result[1]["elements"], 0, 5)
                ultimos_5 = ar.sub_list(result[1]["elements"], ar.size(result[1]["elements"]) - 5, 5)
                print(f"\nLos primeros 5 registros para el rango de edades {edad_i} - {edad_f} son:\n")
                print(tb.tabulate(primeros_5["elements"], headers, tablefmt="pretty"))
                print(f"\nLos últimos 5 registros para el rango de edades {edad_i} - {edad_f} son:\n")
                print(tb.tabulate(ultimos_5["elements"], headers, tablefmt="pretty"))



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    N = int(input("Ingrese el número de registros a mostrar: "))
    sexo = input("Ingrese el sexo a filtrar: ")
    mes = int(input("Ingrese el mes a filtrar: "))

    tiempo_carga, result = lg.req_6(control, N, sexo, mes)

    if ar.size(result) == 0:
        print(f"\nNo se encontraron registros para el sexo '{sexo}' en el mes '{mes}'.")
    else:
        # Número total de áreas que cumplen el criterio
        headers_generales = ["Tiempo de carga (ms)", "Número total de áreas"]
        print(tb.tabulate([[tiempo_carga, ar.size(result)]], headers_generales, tablefmt="pretty"))

        # Información detallada de las áreas
        headers = ["Área", "Nombre del Área", "Cantidad de Crímenes", "Años con Crímenes"]

        # Convertir los datos para tabular
        
        if ar.size(result[1]["elements"]) <= int(N):
            print(f"\nLos registros encontrados para el sexo '{sexo}' en el mes '{mes}' son:\n")
            print(tb.tabulate(result[1]["elements"], headers, tablefmt="pretty"))
        else:
            primeros_5 = ar.sub_list(result[1]["elements"], 0, 5)
            ultimos_5 = ar.sub_list(result[1]["elements"], ar.size(result[1]["elements"]) - 5, 5)
            print(f"\nLos primeros 5 registros para el sexo '{sexo}' en el mes '{mes}' son:\n")
            print(tb.tabulate(primeros_5["elements"], headers, tablefmt="pretty"))
            print(f"\nLos últimos 5 registros para el sexo '{sexo}' en el mes '{mes}' son:\n")
            print(tb.tabulate(ultimos_5["elements"], headers, tablefmt="pretty"))
    



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

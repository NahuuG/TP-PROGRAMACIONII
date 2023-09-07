import os
#import random
#import string

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append({'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1,"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"})
libros.append({'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2,"titulo": "El principito", "autor": "Antoine de Saint-Exupéry"})
libros.append({'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0,"titulo": "El código Da Vinci", "autor": "Dan Brown"})

# Función para mostrar el menú
def mostrar_menu():
    print("Menu:")
    print("1) Gestionar Préstamo")
    print("2) Gestionar Devolución")
    print("3) Registrar nuevo libro")
    print("4) Eliminar ejemplar")
    print("5) Mostrar ejemplares prestados")
    print("6) Salir")

# Función para gestionar el préstamo de un libro
def gestionar_prestamo():
    codigo = input("Ingrese el código del libro: ")
    for libro in libros: # Itera en el arreglo libros[]
        if libro['cod'] == codigo:
            if libro['cant_ej_ad'] > 0:
                print(f"Autor: {libro['autor']}")
                print(f"Título: {libro['titulo']}")
                print(f"Cantidad de ejemplares disponibles: {libro['cant_ej_ad']}")
                confirmar = input("¿Desea confirmar el préstamo? (si/no): ")
                if confirmar.lower() == "si" or confirmar.lower() == "s": # Solamente se confirma con "s" o "si"
                    libro['cant_ej_ad'] -= 1 # Del total de libros se resta porque se adquiere
                    libro['cant_ej_pr'] += 1 # Se suma al arreglo de prestados
                    print("Préstamo confirmado.") # Se confirma el prestamo 
                else:
                    print("Préstamo cancelado.") # Se cancela el prestamo
            else:
                print("No quedan ejemplares disponibles para prestar.")
            return
    print("Libro no encontrado.")




print("Bienvenido al sistema de la biblioteca 'José Manuel Estrada'")
respuesta = input("Presione una tecla para continuar....")
while respuesta != "salir" or respuesta == 6:
    mostrar_menu()
    opcion = input("\nIngrese la opción de menú: ")
    os.system("cls")  # Limpiar pantalla

    if opcion == "1":
        gestionar_prestamo()
    elif opcion == "2":
        print("gestionar_devolucion()")
    elif opcion == "3":
        print("registrar_nuevo_libro()")
    elif opcion == "4":
        print("eliminar_ejemplar_libro()")
    elif opcion == "5":
        print("mostrar_ejemplares_prestados()")
    elif opcion == "6" or opcion == "salir":
        print("Hasta luego!")
        print("\n")
        break
    else:
        print("Ingrese una opción válida.")

    input("Presione una tecla para continuar....")
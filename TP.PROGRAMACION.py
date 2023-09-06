import os
# Función para mostrar el menú
def mostrar_menu():
    print("Menu:")
    print("1) Gestionar Préstamo")
    print("2) Gestionar Devolución")
    print("3) Registrar nuevo libro")
    print("4) Eliminar ejemplar")
    print("5) Mostrar ejemplares prestados")
    print("6) Salir")

print("Bienvenido al sistema de la biblioteca 'José Manuel Estrada'")
respuesta = input("Presione una tecla para continuar....")
while opcion != "salir" or opcion == 6:
    mostrar_menu()
    opcion = input("\nIngrese la opción de menú: ")
    os.system("cls")  # Limpiar pantalla

    if opcion == "1":
        gestionar_prestamo()
    elif opcion == "2":
        gestionar_devolucion()
    elif opcion == "3":
        registrar_nuevo_libro()
    elif opcion == "4":
        eliminar_ejemplar_libro()
    elif opcion == "5":
        mostrar_ejemplares_prestados()
    elif opcion == "6" or opcion == "salir":
        print("Hasta luego!")
        print("\n")
        break
    else:
        print("Ingrese una opción válida.")

    input("Presione una tecla para continuar....")
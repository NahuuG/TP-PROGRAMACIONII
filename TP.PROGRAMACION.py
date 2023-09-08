import os
import random
import string

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
# Se usa el metodo .append para agregar los codigos, cantidad de libros prestados y adquiridos, el nombre del autor y los titulos 
libros.append({'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1,"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"})
libros.append({'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2,"titulo": "El principito", "autor": "Antoine de Saint-Exupéry"})
libros.append({'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0,"titulo": "El código Da Vinci", "autor": "Dan Brown"})

# Función para mostrar el menú
def mostrar_menu():
    print("Menu:")
    print("1) Gestionar Prestamo")
    print("2) Gestionar Devolucion")
    print("3) Registrar nuevo libro")
    print("4) Eliminar ejemplar")
    print("5) Mostrar ejemplares prestados")
    print("6) Salir")

# Funcion para gestionar el prestamo de un libro
# Opcion 1
def gestionar_prestamo(): # Declaracion de la funcion
    codigo = input("Ingrese el codigo del libro: ") # El codigo que se introduzca se va almacenar en la variable codigo
    for libro in libros: # Itera sobre arreglo libros[]
        if libro['cod'] == codigo: # Compara que el codigo que se introduzco en el input sea igual al que esta en el arreglo
            if libro['cant_ej_ad'] > 0: 
                print(f"Autor: {libro['autor']}") # f es para que muestre el valor dentro de las llaves
                print(f"titulo: {libro['titulo']}") # f es para que muestre el valor dentro de las llaves
                print(f"Cantidad de libros disponibles: {libro['cant_ej_ad']}") # f es para que muestre el valor dentro de las llaves
                confirmar = input("¿Desea confirmar el prestamo? (si/no): ")
                if confirmar == "si" or confirmar == "s": # Solamente se confirma con "s" o "si" 
                    libro['cant_ej_ad'] -= 1 # Se resta porque el libro fue adquirido
                    libro['cant_ej_pr'] += 1 # Se suma porque el libro fue prestado
                    print("Prestamo confirmado.") # Se confirma el prestamo 
                else:
                    print("Prestamo cancelado.") # Se cancela el prestamo
            else:
                print("No quedan libros disponibles para prestar.")
            return
    print("Libro no encontrado.")

# Funcion para gestionar la devolución de un libro
# Opcion 2
def gestionar_devolucion(): # Declaracion de la funcion
    codigo = input("Ingrese el codigo del libro: ") # El codigo que se introduzca se va almacenar en la variable codigo
    for libro in libros: # Itera sobre el diccionario libros[]
        if libro['cod'] == codigo: # Compara que el codigo que se introduzco en el input sea igual al que esta en el diccionario
            if  libro['cant_ej_pr']> 0:
                confirmar = input("¿Desea confirmar la devolucion? (si/no): ")
                if confirmar == ("si") or confirmar == ("s"):
                    libro['cant_ej_ad'] +=1 # Se suma porque el libro fue devuelto 
                    libro['cant_ej_pr'] -=1 # Se resta porque la cantidad de libros prestados ahora es menor
                    print("El libro fue devuelto correctamente")
                else:
                    print("La devolucion no se realizo")
            else:
                print("No hay libros prestados")
            return
    print("Libro no encontrado")

# Función para generar un código aleatorio de 8 caracteres
# Parte de la funcion 3
def generar_nuevo_codigo(): # Declaracion de la funcion
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod

# Funcion para registrar un nuevo libro
# Opcion 3
def registrar_nuevo_libro(): # Declaracion de la funcion
    codigo = generar_nuevo_codigo() # Llamada a la funcion
    titulo = input("Ingrese el titulo del libro: ") # Se registra el titulo del libro
    autor = input("Ingrese el nombre del autor: ") # Se registra el nombre del autor
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares disponibles: ")) #Pregunta cuantos libros hay disponible
    cant_ej_pr = 0 # Se inicializa con 0 libros prestados
    nuevo_libro = {'cod': codigo, 'cant_ej_ad': cant_ej_ad,'cant_ej_pr': cant_ej_pr, 'titulo': titulo, 'autor': autor}
    libros.append(nuevo_libro) # Se agrega los datoss cargados recientemente al diccionario
    print("Libro registrado con éxito.")
    print(f"Código del libro: {codigo}") # f es para que muestre el valor dentro de las llaves
  
# Función para eliminar un ejemplar de un libro
# Opcion 4
def eliminar_ejemplar_libro(): # Declaracion de la funcion
    codigo = input("Ingrese el código del libro: ") # Que introduzca el codigo para evaluar si un libro disponible o no
    for libro in libros:
        if libro['cod'] == codigo: # Se evalua que el codigo ingresado sea igual al del diccionario 
            if libro['cant_ej_ad'] > 0: # Si es mayo a 0 significa que si se puede eliminar 
                libro['cant_ej_ad'] -= 1
                print("Libro eliminado con exito.") # Se confirma la eliminacion
            else:
                print("No hay Libros disponibles para eliminar.") # Como es menor a 0 no se puede realizar la eliminacion
            return
    print("Libro no encontrado.") # No hay un libro con ese codigo


# Funcion para mostrar lso libros prestados
# Opcion 5
def mostrar_ejemplares_prestados(): # Declaracion de la funcion
    print("#" * 30)
    for libro in libros:
        print(f"Titulo: {libro['titulo']}") # f es para que muestre el valor dentro de las llaves
        print(f"Libros prestados: {libro['cant_ej_pr']}")
        print("-" * 30)      
       
        
# Programa principal
print("Bienvenido al sistema de la biblioteca 'José Manuel Estrada'")
respuesta = input("Presione una tecla para continuar....")
while respuesta != "salir" or respuesta == 6:
    mostrar_menu()
    opcion = input("\nIngrese la opcion de menu: ")
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
        print("Gracias por usar el sistema de la bilioteca.")
        print("Hasta luego!")
        print("\n")
        break
    else:
        print("Ingrese una opcion valida.")

    input("Presione una tecla para continuar....")
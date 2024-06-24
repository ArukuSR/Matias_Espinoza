import funcion as files
import csv
import time

with open ('Definiciones.csv', 'w') as Archive_csv:
    readingcsv = csv.DictReader (Archive_csv)


lista_productos=[];

while True:
    print("---Menú de Opciones---\n")
    print("Opción 1.-Agregar un producto")
    print("Opción 2.- Ver todos los productos")
    print("Opción 3.- Modificar un producto")
    print("Opción 4.-Eliminar un producto")
    print("Opción 5.- Guardar colección en archivo")
    print("Opción 6.-Salir del programa")

    try:
        opcion=int(input("Elige una opción: "))
    except ValueError:
        print("Opción no valida, elige una opción del 1 al 5")
    else:
        if opcion==1:
            print("Elegiste la opción 1, agregar producto")
            files.agregar_productos()
        elif opcion==2:
            print("Elegiste la opción 2, ver todos los productos...")
            files.lista_productos();
        elif opcion==3:
            print("Elegiste la opción 3, Modificar tus productos")

        elif opcion==4:
            print("Elegiste la opción 4, Eliminar producto")
            files.eliminar_productos();
        
        elif opcion==5:
            print("Elegiste la opción 5, Guardar colección en un archivo")
            files.guardar_archivo()
        elif opcion==6:
            print("Elegiste la opción 6, Salir del programa")
            print("Saliendo Del Programa...")
            time.sleep(3)
            print("Saliste del programa")
            break;
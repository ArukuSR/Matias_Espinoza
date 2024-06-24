import csv
productos=[]
precios=[]
codigo=[]


def agregar_productos ():
    print("agregar productos")
    productos=input("agregar productos")

    print("agregar codigo de producto")
    codigo=input("agregar codigo de producto")

    print("agregar cantidad de producto")
    cantidad=int(input("agregar cantidad de producto"))

    print("agregar precio")
    Precio=int(input("agregar precio"))

    lista_de_productos= {
'productos':productos,
'codigo':codigos,
'cantidad':cantidad,
'precio':precios
}

    precios.append(precios)

def eliminar_productos():
    el = input("Producto a eliminar--> ")
    lista_productos.remove(el)
    print ("Producto eliminado con exito")


def guardar_archivo():
    lista_productos.input(readingcsv)
    codigo = fila['Codigo']
    nombre = fila ['Nombre']
    cantidad = fila['Cantidad']
    precio = int(fila['Precio'])
    print ("***Codigo***Nombre***Cantidad***Precio")
    for fila in readingcsv:
        print (f"***{codigo}***{nombre}***{cantidad}***{precio}***")

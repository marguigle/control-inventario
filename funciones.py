import uuid
from models import Producto

lista_productos = []


def menu_principal():
    print(
        """        #######################################
                GESTION DE STOCK
        #######################################\n"""
    )
    print("Elija una opcion")
    print("opcion 1: Agregar un producto")
    print("opcion 2: Ver lista completa de productos")
    print("opcion 3: Eliminar un producto de la lista")
    print("opcion 4: Buscar un producto especifico de la lista")
    print("opcion 5: Actualizar un producto")
    print("opcion 6: mostrar stock de un  producto")
    print("opcion 7: detectar stock bajo (menos de 10 unidades)")
    print("opcion 8: Salir del menú\n")


#### agregar producto
def agregar_producto():
    unique_id = str(uuid.uuid4())
    id = unique_id
    nombre = input("agregue el nombre producto\n ").lower()
    precio = float(input("abregue el precio del producto\n "))
    cantidad = int(input("agregue la cantidad del producto\n"))
    nuevo_producto = Producto(id, nombre, precio, cantidad)
    print("-" * 80)
    print(f"el producto {nombre} se ha agregado al stock correctamente !!!")

    lista_productos.append(nuevo_producto.__dict__)


#### buscar producto por nombre
def buscar_un_producto():
    try:

        nombre_producto = input(
            "ingrese el nombre del producto que desea buscar: \n"
        ).lower()

        producto = list(
            filter(
                lambda producto: producto["nombre"] == nombre_producto, lista_productos
            )
        )
        if producto == []:
            print(f"No se encuentra disponible el producto {nombre_producto} en stock")
        else:
            print(producto)

    except:
        print("-" * 80)
        print(f"Error el producto {nombre_producto} no se encuentra en la lista")


def eliminar_producto():
    try:
        nombre_producto = input(
            "ingrese el nombre del producto que desea eliminar: \n"
        ).lower()
        producto = list(
            filter(
                lambda producto: producto["nombre"] == nombre_producto, lista_productos
            )
        )

        lista_productos.remove(producto[0])
        print(f"El producto {producto[0]['nombre']} se ha eliminado correctamente ..!")

    except:
        print("-" * 80)
        print(f"Error el producto {nombre_producto} no se encuentra en la lista")


######  actualizar producto  ######


def actualizar_producto():
    nombre_producto = input(
        "ingrese el nombre del producto que desea actualizar: \n"
    ).lower()
    producto = list(
        filter(lambda producto: producto["nombre"] == nombre_producto, lista_productos)
    )
    nombre = input("agregue el nombre producto\n ").lower()
    precio = float(input("agregue el precio del producto\n "))
    cantidad = int(input("agregue la cantidad del producto\n"))

    producto[0]["nombre"] = nombre
    producto[0]["precio"] = precio
    producto[0]["cantidad"] = cantidad
    print(f"el producto {producto[0]['nombre']} se ha actualizado correctamente")


#### mostrar stock ####


def mostrar_stock():
    nombre_producto = input("ingrese el nombre del producto que desea ver el stock: \n")
    producto = list(
        filter(lambda producto: producto["nombre"] == nombre_producto, lista_productos)
    )
    if producto[0]["cantidad"] <= 10:

        print(f"stock bajo {producto[0]["cantidad"]} unidades")
    else:
        print(
            f"el stock de producto {producto[0]["nombre"]} es de {producto[0]["cantidad"]} unidades"
        )


####### detectar stock bajo #####
def detectar_stock_bajo():
    lista_bajo_stock = list(
        filter(lambda producto: producto["cantidad"] <= 10, lista_productos)
    )

    if lista_bajo_stock:

        print("############    PRODUCTOS CON STOCK BAJO    ############")
        print(f"{'ID':^35} {'Nombre':^15} {'Precio':^10} {'Cantidad':^10}")
        print("-" * 80)
        for producto in lista_bajo_stock:
            print(
                f"{producto['id']:^5} {producto['nombre']:^15} {producto['precio']:^10.2f} {producto['cantidad']:^10}"
            )

    else:
        print("No hay productos con bajo stock en la lista.")

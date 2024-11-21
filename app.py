from funciones import *


#### menu principal


############  APP PRINCIPAL  #############


def main():

    menu_principal()
    while True:
        opcion_elegida = input("elija una opcion: ")
        if opcion_elegida == "1":
            agregar_producto()
            print("-" * 80)
            menu_principal()
        elif opcion_elegida == "2":
            if lista_productos:

                print(f"{'ID':^35} {'Nombre':^15} {'Precio':^10} {'Cantidad':^10}")
                print("-" * 80)
                for producto in lista_productos:
                    print(
                        f"{producto['id']:^5} {producto['nombre']:^15} {producto['precio']:^10.2f} {producto['cantidad']:^10}"
                    )
                print("-" * 80)
                menu_principal()
            else:
                print("-" * 80)
                print("No hay productos en la lista.")
                print("-" * 80)
                menu_principal()
        elif opcion_elegida == "3":
            eliminar_producto()
            print("-" * 80)
            menu_principal()
        elif opcion_elegida == "4":
            buscar_un_producto()
            print("-" * 80)
            menu_principal()
        elif opcion_elegida == "5":
            actualizar_producto()
            print("-" * 80)
            menu_principal()
        elif opcion_elegida == "6":
            mostrar_stock()
            print("-" * 80)
            menu_principal()
        elif opcion_elegida == "7":
            detectar_stock_bajo()
            print("-" * 80)
            menu_principal()
        elif opcion_elegida == "8":
            print("\nHASTA PRONTO !!!")
            break

        else:
            print("Elija una opcion válida. debe ser un número del 1 al 8 ")
            main()


main()

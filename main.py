from backend.producto import listar_productos, consultar_producto
from frontend.menu import mostrar_menu, mostrar_productos, mostrar_producto

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            productos = listar_productos()
            mostrar_productos(productos)

        elif opcion == "2":
            id_producto = input("Ingrese el Id del producto: ")
            producto = consultar_producto(id_producto)
            mostrar_producto(producto)

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

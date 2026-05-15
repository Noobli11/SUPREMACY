from tabulate import tabulate
from utils.limpiar import limpiar

def mostrar_menu():
    limpiar()
    print("==============================")
    print("   Gestión de Productos")
    print("==============================")
    print("1. Listar productos")
    print("2. Consultar producto")
    print("0. Salir")
    print("==============================")
    opcion = input("Seleccione una opción: ")
    return opcion

def mostrar_productos(productos):
    limpiar()
    headers = ["Id", "Nombre", "Precio", "Cantidad"]
    print("\n--- Listado de Productos ---")
    print(tabulate(productos, headers=headers, tablefmt="grid"))
    input("\nPresione Enter para continuar...")

def mostrar_producto(producto):
    limpiar()
    if producto is None:
        print("\nProducto no encontrado.")
    else:
        headers = ["#", "Id", "Nombre", "Precio", "Cantidad"]
        print("\n--- Producto Encontrado ---")
        print(tabulate([producto], headers=headers, tablefmt="grid"))
    input("\nPresione Enter para continuar...")

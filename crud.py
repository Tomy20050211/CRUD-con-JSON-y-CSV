import json
import csv


productos = []

def agregarProductos():
    nombre = input("\nNombre del producto: ")
    precio = input("\nPrecio del producto: ")
    cantidad = input("\nCantidad: ")

    producto = {
        "NOMBRE": nombre,
        "PRECIO": precio,
        "CANTIDAD": cantidad
    }

    productos.append(producto)
    print("\nAGREGADO CON EXITO !! \n" \
    f"{producto}")

def guardarJson():
    with open ("Productos.json", "w", encoding="utf-8" ) as archivo:
        json.dump(productos, archivo, indent = 4)
        print("\nAGREGADO EXITOSAMENTE A:\n" \
        "Productos.json")

def agregarCsv():
    with open ("Productos.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["NOMBRE", "PRECIO", "CANTIDAD"])

        for p in productos:
            writer.writerow([p["NOMBRE"], p["PRECIO"], p["CANTIDAD"]])
            
        print("\n DATOS AGRGADOS EXITOSAMENTE EN:\n" \
        "Productos.csv")


while True:
    print("\n===== MENÚ =====")
    print("\n1. Agregar producto")
    print("2. Guardar en JSON")
    print("3. Exportar en CSV")
    print("4. Salir")

    opcion = int(input("\nIngrese una opcion: "))

    if opcion == 1:
        agregarProductos()
    elif opcion == 2:
        guardarJson()
    elif opcion == 3:
        agregarCsv()
    elif opcion == 4:
        print ("Saliendo del programa...")
        break
    else:
        print("Opcion no valida....")

import csv
import json

productos = []
idProducto = 0

def agregarProductos():
    global idProducto 
    while True:
        try:
            nombre = input("\nNombre de su producto: ")
            precio = int(input("\nIngrese su precio: "))
            cantidad = int(input("\nIngrese la cantidad: "))
            break
        except ValueError:
            print("\nIngrese datos válidos.")

    idProducto += 1
    listaProducto = {
        "ID": idProducto,
        "NOMBRE": nombre,
        "PRECIO": precio,
        "CANTIDAD": cantidad
    }
    productos.append(listaProducto)

    print("\nPRODUCTO AGREGADO CON ÉXITO :)")
    print("=" * 50)
    print(f"Nombre: {nombre}\nPrecio: {precio}\nCantidad: {cantidad}\nID: {idProducto}")

def buscarProducto():
    if not productos:
        print("\nInventario vacío...")
        return
    
    buscar = input("\nIngrese nombre o ID a buscar: ").lower()
    print("\nRESULTADOS:")
    encontrado = False

    for p in productos:
        if buscar == str(p["ID"]) or buscar in p["NOMBRE"].lower():
            print("=" * 50)
            print(f"ID: {p['ID']}")
            print(f"Nombre: {p['NOMBRE']}")
            print(f"Precio: {p['PRECIO']}")
            print(f"Cantidad: {p['CANTIDAD']}")
            encontrado = True

    if not encontrado:
        print("\nNo se encontró ningún producto.")

def actualizarProducto():
    if not productos:
        print("\nNo hay productos para actualizar.")
        return

    try:
        idBuscar = int(input("\nIngrese el ID del producto a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for p in productos:
        if p["ID"] == idBuscar:
            print("\nProducto encontrado:")
            print(f"Nombre actual: {p['NOMBRE']}")
            print(f"Precio actual: {p['PRECIO']}")
            print(f"Cantidad actual: {p['CANTIDAD']}")

            print("\n--- NUEVOS DATOS (dejar vacío para NO cambiar) ---")
            nuevoNombre = input("Nuevo nombre: ")
            nuevoPrecio = input("Nuevo precio: ")
            nuevaCantidad = input("Nueva cantidad: ")

            if nuevoNombre:
                p["NOMBRE"] = nuevoNombre
            if nuevoPrecio.isdigit():
                p["PRECIO"] = int(nuevoPrecio)
            if nuevaCantidad.isdigit():
                p["CANTIDAD"] = int(nuevaCantidad)

            print("\nProducto ACTUALIZADO correctamente.")
            return

    print("\nNo existe un producto con ese ID.")

def eliminarProducto():
    if not productos:
        print("\nNo hay productos para eliminar.")
        return

    try:
        idEliminar = int(input("\nIngrese el ID del producto a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    for p in productos:
        if p["ID"] == idEliminar:
            print("\nProducto encontrado:")
            print(f"Nombre: {p['NOMBRE']}")
            print(f"Precio: {p['PRECIO']}")
            print(f"Cantidad: {p['CANTIDAD']}")

            confirm = input("\n¿Está seguro de eliminarlo? (s/n): ").lower()

            if confirm == "s":
                productos.remove(p)
                print("\nPRODUCTO ELIMINADO.")
            else:
                print("\nOperación cancelada.")
            return

    print("\nNo existe un producto con ese ID.")

def guardarJson():
    if not productos:
        print("\nNo hay productos para guardar.")
        return
    
    with open("Productos.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4)
    
    print("\nPRODUCTOS GUARDADOS EN Productos.json")

def exportarCsv():
    if not productos:
        print("\nNo hay productos para exportar.")
        return

    with open("Productos.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["ID", "NOMBRE", "PRECIO", "CANTIDAD"])

        for p in productos:
            writer.writerow([p["ID"], p["NOMBRE"], p["PRECIO"], p["CANTIDAD"]])

    print("\nPRODUCTOS EXPORTADOS EN Productos.csv")

while True:
    print("\n" + "=" * 50)
    print(" MENÚ PRINCIPAL ".center(50))
    print("=" * 50)

    print("\n1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Guardar en JSON")
    print("6. Exportar en CSV")
    print("7. Salir")

    try:
        opcion = int(input("\nIngrese una opción: "))
    except ValueError:
        print("Opción inválida.")
        continue

    if opcion == 1:
        agregarProductos()
    elif opcion == 2:
        buscarProducto()
    elif opcion == 3:
        actualizarProducto()
    elif opcion == 4:
        eliminarProducto()
    elif opcion == 5:
        guardarJson()
    elif opcion == 6:
        exportarCsv()
    elif opcion == 7:
        print("\nSaliendo del programa... ¡Hasta luego!")
        break
    else:
        print("\nOpción inválida, intente de nuevo.")

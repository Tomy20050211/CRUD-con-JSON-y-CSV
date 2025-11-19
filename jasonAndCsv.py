import json
import csv
import os

# Archivo donde se guardan los estudiantes
ARCHIVO_JSON = "estudiantes.json"


# -------------------------------
# 1. Leer datos
# -------------------------------
def leer_datos():
    if not os.path.exists(ARCHIVO_JSON):
        return []  # Si no existe, devolvemos una lista vacía

    with open(ARCHIVO_JSON, "r", encoding="utf-8") as file:
        return json.load(file)


# -------------------------------
# 2. Guardar datos
# -------------------------------
def guardar_datos(estudiantes):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as file:
        json.dump(estudiantes, file, indent=4, ensure_ascii=False)


# -------------------------------
# 3. Crear estudiante
# -------------------------------
def crear_estudiante():
    estudiantes = leer_datos()

    id = input("ID del estudiante: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")

    nuevo = {
        "id": id,
        "nombre": nombre,
        "edad": edad
    }

    estudiantes.append(nuevo)
    guardar_datos(estudiantes)

    print("Estudiante agregado.\n")


# -------------------------------
# 4. Actualizar estudiante por ID
# -------------------------------
def actualizar_estudiante():
    estudiantes = leer_datos()
    id_buscar = input("ID del estudiante a actualizar: ")

    for est in estudiantes:
        if est["id"] == id_buscar:
            est["nombre"] = input("Nuevo nombre: ")
            est["edad"] = input("Nueva edad: ")
            guardar_datos(estudiantes)
            print("Estudiante actualizado.\n")
            return

    print("No se encontró ese ID.\n")


# -------------------------------
# 5. Eliminar estudiante por ID
# -------------------------------
def eliminar_estudiante():
    estudiantes = leer_datos()
    id_buscar = input("ID del estudiante a eliminar: ")

    estudiantes_nuevos = [e for e in estudiantes if e["id"] != id_buscar]

    if len(estudiantes) == len(estudiantes_nuevos):
        print("No se encontró ese ID.\n")
    else:
        guardar_datos(estudiantes_nuevos)
        print("Estudiante eliminado.\n")


# -------------------------------
# 6. Exportar a CSV
# -------------------------------
def exportar_csv():
    estudiantes = leer_datos()

    with open("estudiantes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nombre", "Edad"])

        for e in estudiantes:
            writer.writerow([e["id"], e["nombre"], e["edad"]])

    print("Datos exportados a estudiantes.csv\n")


# -------------------------------
# Menú principal
# -------------------------------
def menu():
    while True:
        print("\n--- CRUD de Estudiantes ---")
        print("1. Crear estudiante")
        print("2. Actualizar estudiante")
        print("3. Eliminar estudiante")
        print("4. Exportar a CSV")
        print("5. Salir")

        op = input("Opción: ")

        if op == "1":
            crear_estudiante()
        elif op == "2":
            actualizar_estudiante()
        elif op == "3":
            eliminar_estudiante()
        elif op == "4":
            exportar_csv()
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")


menu()

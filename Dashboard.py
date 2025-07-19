import os
import subprocess

# ===============================
# Autor: Johao Caicedo
# Fecha: 19/07/2025
# Proyecto adaptado para organizar tareas y proyectos de la materia POO
# Cambios realizados:
# - Menús con formato de tabla
# - Ajuste para nombres largos
# - Función para registrar tareas
# - Comentarios explicativos
# ===============================

# Mostrar el código de un archivo .py
def mostrar_codigo(ruta_script):
    ruta_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# Ejecutar el archivo .py seleccionado
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux o Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# Nueva función para registrar tareas (simple en pantalla)
def registrar_tarea():
    print("\n--- REGISTRAR NUEVA TAREA ---")
    nombre = input("Escribe el nombre de tu tarea: ")
    fecha = input("¿Para cuándo es? (Ej: 20/07/2025): ")
    estado = input("¿Cómo está la tarea? (Pendiente / En proceso / Terminada): ")
    print("\nTarea registrada:")
    print(f"- Nombre: {nombre}")
    print(f"- Fecha de entrega: {fecha}")
    print(f"- Estado: {estado}")
    input("Presiona Enter para volver al menú...")

# Menú principal en formato de tabla
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\n+-----------------------------------------------------------+")
        print("|             DASHBOARD DE POO - JOHAO CAICEDO              |")
        print("+----------------+------------------------------------------+")
        print("| Opción         | Descripción                              |")
        print("+----------------+------------------------------------------+")
        for key, nombre in unidades.items():
            print(f"| {key:<14} | Ver proyectos de {nombre:<24}|")
        print("| T              | Registrar nueva tarea                    |")
        print("| 0              | Salir del programa                       |")
        print("+----------------+------------------------------------------+")

        eleccion = input("Tu opción: ").upper()

        if eleccion == '0':
            print("Gracias por usar el dashboard. Hasta luego.")
            break
        elif eleccion in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion])
            mostrar_sub_menu(ruta_unidad)
        elif eleccion == 'T':
            registrar_tarea()
        else:
            print("Opción no válida. Intenta de nuevo.")

# Submenú de carpetas (proyectos por unidad)
def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n+--------------------------------------------------+")
        print("|            SUBCARPETAS DISPONIBLES               |")
        print("+------------+-------------------------------------+")
        print("| Opción     | Carpeta                             |")
        print("+------------+-------------------------------------+")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            nombre_recortado = carpeta[:30] + ".." if len(carpeta) > 33 else carpeta
            print(f"| {i:<10} | {nombre_recortado:<35} |")
        print("| 0          | Volver al menú anterior             |")
        print("+------------+-------------------------------------+")

        eleccion = input("Tu opción: ")
        if eleccion == '0':
            break
        try:
            num = int(eleccion) - 1
            if 0 <= num < len(sub_carpetas):
                ruta_sub = os.path.join(ruta_unidad, sub_carpetas[num])
                mostrar_scripts(ruta_sub)
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, escribe un número.")

# Menú para ver y ejecutar scripts .py
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n+---------------------------------------------------------+")
        print("|                  SCRIPTS DISPONIBLES                    |")
        print("+------------+--------------------------------------------+")
        print("| Opción     | Archivo                                    |")
        print("+------------+--------------------------------------------+")
        for i, script in enumerate(scripts, start=1):
            nombre_recortado = script[:40] + ".." if len(script) > 43 else script
            print(f"| {i:<10} | {nombre_recortado:<42} |")
        print("| 0          | Volver al submenú anterior                 |")
        print("| 9          | Volver al menú principal                   |")
        print("+------------+--------------------------------------------+")

        eleccion = input("Tu opción: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        try:
            num = int(eleccion) - 1
            if 0 <= num < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[num])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input("¿Quieres ejecutarlo? (1: Sí / 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    input("Presiona Enter para continuar...")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, escribe un número.")

# Iniciar el programa
if __name__ == "__main__":
    mostrar_menu()
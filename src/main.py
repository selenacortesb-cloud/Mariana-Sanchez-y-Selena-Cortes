from validaciones import *
from clsUsuarios import clsUsuarios
from clsItem import clsItem
from administrador import exportar_csv
from datetime import datetime
import os

# CONSTANTES
DATA_DIR = "src/datos"
CERT_DIR = "src/certificados"
TAX_RATE = 0.23
VALID_TIMES = [5, 10, 15, 30]
ITEM_CATEGORIES = {
    "Videojuegos": "VID",
    "Libros": "LIB",
    "Musica y video": "MUS",
    "Herramientas": "HER",
    "Dinero": "DIN",
    "Miscelaneo": "MIS"
}

# USUARIOS
def cargar_usuarios():
    usuarios = []
    usuarios_file = f"{DATA_DIR}/usuarios.txt"
    if os.path.exists(usuarios_file):
        try:
            with open(usuarios_file, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(";")
                    if len(datos) == 5:
                        usuario = clsUsuarios(
                            datos[1],
                            datos[2],
                            datos[0],
                            datos[3],
                            int(datos[4])
                        )
                        usuarios.append(usuario)
        except FileNotFoundError:
            print("Archivo de usuarios no encontrado")
    return usuarios

def guardar_usuario(usuario):
    usuarios_file = f"{DATA_DIR}/usuarios.txt"
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(usuarios_file, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{usuario.documento};"
                f"{usuario.nombre};"
                f"{usuario.apellido};"
                f"{usuario.correo};"
                f"{usuario.tiempo_prestamo}\n"
            )
    except IOError as e:
        print(f"Error al guardar usuario: {e}")

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Nombre: ")
    if not validar_nombre(nombre):
        print("Nombre inválido")
        return
    apellido = input("Apellido: ")
    if not validar_apellido(apellido):
        print("Apellido inválido")
        return
    documento = input("Documento: ")
    if not validar_documento(documento):
        print("Documento inválido")
        return
    correo = input("Correo: ")
    if not validar_correo(correo):
        print("Correo inválido")
        return
    try:
        tiempo = int(input("Tiempo préstamo (5,10,15,30): "))
    except ValueError:
        print("Tiempo inválido")
        return
    if not validar_tiempo(tiempo):
        print("Tiempo inválido")
        return
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u.documento == documento:
            print("Ya existe un usuario con ese documento")
            return
    nuevo_usuario = clsUsuarios(
        nombre,
        apellido,
        documento,
        correo,
        tiempo
    )
    guardar_usuario(nuevo_usuario)
    print("Usuario registrado correctamente")

# ITEMS
def obtener_consecutivo_items():
    items_file = f"{DATA_DIR}/items.txt"
    try:
        if os.path.exists(items_file):
            with open(items_file, "r", encoding="utf-8") as archivo:
                return len(archivo.readlines()) + 1
    except IOError:
        pass
    return 1

def generar_id_item(categoria, consecutivo):
    if categoria not in ITEM_CATEGORIES:
        return None
    return ITEM_CATEGORIES[categoria] + str(consecutivo).zfill(3)

def guardar_item(item):
    items_file = f"{DATA_DIR}/items.txt"
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(items_file, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{item.codigo};"
                f"{item.nombre};"
                f"{item.categoria};"
                f"{item.precio};"
                f"{item.estado}\n"
            )
    except IOError as e:
        print(f"Error al guardar item: {e}")

def registrar_item():
    print("\n=== REGISTRO DE ITEM ===")
    nombre = input("Nombre del item: ")
    print("Categorías disponibles: Videojuegos, Libros, Musica y video, Herramientas, Dinero, Miscelaneo")
    categoria = input("Categoria: ")
    
    if categoria not in ITEM_CATEGORIES:
        print("Categoría inválida")
        return
    
    try:
        precio = float(input("Precio de compra: "))
    except ValueError:
        print("Precio inválido")
        return
    
    print("Estados disponibles: Excelente, Bueno, Regular, Malo")
    estado = input("Estado: ")
    
    consecutivo = obtener_consecutivo_items()
    codigo = generar_id_item(categoria, consecutivo)
    
    if codigo is None:
        print("Error al generar código del item")
        return
    
    item = clsItem(codigo, nombre, categoria, precio, estado)
    guardar_item(item)
    print(f"Item registrado correctamente. ID: {codigo}")

def usuario_existe(documento):
    usuarios_file = f"{DATA_DIR}/usuarios.txt"
    try:
        if os.path.exists(usuarios_file):
            with open(usuarios_file, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(";")
                    if datos[0] == documento:
                        return True
    except IOError:
        pass
    return False

def item_existe(codigo):
    items_file = f"{DATA_DIR}/items.txt"
    try:
        if os.path.exists(items_file):
            with open(items_file, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(";")
                    if datos[0] == codigo:
                        return True
    except IOError:
        pass
    return False

def guardar_prestamo(documento, codigo):
    prestamos_file = f"{DATA_DIR}/prestamos.txt"
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(prestamos_file, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{documento};"
                f"{codigo};"
                f"{datetime.now().date()}\n"
            )
    except IOError as e:
        print(f"Error al guardar préstamo: {e}")

def registrar_prestamo():
    print("\n=== REGISTRO DE PRESTAMO ===")
    documento = input("Documento usuario: ")
    if not usuario_existe(documento):
        print("Usuario no registrado")
        return
    codigo = input("Codigo item: ")
    if not item_existe(codigo):
        print("Item no existe")
        return
    guardar_prestamo(documento, codigo)
    print("Prestamo registrado correctamente")

def consultar_prestamos():
    print("\n=== PRESTAMOS ACTIVOS ===")
    prestamos_file = f"{DATA_DIR}/prestamos.txt"
    try:
        if os.path.exists(prestamos_file):
            with open(prestamos_file, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido.strip() == "":
                    print("No hay prestamos")
                else:
                    print(contenido)
        else:
            print("No hay prestamos registrados")
    except IOError as e:
        print(f"Error al consultar préstamos: {e}")

def generar_certificado(documento, codigo):
    try:
        os.makedirs(CERT_DIR, exist_ok=True)
        nombre_archivo = f"{CERT_DIR}/certificado_{documento}_{codigo}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("CERTIFICADO DE DEVOLUCION\n")
            archivo.write("========================\n")
            archivo.write(f"Usuario: {documento}\n")
            archivo.write(f"Item: {codigo}\n")
            archivo.write(f"Fecha: {datetime.now()}\n")
        print("Certificado generado")
    except IOError as e:
        print(f"Error al generar certificado: {e}")

def registrar_devolucion():
    documento = input("Documento usuario: ")
    codigo = input("Codigo item: ")
    prestamos_actuales = []
    encontrado = False
    prestamos_file = f"{DATA_DIR}/prestamos.txt"
    
    try:
        if os.path.exists(prestamos_file):
            with open(prestamos_file, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(";")
                    if datos[0] == documento and datos[1] == codigo:
                        encontrado = True
                    else:
                        prestamos_actuales.append(linea)
        
        if not encontrado:
            print("Prestamo no encontrado")
            return
        
        with open(prestamos_file, "w", encoding="utf-8") as archivo:
            archivo.writelines(prestamos_actuales)
        
        generar_certificado(documento, codigo)
        print("Devolucion registrada")
    except IOError as e:
        print(f"Error al registrar devolución: {e}")

def generar_factura():
    documento = input("Documento usuario: ")
    codigo = input("Codigo item: ")
    try:
        precio = float(input("Precio del item: "))
    except ValueError:
        print("Precio inválido")
        return
    
    subtotal = precio
    impuesto = subtotal * TAX_RATE
    total = subtotal + impuesto
    
    try:
        os.makedirs(CERT_DIR, exist_ok=True)
        nombre_archivo = f"{CERT_DIR}/factura_{documento}_{codigo}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("FACTURA DE VENTA\n")
            archivo.write("====================\n")
            archivo.write(f"Usuario: {documento}\n")
            archivo.write(f"Item: {codigo}\n")
            archivo.write(f"Subtotal: ${subtotal}\n")
            archivo.write(f"Impuesto 23%: ${impuesto}\n")
            archivo.write(f"TOTAL: ${total}\n")
        print("Factura generada correctamente")
    except IOError as e:
        print(f"Error al generar factura: {e}")

# MENU
def menu():
    while True:
        print("\n===== ALQUILOOP =====")
        print("1. Registrar usuario")
        print("2. Registrar item")
        print("3. Registrar prestamo")
        print("4. Registrar devolucion")
        print("5. Consultar prestamos")
        print("6. Generar venta")
        print("7. Exportar CSV")
        print("8. Salir")
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_item()
        elif opcion == "3":
            registrar_prestamo()
        elif opcion == "4":
            registrar_devolucion()
        elif opcion == "5":
            consultar_prestamos()
        elif opcion == "6":
            generar_factura()
        elif opcion == "7":
            exportar_csv()
        elif opcion == "8":
            print("Hasta luego")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()

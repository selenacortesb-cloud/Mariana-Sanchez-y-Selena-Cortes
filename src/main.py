from validaciones import *
from clsUsuarios import clsUsuarios
from clsItem import clsItem
from administrador import exportar_csv
import os

# USUARIOS
def cargar_usuarios():
usuarios = []
if os.path.exists("src/datos/usuarios.txt"):
    with open(
        "src/datos/usuarios.txt",
        "r",
        encoding="utf-8"
    ) as archivo:
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
return usuarios
def guardar_usuario(usuario):
with open(
    "src/datos/usuarios.txt",
    "a",
    encoding="utf-8"
) as archivo:
    archivo.write(
        f"{usuario.documento};"
        f"{usuario.nombre};"
        f"{usuario.apellido};"
        f"{usuario.correo};"
        f"{usuario.tiempo_prestamo}\n"
    )
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
tiempo = int(
    input(
        "Tiempo préstamo (5,10,15,30): "
    )
)
if not validar_tiempo(tiempo):
    print("Tiempo inválido")
    return
usuarios = cargar_usuarios()
for u in usuarios:
    if u.documento == documento:
        print(
            "Ya existe un usuario con ese documento"
        )
        return
nuevo_usuario = clsUsuarios(
    nombre,
    apellido,
    documento,
    correo,
    tiempo
)
guardar_usuario(
    nuevo_usuario
)
print(
    "Usuario registrado correctamente"
)
# ITEMS
def obtener_consecutivo_items():
try:
    with open(
        "src/datos/items.txt",
        "r",
        encoding="utf-8"
    ) as archivo:
        return len(
            archivo.readlines()
        ) + 1
except:
    return 1
def generar_id_item(
categoria,
consecutivo
):
prefijos = {
    "Videojuegos": "VID",
    "Libros": "LIB",
    "Musica y video": "MUS",
    "Herramientas": "HER",
    "Dinero": "DIN",
    "Miscelaneo": "MIS"
}
return (
    prefijos[categoria]
    + str(consecutivo).zfill(3)
)
def guardar_item(item):
with open(
    "src/datos/items.txt",
    "a",
    encoding="utf-8"
) as archivo:
    archivo.write(
        f"{item.codigo};"
        f"{item.nombre};"
        f"{item.categoria};"
        f"{item.precio};"
        f"{item.estado}\n"
    )
def registrar_item():
print("\n=== REGISTRO DE ITEM ===")
nombre = input(
    "Nombre del item: "
)
categoria = input(
    "Categoria (Videojuegos, Libros, Musica y video, Herramientas, Dinero, Miscelaneo): "
)
precio = float(
    input("Precio de compra: ")
)
estado = input(
    "Estado (Excelente, Bueno, Regular, Malo): "
)
consecutivo = obtener_consecutivo_items()
codigo = generar_id_item(
    categoria,
    consecutivo
)
item = clsItem(
    codigo,
    nombre,
    categoria,
    precio,
    estado
)
guardar_item(item)
print(
    f"Item registrado correctamente. ID: {codigo}"
)
def usuario_existe(documento):
with open(
    "src/datos/usuarios.txt",
    "r",
    encoding="utf-8"
) as archivo:
    for linea in archivo:
        datos = linea.strip().split(";")
        if datos[0] == documento:
            return True
return False
def item_existe(codigo):
with open(
    "src/datos/items.txt",
    "r",
    encoding="utf-8"
) as archivo:
    for linea in archivo:
        datos = linea.strip().split(";")
        if datos[0] == codigo:
            return True
return False
def guardar_prestamo(
documento,
codigo
):
from datetime import datetime
with open(
    "src/datos/prestamos.txt",
    "a",
    encoding="utf-8"
) as archivo:
    archivo.write(
        f"{documento};"
        f"{codigo};"
        f"{datetime.now().date()}\n"
    )
def registrar_prestamo():
print("\n=== REGISTRO DE PRESTAMO ===")
documento = input(
    "Documento usuario: "
)
if not usuario_existe(
    documento
):
    print(
        "Usuario no registrado"
    )
    return
codigo = input(
    "Codigo item: "
)
if not item_existe(
    codigo
):
    print(
        "Item no existe"
    )
    return
guardar_prestamo(
    documento,
    codigo
)
print(
    "Prestamo registrado correctamente"
)
def consultar_prestamos():
print("\n=== PRESTAMOS ACTIVOS ===")
try:
    with open(
        "src/datos/prestamos.txt",
        "r",
        encoding="utf-8"
    ) as archivo:
        contenido = archivo.read()
        if contenido.strip() == "":
            print(
                "No hay prestamos"
            )
        else:
            print(
                contenido
            )
except:
    print(
        "No hay prestamos registrados"
    )
def generar_certificado(
documento,
codigo
):
from datetime import datetime
nombre_archivo = (
    f"src/certificados/"
    f"certificado_{documento}_{codigo}.txt"
)
with open(
    nombre_archivo,
    "w",
    encoding="utf-8"
) as archivo:
    archivo.write(
        "CERTIFICADO DE DEVOLUCION\n"
    )
    archivo.write(
        "========================\n"
    )
    archivo.write(
        f"Usuario: {documento}\n"
    )
    archivo.write(
        f"Item: {codigo}\n"
    )
    archivo.write(
        f"Fecha: {datetime.now()}\n"
    )
print(
    "Certificado generado"
)
def registrar_devolucion():
documento = input(
    "Documento usuario: "
)
codigo = input(
    "Codigo item: "
)
prestamos_actuales = []
encontrado = False
with open(
    "src/datos/prestamos.txt",
    "r",
    encoding="utf-8"
) as archivo:
    for linea in archivo:
        datos = linea.strip().split(";")
        if (
            datos[0] == documento
            and datos[1] == codigo
        ):
            encontrado = True
        else:
            prestamos_actuales.append(
                linea
            )
if not encontrado:
    print(
        "Prestamo no encontrado"
    )
    return
with open(
    "src/datos/prestamos.txt",
    "w",
    encoding="utf-8"
) as archivo:
    archivo.writelines(
        prestamos_actuales
    )
generar_certificado(
    documento,
    codigo
)
print(
    "Devolucion registrada"
)
def generar_factura():
documento = input(
    "Documento usuario: "
)
codigo = input(
    "Codigo item: "
)
precio = float(
    input(
        "Precio del item: "
    )
)
subtotal = precio
impuesto = subtotal * 0.23
total = subtotal + impuesto
nombre_archivo = (
    f"src/certificados/"
    f"factura_{documento}_{codigo}.txt"
)
with open(
    nombre_archivo,
    "w",
    encoding="utf-8"
) as archivo:
    archivo.write(
        "FACTURA DE VENTA\n"
    )
    archivo.write(
        "====================\n"
    )
    archivo.write(
        f"Usuario: {documento}\n"
    )
    archivo.write(
        f"Item: {codigo}\n"
    )
    archivo.write(
        f"Subtotal: ${subtotal}\n"
    )
    archivo.write(
        f"Impuesto 23%: ${impuesto}\n"
    )
    archivo.write(
        f"TOTAL: ${total}\n"
    )
print(
    "Factura generada correctamente"
)
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
    opcion = input(
        "\nSeleccione una opcion: "
    )
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
        break
    else:
        print(
            "Opcion invalida"
        )
if **name** == "**main**":
menu()

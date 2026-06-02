from validaciones import *
from clsUsuarios import clsUsuarios
import os

def cargar_usuarios():
    usuarios = []
    if os.path.exists("src/data/usuarios.txt"):
        with open("src/data/usuarios.txt", "r", encoding="utf-8") as archivo:
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
    with open("src/data/usuarios.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{usuario.documento};{usuario.nombre};{usuario.apellido};{usuario.correo};{usuario.tiempo_prestamo}\n"
        )

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Nombre: ").strip()
    if not validar_nombre(nombre):
        print("Nombre inválido. Debe tener mínimo 3 letras y no contener números.")
        return
    apellido = input("Apellido: ").strip()
    if not validar_apellido(apellido):
        print("Apellido inválido. Debe tener mínimo 3 letras y no contener números.")
        return
    documento = input("Documento: ").strip()
    if not validar_documento(documento):
        print("Documento inválido. Debe tener entre 3 y 15 dígitos y solo números.")
        return
    correo = input("Correo: ").strip()
    if not validar_correo(correo):
        print("Correo inválido. Debe contener @ y terminar en .com")
        return
    tiempo = int(input("Tiempo de préstamo (5, 10, 15, 30): "))
    if not validar_tiempo(tiempo):
        print("Tiempo inválido. Solo se permiten 5, 10, 15 o 30 días.")
        return
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u.documento == documento:
            print("Ya existe un usuario con ese documento.")
            return
    nuevo_usuario = clsUsuarios(nombre, apellido, documento, correo, tiempo)
    guardar_usuario(nuevo_usuario)
    print("Usuario registrado correctamente.")

def menu():
    while True:
        print("\n===== ALQUILOOP =====")
        print("1. Registrar usuario")
        print("2. Registrar item")
        print("3. Registrar prestamo")
        print("4. Registrar devolucion")
        print("5. Consultar prestamos")
        print("6. Administrador")
        print("7. Salir")
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            print("Modulo registro item")
        elif opcion == "3":
            print("Modulo prestamos")
        elif opcion == "4":
            print("Modulo devoluciones")
        elif opcion == "5":
            print("Modulo consultas")
        elif opcion == "6":
            print("Modulo administrador")
        elif opcion == "7":
            print("Hasta luego")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()
cd ruta/a/tu/proyecto
python src/main.py

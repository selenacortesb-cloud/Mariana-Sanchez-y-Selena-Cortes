from validaciones import *

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

        opcion = input(
            "\nSeleccione una opcion: "
        )

        if opcion == "1":

            print(
                "Modulo registro usuario"
            )

        elif opcion == "2":

            print(
                "Modulo registro item"
            )

        elif opcion == "3":

            print(
                "Modulo prestamos"
            )

        elif opcion == "4":

            print(
                "Modulo devoluciones"
            )

        elif opcion == "5":

            print(
                "Modulo consultas"
            )

        elif opcion == "6":

            print(
                "Modulo administrador"
            )

        elif opcion == "7":

            print("Hasta luego")
            break

        else:

            print(
                "Opcion invalida"
            )


menu()

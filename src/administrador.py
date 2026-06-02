import pandas as pd


def exportar_csv():

    datos = []

    try:

        with open(
            "src/datos/prestamos.txt",
            "r",
            encoding="utf-8"
        ) as archivo:

            for linea in archivo:

                datos.append(
                    linea.strip().split(";")
                )

        df = pd.DataFrame(
            datos,
            columns=[
                "Documento",
                "Item",
                "Fecha"
            ]
        )

        df.to_csv(
            "src/exportaciones/prestamos.csv",
            index=False
        )

        print(
            "CSV generado correctamente"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

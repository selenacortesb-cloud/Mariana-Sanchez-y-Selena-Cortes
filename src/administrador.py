import pandas as pd


def exportar_prestamos_csv():

    datos = []

    try:

        with open(
            "src/data/prestamos.txt",
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
            "CSV exportado correctamente"
        )

    except:

        print(
            "No existen prestamos"
        )

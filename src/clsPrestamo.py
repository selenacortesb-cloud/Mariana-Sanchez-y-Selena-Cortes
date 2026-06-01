from datetime import datetime


class clsPrestamo:

    def __init__(
        self,
        documento_usuario,
        codigo_item
    ):

        self.documento_usuario = documento_usuario
        self.codigo_item = codigo_item
        self.fecha_prestamo = datetime.now()

    def mostrar_datos(self):

        return (
            f"{self.documento_usuario} - "
            f"{self.codigo_item}"
        )

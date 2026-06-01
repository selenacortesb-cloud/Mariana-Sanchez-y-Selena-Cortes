class clsUsuarios:

    def __init__(
        self,
        nombre,
        apellido,
        documento,
        correo,
        tiempo_prestamo
    ):

        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.correo = correo
        self.tiempo_prestamo = tiempo_prestamo

    def mostrar_datos(self):

        return (
            f"{self.nombre} "
            f"{self.apellido} "
            f"- {self.documento}"
        )

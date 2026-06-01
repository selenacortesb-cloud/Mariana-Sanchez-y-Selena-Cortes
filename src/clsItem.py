class clsItem:

    def __init__(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        estado
    ):

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.estado = estado

    def mostrar_datos(self):

        return (
            f"{self.codigo} - "
            f"{self.nombre}"
        )

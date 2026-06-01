def validar_nombre(nombre):

    return (
        nombre.isalpha()
        and len(nombre) >= 3
    )


def validar_apellido(apellido):

    return (
        apellido.isalpha()
        and len(apellido) >= 3
    )


def validar_documento(documento):

    return (
        documento.isdigit()
        and 3 <= len(documento) <= 15
    )


def validar_correo(correo):

    return (
        "@" in correo
        and correo.endswith(".com")
    )


def validar_tiempo(tiempo):

    return tiempo in [5, 10, 15, 30]

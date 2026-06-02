# Manual de Usuario - ALQUILOOP
## Descripción
ALQUILOOP es un sistema de gestión de préstamos desarrollado en Python que permite administrar usuarios, ítems, préstamos, devoluciones y ventas.
## Menú Principal
1. Registrar Usuario
2. Registrar Ítem
3. Registrar Préstamo
4. Registrar Devolución
5. Consultar Préstamos
6. Generar Venta
7. Exportar CSV
8. Salir
## Registro de Usuarios
Permite registrar usuarios validando:
* Nombre
* Apellido
* Documento
* Correo electrónico
* Tiempo de préstamo
## Registro de Ítems

Permite registrar:
* Nombre
* Categoría
* Precio
* Estado
Cada ítem recibe un código único.
## Registro de Préstamos
Permite asociar usuarios registrados con ítems registrados.
## Devoluciones
Permite devolver un ítem y genera un certificado automático.
## Ventas
Genera una factura con impuesto del 23%.
## Exportación CSV

Permite exportar la información de préstamos a formato CSV usando Pandas.

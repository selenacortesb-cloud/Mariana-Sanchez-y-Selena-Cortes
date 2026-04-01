## Integrantes

- Mariana Sánchez  
- Selena Cortés  

## Vínculos académicos

### Mariana Sánchez
- Programa: Ingeniería Industrial  
- Habilidades: análisis de datos, organización de información  
- Fortalezas: Responsabilidad, trabajo en equipo  

### Selena Cortés
- Programa: Ingeniería Industrial  
- Habilidades: Lógica de programación, gestión de procesos  
- Fortalezas: Compromiso, organización, trabajo colaborativo  

## Nombre del proyecto

** ALQUILOOP **

Sistema en Python orientado a la gestión eficiente de préstamos de objetos, permitiendo el registro de usuarios, control de inventario, seguimiento de préstamos, devoluciones y generación de ventas.
<img width="2000" height="2000" alt="Logo" src="https://github.com/user-attachments/assets/84251b5d-9eb9-481b-890e-75fbcd91132d" />

## Licencia

Este proyecto está bajo la licencia MIT.

## Reporte de visión

El sistema propuesto tiene como objetivo desarrollar una aplicación en Python basada en consola que permita gestionar de manera eficiente el préstamo de objetos entre usuarios.

Este software busca solucionar el problema de desorganización en el control de préstamos, permitiendo registrar usuarios, ítems, préstamos, devoluciones y ventas de manera estructurada y confiable.

El sistema brindará herramientas para realizar seguimiento a los objetos prestados, generar alertas por retrasos, emitir certificados de devolución y facturas de venta en caso de incumplimiento en los tiempos establecidos.

Se espera que el programa sea fácil de usar, accesible y funcional, permitiendo al usuario administrar su inventario y relaciones de préstamo sin necesidad de conocimientos técnicos avanzados.

### Beneficios del sistema:
- Organización eficiente de la información  
- Reducción de pérdidas de objetos  
- Automatización de procesos de control  
- Generación de reportes y documentos  

Este proyecto representa una solución práctica y escalable para la gestión de préstamos en entornos personales o pequeños grupos.

## Especificación de requisitos

### Requisitos funcionales

** Registro de usuarios **
- El sistema debe permitir registrar usuarios con nombre, apellido, documento y correo electrónico.
- El sistema debe validar que el nombre y apellido no contengan números y tengan mínimo tres caracteres.
- El sistema debe validar que el documento contenga solo números y tenga entre 3 y 15 dígitos.
- El sistema debe permitir seleccionar un tiempo de préstamo de 5, 10, 15 o 30 días.

** Registro de ítems **
- El sistema debe permitir registrar objetos con nombre, categoría y precio de compra.
- El sistema debe validar que el nombre del ítem tenga mínimo tres caracteres.
- El sistema debe asignar un ID único a cada ítem.
- El sistema debe clasificar los ítems en categorías predefinidas.

** Registro de préstamos **
- El sistema debe permitir registrar préstamos únicamente a usuarios existentes.
- El sistema debe permitir seleccionar un ítem disponible mediante su ID.
- El sistema debe registrar la fecha del préstamo.
- El sistema debe impedir prestar un ítem que ya esté prestado.

** Registro de devoluciones **
- El sistema debe permitir registrar devoluciones solo de préstamos activos.
- El sistema debe generar un certificado de devolución si el ítem es devuelto a tiempo.
- El sistema debe validar si el usuario tiene préstamos activos antes de permitir la devolución.

** Generación de ventas **
- El sistema debe generar una venta automática si el préstamo supera los 30 días.
- El sistema debe calcular el valor total incluyendo un 23% de impuesto.
- El sistema debe generar una factura de venta en archivo plano.

**Consulta de préstamos **
- El sistema debe mostrar los préstamos activos ordenados por cantidad de días.
- El sistema debe permitir consultar la información almacenada en archivos.

**Módulo administrador **
- El sistema debe permitir el acceso mediante usuario y contraseña.
- El sistema debe mostrar estadísticas generales como total de préstamos, devoluciones y ventas.
- El sistema debe identificar el usuario con mayor y menor cantidad de préstamos.

### Requisitos no funcionales

- El sistema debe ser desarrollado en el lenguaje de programación Python.
- El sistema debe funcionar en consola (interfaz de texto).
- El sistema debe ser fácil de usar e intuitivo para el usuario.
- El sistema debe almacenar la información en archivos planos.
- El sistema debe permitir exportar información a formato CSV.
- El sistema debe garantizar la integridad de los datos mediante validaciones.
- El sistema debe tener tiempos de respuesta rápidos en la ejecución de operaciones.
- El sistema debe ser organizado y modular mediante el uso de clases y objetos.

## Plan del proyecto

El proyecto se desarrollará en varias fases: análisis, diseño, desarrollo, pruebas y entrega final, permitiendo una organización adecuada del trabajo y cumplimiento de los objetivos planteados.

### Presupuesto del proyecto

El proyecto será desarrollado por un equipo de dos (2) estudiantes, quienes dedicarán un total de 50 horas de trabajo.

**Cálculo: **
- Número de integrantes: 2  
- Total de horas del proyecto: 50 horas  
- Valor estimado: 1 SMLV  

**Distribución del tiempo: **
- Cada integrante aporta aproximadamente 25 horas de trabajo.

**Justificación: **

El presupuesto no se refleja en pagos monetarios reales, sino en el valor del tiempo invertido en el desarrollo del proyecto, considerando actividades como análisis, diseño, programación, pruebas y documentación.

Este enfoque permite dimensionar el esfuerzo requerido para la construcción del software.

### Diagrama de Gantt

(![WhatsApp Image 2026-03-31 at 10 38 35 PM](https://github.com/user-attachments/assets/41e9693d-3939-49e7-90d0-da24b3e84a42)
 
## Actas

Las actas de entendimiento, colaboración y responsabilidad se encuentran en la carpeta "actas" del repositorio.

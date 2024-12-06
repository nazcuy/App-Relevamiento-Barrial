Modelo Module
=============

Este archivo define la conexión con la base de datos y las operaciones CRUD para la tabla `Vivienda`. También incluye la configuración de la base de datos utilizando `Peewee`.

Descripción General
-------------------
El módulo `modelo` proporciona las herramientas necesarias para interactuar con la base de datos SQLite. Contiene:
- Una clase para la conexión y gestión de la base de datos (`Conexion_de_BD`).
- Un modelo `Vivienda` que representa la tabla en la base de datos.
- Una clase `Abmc` para realizar operaciones de alta, baja, modificación y consulta de registros.

.. automodule:: modelo
   :members:
   :undoc-members:
   :show-inheritance:

Clases y Métodos
----------------
### Clase `Conexion_de_BD`
Gestiona la conexión y desconexión a la base de datos y permite la creación de tablas.

- **`conectar`:** Establece una conexión con la base de datos.
- **`desconectar`:** Cierra la conexión con la base de datos.
- **`crear_tabla`:** Crea las tablas necesarias en la base de datos.

### Clase `Vivienda`
Modelo que define los campos de la tabla `Vivienda`:
- **`nombre`:** Nombre del propietario o descripción de la vivienda.
- **`direccion`:** Dirección de la vivienda.
- **`educacion`:** Nivel educativo del propietario.

### Clase `Abmc`
Proporciona métodos para manipular los registros de la tabla `Vivienda`.

- **`alta_registro`:** Crea un nuevo registro.
- **`borrar_registro`:** Elimina un registro por su ID.
- **`modificar_registro`:** Modifica un registro existente.
- **`consultar_registro`:** Recupera y lista todos los registros.

Ejemplo de Uso
--------------
.. code-block:: python

   from modelo import Conexion_de_BD, Abmc

   # Crear conexión y tabla
   conexion = Conexion_de_BD("censo.db")
   conexion.conectar()
   conexion.crear_tabla()

   # Realizar operaciones CRUD
   abmc = Abmc()
   abmc.alta_registro("Casa de prueba", "Calle Falsa 123", "Primaria")
   registros = abmc.consultar_registro()
   for registro in registros:
       print(f"ID: {registro.id}, Nombre: {registro.nombre}, Dirección: {registro.direccion}, Educación: {registro.educacion}")
   conexion.desconectar()
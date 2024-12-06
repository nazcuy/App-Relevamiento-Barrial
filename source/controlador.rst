Controlador Module
==================

Este archivo contiene la implementación de la clase `Controlador`, que actúa como intermediario entre la `vista` y el `modelo`, manejando la lógica de negocio de la aplicación.

Descripción General
-------------------
El módulo `controlador` realiza las siguientes funciones principales:
- Gestionar las operaciones de alta, baja, modificación y consulta en el modelo.
- Coordinar la interacción entre la interfaz gráfica (vista) y la base de datos (modelo).
- Manejar errores y asegurarse de que los datos fluyen correctamente.

.. automodule:: controlador
   :members:
   :undoc-members:
   :show-inheritance:

Clases y Métodos
----------------
La clase principal de este módulo es `Controlador`. Sus métodos incluyen:

- **`realizar_alta`:** Llama al método de alta en el modelo para registrar una nueva vivienda.
- **`realizar_baja`:** Gestiona la eliminación de registros por ID.
- **`realizar_modificacion`:** Actualiza los datos de un registro existente.
- **`realizar_consulta`:** Recupera los registros almacenados en el modelo.

Ejemplo de Uso
--------------
Aquí tienes un ejemplo de cómo utilizar la clase `Controlador` para gestionar las operaciones:

.. code-block:: python

    from controlador import Controlador
    import vista

    mi_vista = vista.Vista()
    mi_controlador = Controlador(mi_vista)

    # Alta de un registro
    mi_controlador.realizar_alta("Casa de prueba", "Calle Falsa 123", "Primaria")

    # Consulta de registros
    registros = mi_controlador.realizar_consulta()
    for registro in registros:
        print(registro)

Detalles Adicionales
--------------------
La clase `Controlador` depende de los siguientes módulos:
- **`modelo`:** Para manejar las operaciones con la base de datos.
- **`vista`:** Para actualizar la interfaz gráfica.


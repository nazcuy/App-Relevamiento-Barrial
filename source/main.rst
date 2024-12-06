Main Module
===========

Este archivo contiene la documentación para el módulo `main`, que es el punto de entrada del programa. Aquí se describen sus funciones, clases y la lógica principal.

Descripción General
-------------------
El módulo `main` se encarga de:
- Iniciar el programa.
- Conectar los módulos `controlador`, `modelo` y `vista`.
- Gestionar el flujo general de la aplicación.

.. automodule:: main
   :members:
   :undoc-members:
   :show-inheritance:

Estructura del Módulo
---------------------
Las principales secciones del módulo incluyen:

- **Importaciones:** Listado de las bibliotecas y módulos necesarios.
- **Funciones principales:** Descripción de las funciones clave incluidas en este módulo.
- **Lógica principal:** Cómo se inicia y coordina la ejecución.

Ejemplo de Uso
--------------
A continuación se presenta un ejemplo de cómo iniciar el programa desde este módulo:

.. code-block:: python

    import tkinter as tk
	from vista import Aplicacion
	from modelo import Conexion_de_BD

	# Punto de entrada principal del programa.
	if __name__ == "__main__":
		# Inicializa la conexión a la base de datos y crea la tabla si no existe. 
		conexion = Conexion_de_BD()
		conexion.conectar()
		conexion.crear_tabla()
		# Crea la ventana principal.
		root = tk.Tk()
		# Instanciamos el objeto "app" de la clase Aplicación, que se encuentra en vista.py, y le pasamos como argumento la ventana principal "root"
		app = Aplicacion(root)
		# Inicia el bucle principal, va a estar esperando las interacciones del usuario.
		root.mainloop()
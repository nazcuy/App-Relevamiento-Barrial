# MAIN #
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
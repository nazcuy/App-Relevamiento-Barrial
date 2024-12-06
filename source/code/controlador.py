# CONTROLADOR #
from peewee import *
import modelo

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.abmc = modelo.Abmc()
       
    def realizar_alta(self, nombre, direccion, educacion):
        if self.abmc.alta_registro(nombre, direccion, educacion):
            print("Alta de vivienda", "¡La casa fue cargada con éxito!")
        else:
            print("Error", "No se pudo guardar la vivienda.")
        self.vista.actualizar_vista()

    def realizar_baja(self, vivienda_id):
        self.abmc.borrar_registro(vivienda_id)

    def realizar_modificacion(self, vivienda_id, nombre, direccion, educacion):
        try:
            self.abmc.modificar_registro(vivienda_id, nombre, direccion, educacion)
            print(f"Controlador: Registro con ID {vivienda_id} modificado correctamente.")
        except Exception as e:
            print(f"Controlador: Error al modificar el registro: {e}")
            raise

    def realizar_consulta(self):
        return self.abmc.consultar_registro()   

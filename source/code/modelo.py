# MODELO #
from peewee import *

basededatos = SqliteDatabase ("censo.db")


class Conexion_de_BD():
    def __init__(self, nombreBD="censo.db"):
        self.nombreBD = nombreBD
        self.basededatos = SqliteDatabase (self.nombreBD)

    def conectar(self):
        try:
            self.basededatos.connect()
            print(f"La conexión a {self.nombreBD} fue sumamente exitosa!")
        except OperationalError as e:
            print(f"Tenés un error al conectar la base de datos:{self.nombreBD}: {e}")
        finally:
            print(f"El intento de conectarse a la base de datos {self.nombreBD} ha finalizado.")

    def desconectar(self):
        if self.basededatos.is_closed():
            print("Conexión cerrada correctamente.")
        else:
            print("No se pudo hacer la desconexión, la base de datos está abierta.")

    def crear_tabla(self):
        self.basededatos.create_tables([Vivienda])
        
class Vivienda(Model):
    nombre = CharField()
    direccion = CharField()
    educacion = CharField()

    class Meta():
        database = basededatos

class Abmc:
    def alta_registro(self, nombre, direccion, educacion):
        try:
            nueva_vivienda = Vivienda.create(nombre=nombre, direccion=direccion, educacion=educacion)
            return True
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")
            return False
            
    def borrar_registro(self, vivienda_id):        
        try:
            # Intenta obtener la vivienda por su ID
            vivienda = Vivienda.get_by_id(vivienda_id)
            vivienda.delete_instance()  # Eliminar la vivienda
        except Vivienda.DoesNotExist:
            # Si no se encuentra el ID en la base de datos
            print(f"Modelo: No se encontró una vivienda con ID {vivienda_id}")
        
    def modificar_registro(self, vivienda_id, nombre, direccion, educacion):
        vivienda = Vivienda.get_by_id(vivienda_id)
        vivienda.nombre = nombre
        vivienda.direccion = direccion
        vivienda.educacion = educacion
        vivienda.save()
        print(f"Registro con ID {vivienda_id} actualizado en la base de datos.")
    
    def consultar_registro(self):
        registros = list(Vivienda.select())
        if registros:
            print("Registros en la base de datos:")
            for registro in registros:
                print(f"ID: {registro.id}, Nombre: {registro.nombre}, Dirección: {registro.direccion}, Educación: {registro.educacion}")
        else:
            print("No hay registros en la base de datos.")
        return registros
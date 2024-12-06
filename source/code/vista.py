# VISTA #
import tkinter as tk
from tkinter import ttk, messagebox, Label, Frame, Entry, StringVar, Button, N, S, E, W
from controlador import Controlador
from modelo import Vivienda
from peewee import *
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Aplicacion:
    def __init__(self, root):
        self.controlador = Controlador(self)
        root.title("ORGANIZACIÓN DE LA COMUNIDAD - Gestor de gobierno popular")
        root.rowconfigure(1, weight=1)  
        root.rowconfigure(2, weight=1)
        root.columnconfigure(1, weight=3)

        titulo = Label(root, text="RELEVAMIENTO BARRIAL", bg="#253876", fg="#fdc444", font=("Open Sans ExtraBold", 16))
        titulo.grid(row=0, column=0, columnspan=2, sticky=E+W)

        # Marco izquierdo
        marco_izquierdo = Frame(root, padx=5, pady=5, bg="#f5efe1")
        marco_izquierdo.grid(row=1, column=0, sticky=N+S+E+W)
        marco_izquierdo.columnconfigure((0, 1), weight=1)

        # Marco para gráfico
        self.marco_grafico = Frame(root, bg="white", padx=5, pady=5)
        self.marco_grafico.grid(row=1, column=1, sticky=N+S+E+W)
        self.marco_grafico.rowconfigure(0, weight=1)
        self.marco_grafico.columnconfigure(0, weight=1)

        # Marco para datos (Treeview, ocupa la mitad inferior)
        marco_datos = Frame(root, bg="lightgrey", padx=5, pady=5)
        marco_datos.grid(row=2, column=1, sticky=N+S+E+W)
        marco_datos.rowconfigure(0, weight=1)
        marco_datos.columnconfigure(0, weight=1)
        
        nombre = Label(marco_izquierdo, text="Nombre y Apellido: ", bg="#f5efe1", fg="#000000", font=("Open Sans", 10, "italic"))
        nombre.grid(row=0, column=0, sticky=W)
        direcc=Label(marco_izquierdo, text="Dirección Relevada: ", bg="#f5efe1", fg="#000000", font=("Open Sans", 10, "italic"))
        direcc.grid(row=1, column=0, sticky=W)
        educ=Label(marco_izquierdo, text="Educación Alcanzada: ", bg="#f5efe1", fg="#000000", font=("Open Sans", 10, "italic"))
        educ.grid(row=2, column=0, sticky=W)

         # Variables para entradas
        self.a_val, self.b_val, self.c_val = StringVar(), StringVar(), StringVar()

        # Entradas
        Entry(marco_izquierdo, textvariable=self.a_val).grid(row=0, column=1, sticky=W+E)
        Entry(marco_izquierdo, textvariable=self.b_val).grid(row=1, column=1, sticky=W+E)
        Entry(marco_izquierdo, textvariable=self.c_val).grid(row=2, column=1, sticky=W+E)

        # Botones
        Button(marco_izquierdo, text="Alta", command=lambda: self.alta(),
               bg="#336699", fg="white", font=("Open Sans ExtraBold", 9)).grid(row=3, column=0, pady=10)
        Button(marco_izquierdo, text="Baja", command=lambda: self.borrar(),
               bg="#336699", fg="white", font=("Open Sans ExtraBold", 9)).grid(row=3, column=1, pady=10)
        Button(marco_izquierdo, text="Modificar", command=lambda: self.modificar(),
               bg="#336699", fg="white", font=("Open Sans ExtraBold", 9)).grid(row=4, column=0, pady=10)
        Button(marco_izquierdo, text="Consultar lista", command=lambda: self.consulta(),
               bg="#336699", fg="white", font=("Open Sans ExtraBold", 9)).grid(row=4, column=1, pady=10)

        # Treeview
        self.tree = ttk.Treeview(marco_datos, columns=("id", "col1", "col2", "col3"), show="headings")
        self.tree.heading("id", text="Id")
        self.tree.heading("col1", text="Nombre y apellido")
        self.tree.heading("col2", text="Dirección relevada")
        self.tree.heading("col3", text="Educación alcanzada")
        self.tree.grid(row=0, column=0, sticky=N+S+E+W)
        self.actualizar_vista()

        #Alta
    def alta(self):
        nombre = self.a_val.get()
        direccion = self.b_val.get()
        educacion = self.c_val.get()
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            messagebox.showerror("Error", "El nombre solo puede contener letras y espacios.")
        else:
            self.controlador.realizar_alta(nombre, direccion, educacion)  # Solo se ejecuta si la validación pasa.
            messagebox.showinfo("Alta de vivienda", "¡La vivienda fue cargada con éxito!")
        self.actualizar_vista()
        self.actualizar_grafico()

        #Baja
    def borrar(self):
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion[0])
            vivienda_id = item["values"][0]
            print(f"Valor de vivienda_id: {vivienda_id} (tipo: {type(vivienda_id)})")
            self.controlador.realizar_baja(vivienda_id)
            messagebox.showinfo("Borrar vivienda", "¡La vivienda fue borrada con éxito!")
            self.actualizar_vista()
            self.actualizar_grafico()

        #Modificación
    def modificar(self):
        global id_modificar  # Almacena el ID del registro que se va a modificar
        seleccion_item = self.tree.selection()
        if seleccion_item:
            # Obtiene los datos de la fila seleccionada
            item = self.tree.item(seleccion_item)
            id_modificar = item['values'][0]
            nombre = item['values'][1]
            direccion = item['values'][2]
            educacion = item['values'][3]
            self.a_val.set(nombre)
            self.b_val.set(direccion)
            self.c_val.set(educacion)
            self.tree.delete(seleccion_item)
            print(f"Modificar: ID={id_modificar}, Nombre={nombre}, Dirección={direccion}, Educación={educacion}")
        try:
            self.registro = Vivienda.get(Vivienda.id == id_modificar)
            self.registro.delete_instance()
            print(f"Registro eliminado de la base de datos: {id_modificar}")
        except Vivienda.DoesNotExist:
            print("Error: No se encontró el registro en la base de datos")
            print(f"Registro eliminado: {id_modificar}, {nombre}, {direccion}, {educacion}")
        else:
            messagebox.showinfo("Registro eliminado.", "Ahora puede cargar los datos modificados.")
            return

        #Consulta
    def consulta(self):
        self.controlador.realizar_consulta()
        self.actualizar_vista()
        self.actualizar_grafico()

    def actualizar_grafico(self):
        # Limpia cualquier contenido previo en el marco
        for widget in self.marco_grafico.winfo_children():
            widget.destroy()

        # Se cuenta cuántas veces se repite cada categoría en el campo 'Educación'
        educacion_contadores = {'A': 0, 'PI': 0,'PC': 0,  'SI': 0, 'SC': 0, 'TI': 0, 'TC': 0, 'UI': 0, 'UC': 0}

        # Obtiene todos los registros de la base de datos
        viviendas = Vivienda.select()

        # Cuenta las ocurrencias de cada valor de educación
        for vivienda in viviendas:
            educacion = vivienda.educacion
            if educacion in educacion_contadores:
                educacion_contadores[educacion] += 1

        # Prepara los datos para el gráfico
        categorias = list(educacion_contadores.keys())
        conteos = list(educacion_contadores.values())

        # Se crea el gráfico de barras
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(categorias, conteos, color='skyblue')

        # Añado el título y las etiquetas
        ax.set_title('TRAYECTORIA EDUCATIVA RELEVADA', fontsize=14)
        ax.set_xlabel('Nivel de Educación', fontsize=12)
        ax.set_ylabel('Cantidad de Personas Relevadas', fontsize=12)

        # Se convierte el gráfico a formato que Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.marco_grafico)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky=N+S+E+W)

    def actualizar_vista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        viviendas = Vivienda.select().order_by(Vivienda.id)
        if viviendas:
            for vivienda in viviendas:
                self.tree.insert("", tk.END, text=vivienda.id, values=(vivienda.id, vivienda.nombre, vivienda.direccion, vivienda.educacion))
        else:
            print("No se encontraron registros para mostrar.")

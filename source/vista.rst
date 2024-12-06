Vista: Aplicación de Gestión de Relevamiento Barrial
===================================================

Este archivo contiene la interfaz gráfica de usuario (GUI) del sistema de relevamiento barrial, desarrollada con la biblioteca `tkinter`. La vista permite gestionar registros de viviendas, mostrando datos relevantes y proporcionando herramientas para interactuar con los datos.

Descripción de la clase `Aplicacion`
-----------------------------------

La clase `Aplicacion` se encarga de la creación de la interfaz gráfica y la interacción con el controlador y el modelo. A continuación, se detallan los componentes clave:

1. **Configuración inicial de la ventana**:
   - Se define el título de la ventana como "ORGANIZACIÓN DE LA COMUNIDAD - Gestor de gobierno popular".
   - Se configuran las filas y columnas de la ventana principal para una distribución flexible.

2. **Interfaz de usuario (UI)**:
   - Un `Label` en la parte superior muestra el título "RELEVAMIENTO BARRIAL".
   - El marco izquierdo contiene campos de entrada para el nombre, dirección y nivel educativo de los residentes.
   - Se incluyen botones para las acciones de **Alta**, **Baja**, **Modificar** y **Consultar lista**.
   - Un `Treeview` en la parte inferior de la interfaz muestra una lista de viviendas con sus respectivos detalles (nombre, dirección y educación).
   - Un área dedicada a la visualización de gráficos muestra un gráfico de barras con las estadísticas de la educación alcanzada en las viviendas.

3. **Funciones de la clase**:
   - **Alta**: Agrega un nuevo registro de vivienda a la base de datos tras validar que el nombre solo contiene letras.
   - **Baja**: Permite eliminar un registro seleccionado en el `Treeview` de la base de datos.
   - **Modificar**: Permite modificar los datos de un registro previamente existente.
   - **Consulta**: Actualiza la vista con los registros más recientes desde la base de datos y actualiza el gráfico.
   - **Actualizar gráfico**: Genera un gráfico de barras mostrando el conteo de viviendas según el nivel educativo de los residentes.
   - **Actualizar vista**: Refresca el `Treeview` con los registros actuales de la base de datos.

4. **Integración con el modelo y controlador**:
   - La clase `Aplicacion` interactúa con el modelo `Vivienda` y el controlador `Controlador` para realizar las operaciones de gestión de los registros (alta, baja, modificación y consulta).
   - Los gráficos se generan usando `matplotlib` y se integran en la interfaz utilizando `FigureCanvasTkAgg`.

Requisitos
----------
- Python 3.x
- Tkinter
- Matplotlib
- Peewee (para la gestión de base de datos)

Funcionalidad principal
-----------------------
La aplicación permite gestionar un relevamiento barrial, almacenando datos sobre la vivienda, el nivel educativo de los residentes y proporcionando una vista gráfica de la distribución educativa de las viviendas relevadas.

Referencias:
- Tkinter para la interfaz gráfica: https://docs.python.org/3/library/tkinter.html
- Matplotlib para gráficos: https://matplotlib.org/
- Peewee para base de datos: http://docs.peewee-orm.com/

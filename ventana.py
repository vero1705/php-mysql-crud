from doctest import master
from tkinter import Entry, Label, Frame, Misc, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END, Toplevel
from typing import Any
from conexion import Registro_datos

class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        frame1 = Frame(master, bg="#082338")
        frame1.place(x=0, y=0, width=300, height=1080)
        frame2 = Frame(master, bg="gray")
        frame2.place(x=300, y=0, width=225, height=1080)
        frame3 = Frame(master, bg="gray")
        frame3.place(x=526, y=0, width=1400, height=1020)

        self.buscar = StringVar()  # Define la variable de búsqueda
        self.btnnuevo = Button(frame1, text="Buscar", command=self.buscar_nombre, bg="white", fg="black", font=10)
        Entry(frame1, textvariable=self.buscar, font=('Arial', 12), width=24).place(x=40, y=10)  # Asigna self.buscar aquí
        
        self.btnnuevo.place(x=45, y=40, width=210, height=25)

        self.btnmodificar = Button(frame1, text="Modificar", command=self.agregar_datos, bg="white", fg="black", font=10)
        self.btnmodificar.place(x=45, y=75, width=210, height=25)

        self.legajo = StringVar()
        self.Apellido_y_nombre = StringVar()
        self.direccion = StringVar()
        self.localidad = StringVar()
        self.cp = StringVar()
        self.fecha_ingreso = StringVar()
        self.Antigüedad = StringVar()
        self.Fecha_Nacimiento = StringVar()
        self.Edad = StringVar()
        self.DNI = StringVar()
        self.nro = StringVar()
        self.cat = StringVar()
        self.oficina = StringVar()
        self.Nombre_Oficina = StringVar()
        self.Secretaria = StringVar()
        self.sindicato = StringVar()
        self.Sepelio = StringVar()
        self.Mutual = StringVar()
        self.solo_4 = StringVar()
        self.Seguro = StringVar()
        self.Coseguro = StringVar()
        self.PUESTO = StringVar()
        self.SEXO = StringVar()        
        self.ANTIGÜEDAD = StringVar()
        self.ESTUDIO = StringVar()
        self.buscar = StringVar()
        self.busca_producto = StringVar()
        self.Nro_De_Afiliado = StringVar()
        self.Fecha_De_Afiliacion = StringVar()
        self.basededatos = Registro_datos()
        
        # Configuración de los Labels y Entrys omitida por brevedad
        
        self.tabla = ttk.Treeview(frame3, height=40)
        self.tabla.pack(fill='both', expand=True)

        ladox = Scrollbar(frame3, orient=HORIZONTAL, command=self.tabla.xview)
        ladox.place(x=0, y=1000, relwidth=0.9, height=20)  
        
        ladoy = Scrollbar(frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.place(x=1375, y=0, width=20, relheight=0.9) 

        frame3.rowconfigure(0, weight=1)
        self.tabla['columns'] = (
            'legajo', 'apellido_y_nombre', 'direccion', 'localidad', 'cp', 'fecha_ingreso', 
            'antiguedad', 'fecha_de_nacimiento', 'edad', 'dni', 'nro', 'cat', 'oficina', 
            'nombre_oficina', 'secretaria', 'sindicato', 'sepelio', 'mutual', 'solo_4', 
            'coseguro', 'seguro', 'puesto', 'sexo', 'antigüedad', 'estudio', 
            'Nro_De_Afiliado', 'Fecha_De_Afiliacion'
        )
        
        self.mostrar_todo()
        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        # Configuración de columnas y encabezados omitida por brevedad

        estilo = ttk.Style(frame3)
        estilo.theme_use('default') # ('clam', 'alt', 'default', 'classic')
        estilo.configure("Treeview", font=(10), foreground='black', background='white')
        estilo.map('Treeview', background=[('selected', 'gray')], foreground=[('selected', 'black')])

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)

    def agregar_datos(self):
        self.tabla.focus()
        datos = (
            self.legajo.get(), self.Apellido_y_nombre.get(), self.direccion.get(), self.localidad.get(), self.cp.get(), 
            self.fecha_ingreso.get(), self.Antigüedad.get(), self.Fecha_Nacimiento.get(), self.Edad.get(), self.DNI.get(), 
            self.nro.get(), self.cat.get(), self.oficina.get(), self.Nombre_Oficina.get(), self.Secretaria.get(), 
            self.sindicato.get(), self.Sepelio.get(), self.Mutual.get(), self.solo_4.get(), self.Coseguro.get(), 
            self.Seguro.get(), self.PUESTO.get(), self.SEXO.get(), self.ANTIGÜEDAD.get(), self.ESTUDIO.get(), 
            self.Nro_De_Afiliado.get(), self.Fecha_De_Afiliacion.get()
        )
        
        self.tabla.insert('', 0, text=datos[0], values=datos)
        self.basededatos.inserta_datos(datos)
        
        for var in [
            self.legajo, self.Apellido_y_nombre, self.direccion, self.localidad, self.cp, self.fecha_ingreso, 
            self.Antigüedad, self.Fecha_Nacimiento, self.Edad, self.DNI, self.nro, self.cat, self.oficina, 
            self.Nombre_Oficina, self.Secretaria, self.sindicato, self.Sepelio, self.Mutual, self.solo_4, 
            self.Coseguro, self.Seguro, self.PUESTO, self.SEXO, self.ANTIGÜEDAD, self.ESTUDIO, 
            self.Nro_De_Afiliado, self.Fecha_De_Afiliacion
        ]:
            var.set("")

    def buscar_nombre(self):
        valor = self.buscar.get()  # Obtener el valor de búsqueda desde self.buscar
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla
        for row in self.basededatos.buscar_datos(valor):
            self.tabla.insert('', 0, text=row[0], values=row)

    def mostrar_todo(self):
        registros = self.tabla.get_children()
        for registro in registros:
            self.tabla.delete(registro)
        for row in self.basededatos.mostrar_legajo():
            self.tabla.insert('', 0, text=row[0], values=row)

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        
        data = self.tabla.item(current_item)
        values = data['values']
        self.legajo.set(values[0])
        self.Apellido_y_nombre.set(values[1])
        self.direccion.set(values[2])
        self.localidad.set(values[3])
        self.cp.set(values[4])
        self.fecha_ingreso.set(values[5])
        self.Antigüedad.set(values[6])
        self.Fecha_Nacimiento.set(values[7])
        self.Edad.set(values[8])
        self.DNI.set(values[9])
        self.nro.set(values[10])
        self.cat.set(values[11])
        self.oficina.set(values[12])
        self.Nombre_Oficina.set(values[13])
        self.Secretaria.set(values[14])
        self.sindicato.set(values[15])
        self.Sepelio.set(values[16])
        self.Mutual.set(values[17])
        self.solo_4.set(values[18])
        self.Coseguro.set(values[19])
        self.Seguro.set(values[20])
        self.PUESTO.set(values[21])
        self.SEXO.set(values[22])
        self.ANTIGÜEDAD.set(values[23])
        self.ESTUDIO.set(values[24])
        self.Nro_De_Afiliado.set(values[25])
        self.Fecha_De_Afiliacion.set(values[26])

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        
        data = self.tabla.item(current_item)
        values = data['values']
        self.legajo.set(values[0])
        self.Apellido_y_nombre.set(values[1])
        self.direccion.set(values[2])
        self.localidad.set(values[3])
        self.cp.set(values[4])
        self.fecha_ingreso.set(values[5])
        self.Antigüedad.set(values[6])
        self.Fecha_Nacimiento.set(values[7])
        self.Edad.set(values[8])
        self.DNI.set(values[9])
        self.nro.set(values[10])
        self.cat.set(values[11])
        self.oficina.set(values[12])
        self.Nombre_Oficina.set(values[13])
        self.Secretaria.set(values[14])
        self.sindicato.set(values[15])
        self.Sepelio.set(values[16])
        self.Mutual.set(values[17])
        self.solo_4.set(values[18])
        self.Coseguro.set(values[19])
        self.Seguro.set(values[20])
        self.PUESTO.set(values[21])
        self.SEXO.set(values[22])
        self.ANTIGÜEDAD.set(values[23])
        self.ESTUDIO.set(values[24])
        self.Nro_De_Afiliado.set(values[25])
        self.Fecha_De_Afiliacion.set(values[26])

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Registro")
    root.config(bg="#082338")
    root.geometry("1900x1080")
    app = Registro(root)
    root.mainloop()

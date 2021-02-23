from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import val
from temas.OpcionTemas import EleccionTema
from guardarModal import *
from eliminarModal import *
from modificarModal import *
from base_datos import *
from peewee import * 

class Producto:

    def __init__(self, window):
    
        # Ventana principal 
        self.root = window
        self.root.title("Tarea POO")

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val = StringVar(), StringVar()
        w_ancho = 20

        # Treeview y encabezados
        self.tree = ttk.Treeview(height = 10, columns = 3)
        self.tree["columns"]=("one","three")
        self.tree.grid(row = 7, column = 0, columnspan = 3)
        self.tree.heading("#0",text="ID",anchor=CENTER)
        self.tree.heading("one", text = 'Título', anchor = CENTER)
        self.tree.heading("three", text = 'Descripción', anchor = CENTER)

        # Botones de Alta, Eliminar y Modificar
        Button(self.root, text='Alta', command=lambda:self.pasarObjetoGuardar()).grid(row=11, column=0)
        Button(self.root, text='Eliminar', command=lambda:self.pasarObjetoEliminar()).grid(row=11, column=1)
        Button(self.root, text='Modificar', command=lambda:self.pasarObjetoModificar()).grid(row=11, column=2)

        # Temas del aplicativo
        self.temas_opciones = Frame(self.root, bg="red",borderwidth=2, relief=RAISED)
        self.temas_opciones.grid(row=12, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        self.tema_option = IntVar(value=0)
        Label(self.temas_opciones, borderwidth=4, relief=RAISED,text="Temas", bg="#222",fg="OrangeRed",).pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(self.temas_opciones,
            text=str(opcion), indicatoron=1, value=int(opcion[-1])-1, variable =self.tema_option,
            bg="#222",fg="OrangeRed", command=self.bg_fg_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

    def pasarObjetoGuardar(self,):
        guardar(self)

    def pasarObjetoEliminar(self,):
        eliminar(self)

    def pasarObjetoModificar(self,):
        modificar(self)
        
    def bg_fg_option(self):
        self.temas_opciones["bg"] = EleccionTema(self.tema_option.get())
        self.root["bg"] = EleccionTema(self.tema_option.get())

    # Función para mostrar los elementos de la BBDD
    def mostrar(self,):

        # Eliminación de elementos de la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Consulta a la tabla para la obtención de registros actualizados
        datos = []
        resultado = Articulos.select().order_by(Articulos.ID.desc())
        for elemento in resultado:
            lista_datos = []
            lista_datos.append(elemento.ID)
            lista_datos.append(elemento.titulo)
            lista_datos.append(elemento.descripcion)
            datos.append(lista_datos)    

        # Mostrar consulta anterior en la aplicacion
        for fila in datos:
            self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2]))

if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    application.mostrar()
    window.mainloop()

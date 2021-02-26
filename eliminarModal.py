from tkinter import *
from eliminar import *
from base_datos import *
from tkinter import messagebox
from observers import observadorEliminar


def show(variables, popupGuardar):
    popupGuardar.destroy()


def elimina(variables, popupEliminar, elobjeto):
    try: 
        popupEliminar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())

        lista_old = []
        for x in Articulos.select().where(Articulos.ID == lista[0]):
            lista_old.append(x.ID)
            lista_old.append(x.titulo)
            lista_old.append(x.descripcion)

        borrar = Articulos.get(Articulos.ID == lista[0])
        borrar.delete_instance()

        # Patron observador
        observer = observadorEliminar(borrar, lista_old)
    
        elobjeto.mostrar()
        messagebox.showinfo(message="El ID %s se elimino satisfactoriamente." % borrar, title="Eliminar registro")
    except:
        # Patron observador
        observer = observadorEliminar(None, None)
        messagebox.showerror(message="El ID no existe en la BBDD.", title="Eliminar registro")


def eliminar(objeto):
    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)
    Button(popupEliminar, text='Eliminar', command=(lambda: elimina(vars_eliminar, popupEliminar, objeto))).pack()
    Button(popupEliminar, text='Cancelar', command=(lambda: show(vars_eliminar, popupEliminar))).pack()
    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()
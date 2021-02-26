from tkinter import *
from modificar import *
from base_datos import *
from tkinter import messagebox
from peewee import DoesNotExist
from observers import observadorModificar


def show(variables, popupModificar):
    popupModificar.destroy()


def modifica(variables, popupModificar, elobjeto):
    popupModificar.destroy()
    
    lista = []
    for variable in variables:
        lista.append(variable.get())

    lista_old = []
    for x in Articulos.select().where(Articulos.ID == lista[0]):
        lista_old.append(x.ID)
        lista_old.append(x.titulo)
        lista_old.append(x.descripcion)

    # Patron observador
    observer = observadorModificar(lista, lista_old)

    try:
        verificar_id = Articulos.get(Articulos.ID == lista[0])
        actualizar = Articulos.update(titulo = lista[1], descripcion = lista[2]).where(Articulos.ID == lista[0])
        actualizar.execute()
        elobjeto.mostrar()
        messagebox.showinfo(title="Modificacion de datos", message="Los datos para el ID %s se modificaron correctamente." % lista[0])
    except DoesNotExist:
        messagebox.showerror(title="Modificacion de datos", message="No se encontro el ID %s en la BBDD.\n Pruebe nuevamente con otro ID." % lista[0])

def modificar(objeto):
    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    Button(popupModificar, text='Modificar', command=(lambda: modifica(vars_modificar, popupModificar, objeto))).pack()
    Button(popupModificar, text='Cancelar', command=(lambda: show(vars_modificar, popupModificar))).pack()    

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()
from tkinter import *
from guardar import *
import base_datos
from base_datos import *
from tkinter import messagebox
from observers import observadorAlta


def show(variables, popupGuardar):
    popupGuardar.destroy()


def guarda(variables, popupGuardar, elobjeto):
    
    popupGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    # Patron observador
    observer = observadorAlta(lista)
    
    # Insertar registro en BBDD
    res = Articulos.insert({
    Articulos.titulo: lista[0],
    Articulos.descripcion: lista[1]
    }).execute()

    elobjeto.mostrar()
    messagebox.showinfo(title="Alta de registro", message="El registro se dio de alta satisfactoriamente.")

def guardar(objeto):
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    
    Button(popupGuardar, text='Guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()
    Button(popupGuardar, text='Cancelar', command=(lambda: show(vars_guardar, popupGuardar))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
from base_datos import registrosAlta
from base_datos import registrosModif
from base_datos import registrosElim


class observadoresApp:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def notificar(self):
        for observador in self.observadores:
            self.update_log()
            self.update_query()
        self.observadores.clear()


class observadorAlta(observadoresApp):
    def __init__(self, obj):
        self.lista_alta = obj
        self.agregar(self)
        self.notificar()

    def update_log(self):
        print("--" * 25)
        print("El Observador de 'ALTAS' ha detectado un nuevo registro en la BBDD. Se detalla a continuación:")
        print("Título:", self.lista_alta[0])
        print("Descripción:", self.lista_alta[1])
        print("--" * 25)
    
    def update_query(self):
        record_update = registrosAlta.insert({
        registrosAlta.titulo: self.lista_alta[0],
        registrosAlta.descripcion: self.lista_alta[1]
        }).execute()


class observadorModificar(observadoresApp):
    def __init__(self, objnew, objold):
        self.lista_modif = objnew
        self.lista_old = objold
        self.agregar(self)
        self.notificar()
    
    def update_log(self):
        if len(self.lista_old) == 3:          
            print("--" * 25)
            print("El Observador de 'MODIFICACIONES' ha detectado la modificación de un registro en la BBDD. Se detalla a continuación:")
            print("ID:", self.lista_modif[0])
            print("Nuevo Título:", self.lista_modif[1])
            print("Nueva Descripción:", self.lista_modif[2])
            print("--" * 25)
        else:
            pass

    def update_query(self):
        try: 
            record_update = registrosModif.insert({
            registrosModif.ID_record: self.lista_modif[0],    
            registrosModif.titulo_old: self.lista_old[1],
            registrosModif.titulo_new: self.lista_modif[1],
            registrosModif.descripcion_old: self.lista_old[2],
            registrosModif.descripcion_new: self.lista_modif[2]
            }).execute()
        except IndexError:
            print("--" * 25)
            print("El Observador de 'MODIFICACIONES' ha detectado el intento de una modificación en la BBDD.")
            print("No hubo modificaciones en la BBDD - El ID no se encontró.")
            print("--" * 25)

class observadorEliminar(observadoresApp):
    def __init__(self, obj, objold):
        self.lista_elim = obj
        self.lista_old = objold
        self.agregar(self)
        self.notificar()
    
    def update_log(self):
        if self.lista_elim == None:
            print("--" * 25)
            print("El Observador de 'ELIMINAR' ha detectado el intento de la eliminación de un registro en la BBDD.")
            print("La operacion no pudo ser completada. El ID no se encontro en la BBDD.")
            print("--" * 25)
        else:
            print("--" * 25)
            print("El Observador de 'ELIMINAR' ha detectado la eliminación de un registro en la BBDD. Se detalla a continuación:")
            print("ID:", self.lista_elim)
            print("--" * 25)

    def update_query(self):
        try:
            record_update = registrosElim.insert({
            registrosElim.ID_record: self.lista_old[0],    
            registrosElim.titulo: self.lista_old[1],
            registrosElim.descripcion: self.lista_old[2]
            }).execute()
        except TypeError:
            pass
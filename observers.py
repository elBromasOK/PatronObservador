class observadoresApp:
    observadores = []
    
    def agregar(self, obj):
        self.observadores.append(obj)

    def notificar(self):
        for observador in self.observadores:
            self.update()

class observadorAlta(observadoresApp):
    def __init__(self, obj):
        self.alta_titulo = None
        self.alta_descripcion = None
        self.lista_alta = obj
        self.agregar(self)
        self.notificar()
    
    def update(self):
        print("El Observador de 'ALTAS' ha detectado un nuevo registro en la BBDD. Se detalla a continuación:")
        print("Título:", self.lista_alta[0])
        print("Descripción:", self.lista_alta[1])
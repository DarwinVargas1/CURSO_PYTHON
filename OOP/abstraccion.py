class auto:
    def __init__(self):
        self._estado="apagado"
    
    def encender(self):
        self._estado="encedido"
        print("el auto está encendido")

    def conducir(self):
        if self._estado=="apagado":
            self.encender()
        print("conduciendo el auto")

mi_auto=auto()
mi_auto.conducir()
#aca usamos abstraccion pq le estamos pasando solo el metodo conducir ocultando el resto, no sabe que esta pasando detras como si esta apagado o encendido esas con validaciones, lo importante es que si llamamos el metodo conducir este empieza a conducir sin importar que se tiene que prender, que cosas interna tiene que ejecutar para poder conducir
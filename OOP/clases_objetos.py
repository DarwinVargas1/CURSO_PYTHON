"""class Celular():
    marca="Samsung" #atributos de clases
    modelo="S21"
    color="negro"

celular1=Celular()
print(celular1)

celular2=Celular()

print(Celular.marca)"""

##print(marca)#error ya que no existe marca como variable global, esta solo existe en los objetos de la clase celular

class Celular:
    def __init__(self, marca, modelo, color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
    
    def llamar(self):
        print(f'Estas haciendo un llamado desde tu {self.modelo}')
    
    def cortar(self):
        print(f'cortaste la llamada desde tu {self.modelo}')
        
celular1=Celular("Samsung","S21","negro")
celular2=Celular("Apple","iPhone 13","blanco") ##atributos de instancias
##print(celular1.marca)

celular1.cortar()
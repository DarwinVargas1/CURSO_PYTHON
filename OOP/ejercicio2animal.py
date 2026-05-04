class animal: 
    def comer(self):
        print("comer")

class mamifero:
    def amamantar(self):
        print("amamantar")
class ave(animal):
    def volar(self):
        print("volar")

class Murcielago(mamifero, ave):
   pass
        
#Ave=ave()
#Ave.comer()#SOLO PUEDE COMER YA QUE HEREDA ATRIBUTOS DE ANIMAL 
#Ave.amamantar()#produce error ya que no tiene el atributo o metodo amamantar
murcielago=Murcielago()
murcielago.comer()
#murcielago.amamantar()
#murcielago.volar()

print(Murcielago.mro())
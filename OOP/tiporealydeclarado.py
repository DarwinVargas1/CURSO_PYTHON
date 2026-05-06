class Animal:
    def sonido(self):
        pass #metodo vacio, no hace nada, se implementa en las clases hijas



class Gato(Animal):
    def sonido(self):
        return "miau"
    

class Perro(Animal):
    def sonido(self):
        return "guau"

gato=Gato()#el tipo real es animal ya que es el origen de todo la que hereda, mientras que el tipo declarado es gato, ya que es de donde se origina la variable
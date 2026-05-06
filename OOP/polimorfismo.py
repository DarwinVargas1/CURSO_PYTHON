class Animal:
    def sonido(self):
        pass #metodo vacio, no hace nada, se implementa en las clases hijas



class Gato(Animal):
    def sonido(self):
        return "miau"
    

class Perro(Animal):
    def sonido(self):
        return "guau"


def hacer_sonido(animal):
    print(animal.sonido())


#ejemplo sencillo de polimorfismo


"""print(perro.sonido())#la razon es que estoy enviando un mismo mensaje solo cambio el objeto

hacer_sonido(perro)#otra forma de hacer polimorfismmo misma funcion, solo cambia el argumento

print(gato.sonido()) #ejecuto el mismo metodo pero objeto diferente"""

animales= [Gato(), Perro()]
for animal in animales:
    print(animal.sonido())
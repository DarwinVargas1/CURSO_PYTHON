class persona:
    def __init__(self, nombre,edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("hola estoy hablando")

class artista:
    def __init__(self, habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        return f"la habilidad del artista es: {self.habilidad}"


class empleadoArtista(persona,artista):##ejemplo de herencia multiple, ya que la clase empleadoArtista hereda de las clases persona y artista, por lo que tiene acceso a los atributos y metodos de ambas clases.
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        persona.__init__(self, nombre, edad, nacionalidad)
        artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrar_habilidad(self):
        print("no tengo jaja")

    def presentarse(self):
        return f'{super().mostrar_habilidad()}'

roberto=empleadoArtista("roberto", 30, "mexicano", "cantar", 10000, "google")

##print(roberto.nacionalidad)#la salida es mexicano, ya que la clase empleado es la hija de persona, por lo que hereda sus atributos y metodos. 
##roberto.hablar()

##instancia=isinstance(roberto, persona)##la funcion isinstance nos permite saber si un objeto es una instancia de una clase o de una clase padre. En este caso, roberto es una instancia de la clase empleado, por lo que la salida es True. ademas si le ponemos que es una instancia de la clase persona, tambien da true porque la clase persona es la clase padre de empleado, por lo que roberto tambien es una instancia de la clase persona.

herencia=issubclass(empleadoArtista, persona)##la funcion issubclass nos permite saber si una clase es una subclase de otra clase. en este caso es true porque empleadoArtista es una subclase de persona, ya que hereda de persona. ademas si le ponemos que es una subclase de artista, tambien da true porque empleadoArtista tambien hereda de artista.



print(herencia)

##roberto.mostrar_habilidad()

##print(roberto.presentarse())

#print(instancia)
class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def detalles_personas(self):
        print (f"el nombre es: {self.nombre} y la edad es: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado


    def mostrar_grado(self):
        print (f"el grado es{self.grado}")


estudiante=Estudiante("Juan", 18, "11")
estudiante.detalles_personas()
estudiante.mostrar_grado()

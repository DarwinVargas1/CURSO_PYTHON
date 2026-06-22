from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad= actividad
    
    @abstractmethod
    def hacer_actividad(self):
        pass


    def presentarse(self):
        print(f"hola como estan mi nombre es {self.nombre}, tengo {self.edad} años")



class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente trabajo en el area de: {self.actividad}")


dalto=Estudiante("Dalto", 21, "Masculino", "Programación")
Darwin=Trabajador("Darwin", 21, "Masculino", "Programación")

dalto.presentarse()
dalto.hacer_actividad()
Darwin.presentarse()
Darwin.hacer_actividad()
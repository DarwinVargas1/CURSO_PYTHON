class persona:
    def __init__(self, nombre,edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("hola estoy hablando")
class estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad, carrera):
        __init__(nombre, edad, nacionalidad)
        self.carrera=carrera

class empleado(persona):
    def __init__(self, nombre,edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario
    
    def hablar(self):
        print("hola estoy hablando como empleado")##reescribe el metodo hablar de la clase padre, por lo que al llamar al metodo hablar de un objeto de la clase empleado, se ejecutara este metodo en lugar del metodo hablar de la clase persona.

roberto=empleado("roberto", 30, "mexicano", "programador", 10000)

print(roberto.nacionalidad)#la salida es mexicano, ya que la clase empleado es la hija de persona, por lo que hereda sus atributos y metodos. 
roberto.hablar()
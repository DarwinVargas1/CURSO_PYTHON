class Persona:
    def __init__(self, nombre,edad):
        self.__nombre=nombre
        self._edad=edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter#permite modificar el atributo nombre, sino usaramos el setter no seria posible y generaria error
    def nombre(self, new_nombre):
        self.__nombre= new_nombre

   
    
dalto=Persona("juan",18)

nombre=dalto.nombre
print(nombre)

dalto.nombre="pepe"
nombre=dalto.nombre
print(nombre)

#si no tiene un deleter  no es posible eliminarlo

del dalto.nombre#    elimina los nombres por lo cual provoca un error diciendo que persona no tiene el atributo nombre


nombre=dalto.nombre
print(nombre)
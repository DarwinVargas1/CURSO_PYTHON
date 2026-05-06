class persona():
    def __init__(self, nombre, edad):
        self.__nombre=nombre
        self.__edad=edad


    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre=new_nombre
    
dalto=persona("Juan", 19)

nombre=dalto.get_nombre()#funcion que accede a un valor privado
print(nombre)


dalto.set_nombre("pepito")

nombre=dalto.get_nombre()
print(nombre)
#print(dalto._nombre) no es correcto, el guion bajo lo indica



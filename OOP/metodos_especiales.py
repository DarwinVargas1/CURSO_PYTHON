class Persona():
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
    

    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})" #permite como mostrar como cadena de texto el objeto
    
    def __repr__(self):#actua como la representación de
        return f"Persona('{self.nombre}', {self.edad}) "


    def __add__(self, otro):
        nuevo_valor=self.edad + otro.edad        
        return Persona(self.nombre + otro.nombre, nuevo_valor)

darwin=Persona("Juan", 19)
lucas=Persona("Lucas", 20)

nueva_persona=darwin+lucas
print(nueva_persona.nombre)
resultado=darwin+lucas
print(resultado)




"""darwin=Persona("pedro",19)
repre= repr(darwin)#obtengo la representación del objeto
resultado=eval(repre)#ya es e l objeto
print(resultado.edad)"""











#print(darwin)##si usamos el print sin el __str__ solo daria algo menos intuitivo pero mas preciso como la ubicacion del objeto en memoria 


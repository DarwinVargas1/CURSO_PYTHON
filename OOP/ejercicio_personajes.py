class Personaje:
    def __init__(self, nombre, velocidad, fuerza):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad=velocidad
        
    

    def __repr__(self):#devuelve una cadena de texto que sea una representacion oficial e inequivoca del objeto
        return f"{self.nombre} (fuerza:{self.fuerza}, velocidad {self.velocidad})"


    def __add__(self, otro_pj):
        nuevo_nombre=self.nombre + "-" + otro_pj.nombre
        nueva_fuerza=round(((self.fuerza  + otro_pj.fuerza)/2)**1.2)
        nueva_velocidad=round(((self.velocidad + otro_pj.velocidad)/2)**1.2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku=Personaje("Goku", 100, 100)
vegeta=Personaje("Vegeta", 99,99)
jiren=Personaje("Jiren", 130, 140)

gogeta= goku + vegeta
jireta= gogeta+jiren
print(goku)
print(vegeta)
print(gogeta)
print(jireta)
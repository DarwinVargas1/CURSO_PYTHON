#Ejemplo ultimo principio lo que no se debe hacer 
"""
class MySQLDB:
    def guardar (self, datos):
        print("Guardando en MySQL")
    
class GestorProyectos:
    def __init__(self):
        #error la conexion esta siendo creada aqui adentro.
        #si mañana cambiamos la base de datos, como por ejemplo usar mongo, hay que modificar esta clase
        self.db=MySQLDB()

    def ejecutar(self, proyecto):
        self.db.guardar(proyecto)"""

#la solucion correcta es crear una "abstracion" (interfaz) para que el gestor no sepa (ni le importe) que base de datos se usa

from abc import ABC, abstractmethod

#1. creamos la abstraccion (El enchufe)

class ConexionBD(ABC):
    @abstractmethod
    def guardar(self,datos):
        pass

#2. Detalles de bajo nivel (Las lamparas)

class MySQLDB(ConexionBD):
    def guardar(self, datos):
        print(f"Guardando {datos}en mySQL")

class MongoDBAtlas(ConexionBD):
    def guardar(self, datos):
        print(f"guardando {datos} en mongo DB atlas")

class GestorProyectos():
    def __init__(self, db: ConexionBD):
        #ahora aqui no creamos la base de datos, la recibimos
        #no sabemos que base de datos es, solo se sabe que tiene el metodo guardar()
        self.db=db

    def ejecutar(self, datos):
        self.db.guardar(datos)

#uso del codigo
db_mongo=MongoDBAtlas()
gestor=GestorProyectos(db_mongo)
gestor.ejecutar("proyecto IA")
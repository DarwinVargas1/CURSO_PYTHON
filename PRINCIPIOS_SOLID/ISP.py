from abc import ABC, abstractmethod
""" #esto actua como nuestra interfaz
    class Trabajador(ABC):

        @abstractmethod
        def comer(self):
            pass
        @abstractmethod
        def dormir(-self):
            pass    
        @abstractmethod
        def trabajar(self):
            pass   

    #la clase que hereda esta obligada a implementar esos metodos    
    class humano(Trabajador):
        def comer(self):
            return "el humano esta comiendo"
        
        def dormir(self):
            return "el humano esta durmiendo"
        
        def trabajar(self):
            return "el humano esta trabajando"
        
    class Robot(Trabajador):
        def comer(self):
            pass
        
        def dormir(self):
            pass
        
        def trabajar(self):
            return "el robot esta trabajando"
        
    robot=Robot()
    robot.trabajar()"""
    #La forma de arriba no es la correcta ya que implementamos metodos innecesarios por ejemplo en la clase robot, lo mejor es tener muchas interfaces especificas pero que no tenga metodos innecesarios


"""esta es la manera correcta estamos creando interfaces especificas que nos evitan usar metodos innecesarios, podemos tener un robot que no necesite comer y dormir por lo cual creamos una interfaz aparte que sea solo de trabajar y que la clase robot herede de ella, evitando tener los metodos dormir y comer sin hacer nada"""
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    

class Comedor(ABC):
    @abstractmethod
    def comer():
        return "comiendo"
    
class Durmientes(ABC):
    @abstractmethod
    def dormir():
        pass

class Humano(Trabajador, Durmientes, Comedor):
    def comer(self):
        print("el humano está comiendo")
    
    def dormir(self):
        print("el humano esta durmiendo")

    def trabajar(self):
        print("el humano está trabajando")

class robot (Trabajador):
    def trabajar(self):
        print("el robot está trabajando") 

robot=robot()
robot.trabajar()


Persona=Humano()
Persona.comer()
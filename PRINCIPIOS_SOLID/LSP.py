# class Ave: #clase base
#     def volar(self):
#         return "estoy volando"

# class Pinguino(Ave):
#     def volar(self):
#         return "no puedo volar"
    
# def hacer_volar(ave=Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:##aca definimos todas las caracteristicas en comun que va tener un ave, excepto las que tenemos en sub division en este caso las que vuelan y no vuelan
    pass

class AveVoladora(Ave):
    def volar(Self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass


class Ave:
    def comer(self):
        return "estoy comiendo"
    
class AveVoladora(Ave):
    def volar(self):
        return "estoy volando"

class AveNoVoladora(Ave):
    def caminar(self):
        return "estoy caminando"
    
#funciones especificas 

def realizar_vuelo(ave: AveVoladora):
    #esta función solo acepta aves que si vuelan
    print(ave.volar())

#uso 
pajaro=AveVoladora()
Pinguino= AveNoVoladora()

realizar_vuelo(pajaro)#funciona bien
realizar_vuelo(Pinguino)#error pinguino no tiene el metodo o atributo volar
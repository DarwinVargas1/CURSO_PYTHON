#la idea clave es ocultar los datos internos (atributos)
#permitir el acceso a los datos mediante metodos controlados 

class cuentaBancaria():
    def __init__(self, titular, saldo_inicial):
        #atributos privados
        self.titular=titular
        self.__saldo_inicial=saldo_inicial
# Método público para consultar el saldo

    def consultar_saldo(self):
        return self.__saldo_inicial

# Método público para depositar dinero
    def depositar(self, monto):
        if monto>0:
            self.__saldo_inicial+=monto
            print(f"Deposito realiza con exito, Nuevo Saldo: {self.__saldo_inicial}")
        else:
            print("Error, el monto debe ser mayor a 0")    
 # Método público para retirar dinero
    def retirar(self, monto):
        if monto>self.__saldo_inicial:
            print("fondos insuficientes")

        elif monto<=0:
            print("el monto debe ser mayor a 0")
        else:
            self.__saldo_inicial-=monto
            print(f"retiro exitoso. nuevo saldo {self.__saldo_inicial}")

cuenta=cuentaBancaria("Darwin", 100)
cuenta.depositar(500)
print(cuenta.consultar_saldo())
"""X=int(input("ingrese un numero: "))
Y=int(input("ingrese otro numero: "))

try:
    dividir= X/Y
    print(dividir)
except ZeroDivisionError:
    print("No se puede dividir por cero")

try:
    A=int(input("ingrese un numero: "))
    B=int(input("ingrese otro numero: "))
    print("La suma es:", A+B)
except ValueError:
    print("No se pueden ingresar letras, solo numeros")"""

x=1

try:
    print(x)
except NameError:
    print("La variable x no esta definida")
finally:
    print("Este bloque se ejecuta siempre, haya o no un error")
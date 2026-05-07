# def mi_decorador(funcion_a_decorar):
#     def envoltura():
#         print("1. Estoy a punto de ejecutar la función...")
#         funcion_a_decorar()
#         print("2. La función ya se ejecutó.")
#     return envoltura

# def saludo():
#     print("   ¡Hola, mundo! 👋")

 # Aquí "envolvemos" la función manualmente
#saludo_decorado = mi_decorador(saludo)
#saludo_decorado()



def mi_decorador(funcion_a_decorar):
     def envoltura():
         print("vamos a sumar")
         funcion_a_decorar()
         print("la suma fue realizada")
     return envoltura

# def sumar():
#      x=7+8
#      print(x)

# suma_decorada=mi_decorador(sumar) 
# suma_decorada()



#es la misma forma de arriba solo que es mas sencilla, el decorador se encarga de envolver la funcion sin necesidad de crear una nueva variable para ello, es decir, se hace de forma automatica
@mi_decorador
def sumar():
     x=7+8
     print(x)

sumar()
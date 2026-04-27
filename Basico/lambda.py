#lambda es una funcion pequeña y anonima, puede tenerr muchos argumentos pero solo una expresion, se utiliza para funciones simples y rapidas

#sintaxis: lambda argumentos: expresion

x= lambda a,b: a + b
print(x(5,10))


def mifuncion(n):
    return lambda a: a * n

duplicador=mifuncion(2)
triplicador=mifuncion(3)
quintuplicador=mifuncion(5)


print(duplicador(5)) #1

print(triplicador(5)) #15

print(quintuplicador(5)) #25
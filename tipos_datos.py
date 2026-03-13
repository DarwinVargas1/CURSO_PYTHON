String="Este es una varibable tipo string"
String2='Este es otra variable tipo string'
String3='''Este es una variable tipo string con comillas triples'''

a=10
b=11
c=12.1
d=5+2j
print(a+b+c)
print(d)

#listas 
Lista=[1,2,3,4,5]

#tupla- inmutable
tupla=("hola mundo", 1,2,a)

#diccionario
diccionario= {
    "nombre":"juan",
    "edad":30
    }

#conjuntos (sets)-desordenado y no repite elemento
conjunto = {1,1,1,2,2,3,3} #output esperado {1,2,3}
BoleeanoV=True
BoleeanoF=False

print(diccionario["nombre"])
print(Lista)
print(tupla)
print(conjunto)
print(BoleeanoV, BoleeanoF)

print(type(String))
print(type(a))
print(type(Lista))
print(type(diccionario))
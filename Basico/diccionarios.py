# coleccion de pares clave-valor (a partir de python 3.7 es ordenado)
#[ ]
auto={
    "marca":"toyota",
    "modelo":"hilux",
    "año":2020
}

print(auto)

[ ]
print(auto["marca"])
print(auto.get("año"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")

auto["año"]= 2021
print(auto)

auto["modelo"]="Ferrari"
print(auto)

auto["color"]="rojo"
print(auto)

auto.update({"año":2022, "puertas": 4})
print(auto)

#auto.pop("puertas")
#print(auto)

#auto.popitem()
#print(auto)

#auto.clear()
#print(auto)

for k in auto: #keys
    print(k)
    print("----------------")
for v in auto.values():
    print(v)

print("------------------")
for k,v in auto.items(): #keys and values
    print(k,v)

#diccionarios anidados 

familia={
    "hijo1":{
        "nombre":"jesus",
        "edad": 16,
    },
    "hijo2":{
        "nombre":"pedro",
        "edad":34
    },
    "hijo3":{
        "nombre":"luisa",
        "edad": 45,
    }
}

print(familia[ "hijo1"][ "nombre"], familia[ "hijo1"][ "edad"])
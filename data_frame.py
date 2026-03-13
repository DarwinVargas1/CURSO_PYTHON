import pandas as pd

#crear un dataframe a partir de un diccionario

datos= {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df= pd.DataFrame(datos)

print(df)
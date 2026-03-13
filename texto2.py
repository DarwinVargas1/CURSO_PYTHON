#ind    01234         21    
texto= "Este es un texto"

print(texto[5:-2])

curso= "este curso es de javascript, y siempre será de javascript"
print(curso.replace("javascript","python"))

textoDividido = texto.split()
print(textoDividido)

#normalización 

texto2= "Este texto tiene MAYUSCULAS y minisculas y necesito encontrar ciertas palabras"
print("mayusculas".lower() in texto2.lower())
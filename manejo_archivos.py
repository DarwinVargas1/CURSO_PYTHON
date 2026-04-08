
# open (nombre, modo)

# R (read) Lectura
# # W (write) Escritura
# X (crea archivo nuevo)  
# A (append) Agregar al final del archivo

try:
    f=open("archivo.txt", "r")
    print(f.readline())
    f.close()

    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "w") #crea el archivo si no existe
    print("No se ha encontrado el archivo")

try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
           f.write("\n")
           f.write("Hola mundo")
    with open("archivo.txt", "r", encoding="utf-8") as f:
            print(f.read())
except FileNotFoundError:
        print("No se ha encontrado el archivo")
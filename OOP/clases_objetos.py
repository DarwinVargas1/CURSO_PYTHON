class Celular():
    marca="Samsung"
    modelo="S21"
    color="negro"

celular1=Celular()
print(celular1)

celular2=Celular()

print(Celular.marca)

##print(marca)#error ya que no existe marca como variable global, esta solo existe en los objetos de la clase celular
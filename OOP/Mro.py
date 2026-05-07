class a: #por ultimo la clase padre, 
    pass


class f(): #es la ultima clase que definimos, no hereda de nadie, entonces es la ultima en el orden de busqueda
    def hablar(self):
        print("hola, soy la clase f")

class b(a):
   pass


class c(f):#sigue c por que es la segunda clase que hereda de a, si c no tuviera el metodo hablar entonces seguiria a b, en el caso de heredar de f, como f es la ultima clase que definimos y no hereda, entonces seguiria a 
    pass

class D(b,c):#sigue a b porque es la primera clase que definimos que hereda de a, si b no tuviera el metodo hablar entonces seguiria a c
    pass
d = D()

d.hablar()      # bound method   → Python busca 'hablar' en el MRO de D
                #                  lo encuentra en f, pasa d como self automáticamente

f.hablar(d)     # unbound call   → vas directo a f.hablar
                #                  pasas d como self tú mismo, saltando el MRO

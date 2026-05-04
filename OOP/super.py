class a:
    def hablar(self):
        super().hablar()  
        print("soy a")

class f():
    def hablar(self):
        print("soy f")

class b(a):
    def hablar(self):
        super().hablar()  
        print("soy b")

class c(f):
    def hablar(self):
        super().hablar()  # siguiente de c en el MRO de D es → f
        print("soy c")

class D(b, c):
    def hablar(self):
        super().hablar()  # siguiente de D en el MRO es → b
        print("soy D")

d = D()
d.hablar()
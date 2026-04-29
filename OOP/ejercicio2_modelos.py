class modeloIA:
    def __init__(self,nombre,algoritmo, precision):
        self.nombre=nombre
        self.algoritmo=algoritmo
        self.precision=precision

    def predecir(self):
        print(f"el modelo {self.nombre} esta realizando una prediccion sobre los datos")

    def mostrar_info(self):
        print(f"""DATOS DEL MODELO: \n\n
              
                Nombre: {self.nombre}\n
                algoritmo: {self.algoritmo}\n
                precision: {self.precision}\n
              """)
    
    def actualizar_precision(self, nueva_precision):
        self.precision= nueva_precision
        print(f"la nueva precision del modelo {self.nombre} es {self.precision}")
        
nombre_modelo=input("Ingrese el nombre del modelo:")
algoritmo=input("ingrese el algoritmo a usar:")
precision=input("ingrese la precision del modelo:")
modelo1=modeloIA(nombre_modelo,algoritmo, precision)
modelo1.predecir()
modelo1.mostrar_info()
nueva=input("Ingrese la nueva precision tras el entrenamiento")

modelo1.actualizar_precision(nueva)

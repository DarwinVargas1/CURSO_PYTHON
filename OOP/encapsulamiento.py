class miclase:
    def __init__(self):
        #self._atributo_privado= "direccion"#el guion bajo es una convención para indicar que el atributo es privado, aunque en realidad no lo es, ya que se puede acceder a él desde fuera de la clase, es como una recomendación al verlo para saber que no se debe acceder a él directamente, sino a través de un método getter o setter.
        self.__atributo_privado= "direccion"##el doble guion bajo es una convención para indicar que el atributo es muy muy privado, no se puede acceder a el desde fuera de la clase

    #def _metodo_privado(self):##asi si se puede acceder. sirve mas como advertencia de que no sebe de acceder desde afuera

    def __metodo_privado(self):#con este directamente no podemos acceder
        print("este es un metodo privado, no se puede acceder a el desde fuera de la clase")
objeto=miclase()
##print(objeto.__atributo_privado)
objeto.__metodo_privado()

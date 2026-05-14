class notificador():
    def __init__(self, usuario, mensaje):
        self.usuario=usuario
        self.mensaje=mensaje
    
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(notificador):
    def notificar(self):
        print(f"enviando mensaje email a {self.usuario.email}")


class NotificadorSMS(notificador):
    def notificar(self):
        print(f"enviando mensaje SMS al {self.usuario.sms}")


#como podemos ver podemos crear muchos metodos mas si queremos notificar por diferentes medios whatsapp, email, sms, ig, etc. Lo importante es que es posible crear otras clases que son capaces de solucionar esto y no modifiquen el codigo fuente o principal. 
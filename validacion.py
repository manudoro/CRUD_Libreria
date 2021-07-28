"""Este módulo utiliza el paquete re para validar los datos de los 
registros cuyo ingreso a la base de datos es solicitado. """
import re

class Validacion:
    """Esta clase contiene un método que recibe de los metodos 
    restantes un patrón especifico para cotejar con cada dato."""
   # No supe qué contenido darle al método constructor en este caso

    def validacion(self,patron,cad): 
        """Este método recibe un patrón y un dato y retorna True en 
        caso de que estos coincidan y False en caso contrario."""      
        try:
            re.match(patron, cad)
            if re.match(patron, cad):
                return True
            else:
                return False
        except:
            return False
   
    def validar_titulo(self,cad):
        """Este método define el patrón válido para el título
        de cada obra y llama al método validacion"""
        patron = r"^[A-Za-záéíóúÁÉÍÓÚñÑ0-9.,:&%$#@¿?¡!*-+() ]+$"
        return self.validacion(patron,cad)
    
    def validar_nautor(self,cad):
        """Este método define el patrón válido para el nombre
        del autor de cada obra y llama al método validacion"""
        patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ. ]*$"
        return self.validacion(patron,cad)

    def validar_aautor(self,cad):
        """Este método define el patrón válido para el apellido
        del autor de cada obra y llama al método validacion"""        
        patron = r"^[A-Za-záéíóúÁÉÍÓÚÑñ ]+$"
        return self.validacion(patron,cad)

    def validar_precio(self,cad):
        """Este método define el patrón válido para el precio
        de cada obra y llama al método validacion"""        
        patron = r"\d+.?\d+$"
        return self.validacion(patron,cad)



# Definición de la clase Telefono
class Telefono():    
    #Función init, cada vez que creemos el objeto se ejecutará
    #self es una referencia a la instancia de la clase
    def __init__(self, marca, modelo, color):
        self.marca = marca #es como si digo Telefono.marca y lo iguala a la marca que le pasamos
        self.modelo = modelo
        self.color = color
        
    #Definición de un método de la clase Telefono
    def encender(self):
        print(f"Encendiendo el teléfono {self.marca} {self.modelo}...")
          
    
    
#Instancio un objeto de la clase Telefono
telefono1 = Telefono("Samsung", "Galaxy S21","negro") #telefono1 es una instancia de la clase Telefono (es un objeto)
print(telefono1.marca) #Accedo al atributo marca del objeto telefono1

telefono1.encender() #Llamo al método encender del objeto telefono1
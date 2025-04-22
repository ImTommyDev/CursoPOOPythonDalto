# Definición de la clase Telefono
class Telefono():    
    #Función init, cada vez que creemos el objeto se ejecutará
    #self es una referencia a la instancia de la clase
    def __init__(self, marca, modelo, color):
        self.marca = marca #es como si digo Telefono.marca y lo iguala a la marca que le pasamos
        self.modelo = modelo
        self.color = color
          
    
    
#Instancio un objeto de la clase Telefono
telefono1 = Telefono("Samsung", "Galaxy S21","negro")
print(telefono1.marca) #Accedo al atributo marca del objeto telefono1
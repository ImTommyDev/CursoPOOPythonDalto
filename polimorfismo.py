class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    
#Primera forma de aplicar polimorfismo
gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido()) #Esto es polimorfismo, ya que el mismo método sonido() se comporta de diferente manera dependiendo del objeto que lo llama.

print("-"*20)

#Segunda forma de aplicar polimorfismo
def hacerSonido(animal):
    print(animal.sonido())
    
hacerSonido(gato) 
hacerSonido(perro) #Esto es polimorfismo, ya que la función hacerSonido() puede recibir diferentes tipos de objetos y el método sonido() se comporta de diferente manera dependiendo del objeto que se le pase como argumento. 

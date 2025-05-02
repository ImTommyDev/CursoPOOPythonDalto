class Animal():
    def comer(self):
        print("El animal come")
    
class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero amamanta")
    
class Ave(Animal):
    def volar(self):
        print("El ave vuela")
        
class Murcielago(Mamifero,Ave):
    # def comer(self):
    #     return super().comer()
    
    # def amamantar(self):
    #     return super().amamantar()

    # def volar(self):
    #     return super().volar()
    pass
    
lucas = Murcielago()
lucas.amamantar()
lucas.volar()
lucas.comer()


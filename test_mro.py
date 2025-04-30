#Practicando con el MRO por mi cuenta

class A():
    pass
    
class B(A):
    pass

class C(B):
    pass
    
class D():
    def saludo(self):
        return "Hola desde D"

class E(C, D):
    pass

# Verificando el MRO de la clase E
print(E.__mro__)
    
e = E()
print(e.saludo())
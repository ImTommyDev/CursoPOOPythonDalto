#MRO (Método de Resolución de Orden) es el orden en el que python busca los metodos y atributos de una clase, tengo que saber que se ejecutará primero y que tiene prioridad y que no

class A:
    def hablar(self):
        print("Hola desde A")
        
class F:
    def hablar(self):
        print("Hola desde F")
        
class B(A):
    pass

class C(F):
    def hablar(self):
        print("Hola desde C")
        
class D(B, C): 
    pass
        
#Heredo de B y C, si no tengo el metodo hablar en D, busco en B y C, primero busca en B y luego en C, si no estuviese en ninguna de las dos clases, buscaría en A (en el caso de que ambas herenden de A)
# Si C hereda de F, primero se verás todo el arbol de B, es decir (B > A) y si no está ahí ya busca en C        
d = D()
d.hablar() #Hola desde D
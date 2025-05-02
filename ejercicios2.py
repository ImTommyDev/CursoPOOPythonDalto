class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def grado_estudiante(self):
        return f"Estoy en el grado {self.grado}."
    
lucas = Estudiante("Lucas", 20, str("3er año"))
print(lucas.saludar())
print(lucas.grado_estudiante())

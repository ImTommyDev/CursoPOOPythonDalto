class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        

class Estudiante(Persona):
    def __init__(self, nombre, edad,curso,media):
        super().__init__(nombre, edad)
        self.curso = curso
        self.media = media
        
    def mostrar_notas(self):
        print(f"{self.presentarse()} estoy en {self.curso} y mi media es {self.media}.")


pacual = Estudiante("Pacual", 20, "1º", 8.5)
pacual.mostrar_notas()
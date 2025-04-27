class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
        

class Estudiante(Persona):
    def __init__(self, nombre, edad,curso,media):
        super().__init__(nombre, edad)
        self.curso = curso
        self.media = media
        
    def mostrar_notas(self):
        print(f"{self.presentarse()} Estoy en {self.curso} y mi media es {self.media}.")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,empresa,sueldo):
        super().__init__(nombre, edad)
        self.empresa = empresa
        self.sueldo = sueldo
        
    def mostrar_datos(self):
        print(f"{self.presentarse()} Trabajo en {self.empresa} y mi sueldo es {self.sueldo}.")


pacual = Estudiante("Pacual", 20, "1º", 8.5)
joselui = Trabajador("Joselui", 30, "Google", 3000)
pacual.mostrar_notas()
joselui.mostrar_datos()
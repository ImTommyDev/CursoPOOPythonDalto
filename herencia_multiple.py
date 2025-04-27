class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
        

class Estudiante():
    def __init__(self,curso,media):
        self.curso = curso
        self.media = media
        
    def mostrar_notas(self):
        return f"Estoy en {self.curso} y mi media es {self.media}."
        
class PersonaEstudiante(Persona, Estudiante):
    def __init__(self, nombre, edad, curso, media):
        Persona.__init__(self, nombre, edad)
        Estudiante.__init__(self, curso, media)
        
    #IMPORTANTE: Si yo ahora defino otro metodo presentarse en la clase PersonaEstudiante, este va a sobreescribir el de la clase Persona. Por lo tanto, si quiero que se ejecute el de la clase Persona, tengo que llamarlo usando super().
    def presentarse(self):
        return "heeyyyyy"
            
    def mostrar_datos(self):
        #Con self accedo al metodo presentarse de la clase PersonaEstudiante, y con super() al de la clase Persona.
        print(f"{self.presentarse()}, {super().presentarse()} {self.mostrar_notas()}. MI NOMBRE ES {self.nombre} Y TENGO {self.edad} AÑOS.")
        
carlos = PersonaEstudiante("Carlos", 25, "2º", 9.0)
carlos.mostrar_datos()
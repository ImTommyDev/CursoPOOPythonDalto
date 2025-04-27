class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")
       
        
# Crear una instancia de la clase Estudiante
# estudiante1 = Estudiante("Juan", 20, "Ingeniería")
# estudiante2 = Estudiante("María", 22, "Arquitectura")
# estudiante3 = Estudiante("Pedro", 21, "Medicina")
# print("Datos del estudiante 1:")
# estudiante1.mostrar_informacion()
# print("Datos del estudiante 2:")
# estudiante2.mostrar_informacion()
# print("Datos del estudiante 3:")
# estudiante3.mostrar_informacion()

#Interacción con el usuario
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
carrera = input("Ingrese la carrera del estudiante: ")
estudiante = Estudiante(nombre, edad, carrera)
estudiante.mostrar_informacion()
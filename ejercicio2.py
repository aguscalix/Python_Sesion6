'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los
métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

from re import A


class Alumno:
    nombre = None
    nota = None

    def __init__ (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def evaluacion(self):
        if self.nota > 70:
            print("Has aprobado, Felicidades!")
        else:
            print("Reprobado, Repite el curso.")


estudiante = Alumno("Ricardo", 95)

print(f"Estudiante: {estudiante.nombre}")
print(f"nota: {estudiante.nota}")
estudiante.evaluacion()
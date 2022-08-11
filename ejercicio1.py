'''En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
*Color
*Ruedas
*Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
*Velocidad
*Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''

class Vehiculo:
    color = "negro"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 140
    cilindrada = 4


turismo = Coche()

print(f"Cilindrada: {turismo.cilindrada}")
print(f"Velocidad: {turismo.velocidad} km/h")
print(f"Puertas: {turismo.puertas}")
print(f"Ruedas: {turismo.ruedas}")
print(f"Color: {turismo.color}")
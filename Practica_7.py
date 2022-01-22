"""Practica 7: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 7:
	Crea un programa que pida números infinitamente. Los números introducidos deben
	ser cada vez mayores El programa finalizará cuando se introduce un número menor que
	el anterior."""

print("Programa solicita números infinitamente")


numAnterior=int(input("Introduce un número: "))
numNuevo=int(input("Introduce un número mayor que " + str(numAnterior) + ": "))

while numNuevo>numAnterior:
		numAnterior=numNuevo
		numNuevo=int(input("Introduce un número mayor que " + str(numAnterior) + ": "))

print(numNuevo, "no es mayor que", str(numAnterior))

"""Me encanta aprender, si tienes algún aporte que me ayude a hacer más eficiente el código será bien recibido, muchas gracias"""
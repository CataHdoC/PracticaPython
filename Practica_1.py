"""Practica 1: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 1:
	Crea un programa que pida dos números por teclado. El programa tendrá una función
	llamada “DevuelveMax” encargada de devolver el número más alto de los dos
	introducidos"""

print("Programa para hallar el máximo entre dos números")

numero1=input("Introduce el primer número: ")
numero2=input("Introduce el segundo número: ")

while numero1==numero2:
	print("Los números son iguales")
	
	numero1=input("Introduce el primer número: ")
	numero2=input("Introduce el segundo número: ")


def DevuelveMax(num1, num2):
	maximo=num1
	if num1<num2:
		maximo=num2
	return maximo


#print(max(8,2))
print("El número mayor es: ")
print(DevuelveMax(float(numero1), float(numero2)))
print("El programa ha finalizado")

"""Me encanta aprender, si tienes algún aporte que me ayude a hacer más eficiente el código será bien recibido, muchas gracias"""
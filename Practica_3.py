"""Practica 3: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 3:
	Crea un programa que pida tres números por teclado. El programa imprime en consola
	la media aritmética de los números introducidos."""

print("Programa realiza las operaciones aritméticas y la media aritmética de los números introducidos")

def suma(num1, num2, num3):
	resultado=num1+num2+num3
	return resultado

def resta(num1, num2, num3):
	resultado=num1-num2-num3
	return resultado

def producto(num1, num2, num3):
	resultado=num1*num2*num3
	return resultado

def mediaAritmetica(num1, num2, num3):
	resultado=(num1+num2+num3)/3
	return resultado

def division(num1, num2):
	resultado=num1/num2
	return resultado

operacion=input("Introduce la operacion a realizar \nEscribe a continuación la operación deseada \nsuma, resta, producto, media aritmética o división: ")

if operacion=="suma" or operacion=="resta" or operacion=="producto" or operacion=="media aritmética":
	numero1=float(input("Introduce el primer número: "))
	numero2=float(input("Introduce el segundo número: "))
	numero3=float(input("Introduce el tercer número: "))
else:
	numero1=float(input("Introduce el primer número: "))
	numero2=float(input("Introduce el segundo número: "))

if operacion=="suma":
	result=suma(numero1, numero2, numero3)
elif operacion=="resta":
	result=resta(numero1, numero2, numero3)
elif operacion=="producto":
	result=producto(numero1, numero2, numero3)
elif operacion=="media aritmética":
	result=mediaAritmetica(numero1, numero2, numero3)
else:
	result=division(numero1, numero2)


print("\nEl resultado de la operación " + operacion + " es: " + str(result))

"""Me encanta aprender, si tienes algún aporte que me ayude a hacer más eficiente el código será bien recibido, muchas gracias"""

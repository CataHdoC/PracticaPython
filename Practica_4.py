"""Practica 4: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 4:
	Crea un programa que muestre los números impares del 1 al 100. Los números deberán
	aparecer una al lado del otro sin salto de línea"""

print("Programa para generar los números impares del 1 al 100")

#Solución simple
print("Solución simple \n")
for i in range(1, 100, 2):
	print(i, end=" ")

print("\n")

#Solución usando generadores
print("Solución usando generadores \n")
def generaImpares(limite):
	num=1

	while (num+(num-1))<limite:
		
		yield num+(num-1)

		num=num+1


devuelveImpares=generaImpares(100)


#Código para que devuelva todo el generador creada
for i in devuelveImpares:

	print(i, end=" ")


"""Me encanta aprender, si tienes algún aporte que me ayude a hacer más eficiente el código será bien recibido, muchas gracias"""
"""Practica 6: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 3:
	Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
	función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
	correcta si solo tiene una “@” y si tiene uno o más “.”"""

print("Programa válidar correo electrónico")

email=input("Introduce email: ")

arroba=0
punto=0

for i in range(len(email)):

	if email[i]=="@":
		arroba += 1

	if email[i]==".":
		punto += 1

print(arroba, punto)

if arroba==1 and punto==1:
	print("Correo electrónico correcto")
else:
	print("Correo electrónico erróneo")
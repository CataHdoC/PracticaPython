"""Practica 2: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 2:
	Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
	deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
	personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
	teclado)."""

print("Programa para almacenar datos introducidos en una lista")

def contarDigitos(cadena):
	digitos=0

	for c in cadena:
		if c.isdigit():
			digitos += 1
		else:
			pass
	
	return digitos

def validarEmail(correo):
	for i in correo:
		if i=="@":
			arroba=True
			break;
	else:
		arroba=False

	for i in correo:
		if i==".":
			punto=True
			break;
	else:
		punto=False

	if arroba and punto:
		valido=True
	else:
		valido=False

	return valido


nombre=input("Introduce el nombre: ")
direccion=input("Introduce la dirección: ")
email=input("Introduce el email: ")
incluyeArroba=validarEmail(email)

while incluyeArroba==False:
	print("El email no es válido")
	
	email=input("Introduce un email válido: ")
	incluyeArroba=validarEmail(email)

print("Email válido")


celular=input("Introduce el número de celular: ")
cant_numeros=contarDigitos(celular)

while cant_numeros!=10:
	print("El número de celular en inválido")
	
	celular=input("Introduce un número de celular de 10 dígitos: ")
	cant_numeros=contarDigitos(celular)

print("Celular válido")

listaDatos=[nombre, direccion, email, celular]

print("\nLos datos personales son: \n" + 
	"Nombre: " + listaDatos[0] +", \n"+
	"Dirección: "+ listaDatos[1] +", \n"+
	"Email: "+ listaDatos[2] +" y \n"+
	"Celular: "+ listaDatos[3] +".")

"""Me encanta aprender, si tienes algún aporte que me ayude a hacer más eficiente el código será bien recibido, muchas gracias"""
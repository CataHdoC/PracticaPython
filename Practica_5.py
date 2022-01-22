"""Practica 5: Este programa hace parte de la práctica del curso Python"""
"""Ejercicio 5:
	Crea un programa que pida por teclado introducir una contraseña. La contraseña no
	podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
	el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
	errónea”"""

#Solución 1 con bucle
print("Programa válidar contraseña")

def contarCaracteres(cadena):
	caracteres=0
	espacios=0

	for c in cadena:
		if c.isalpha() or c.isdigit():
			caracteres += 1
		else:
			espacios += 1
	
	return caracteres, espacios


print("La contraseña no puede contener espacios y debe ser de mínimo 8 caracteres")
password=input("Introduce contraseña: ")

cantidad=contarCaracteres(password)
#print(cantidad[0], cantidad[1])


while cantidad[0]<8 or cantidad[1]!=0:
	print("Contraseña errónea")
	if cantidad[0]<8:
		print("La contraseña deben ser de mínimo 8 caracteres")

	if cantidad[1]!=0:
		print("La contraseña no puede contener espacios")

	password=input("Introduce contraseña sin espacios y con al menos 8 caracteres: ")
	cantidad=contarCaracteres(password)
	#print(cantidad[0], cantidad[1])

print("Contraseña OK")


#Solución 2
_password=input("Introduce contraseña: ")

contador=0

for i in range(len(_password)):

	if _password[i]==" ":
		contador=1

if len(_password)<8 or contador>0:
	print("Contraseña errónea")
else:
	print("Contraseña correcta")


"""Me encanta aprender, si tienes algún aporte que me ayude a hacer más eficiente el código será bien recibido, muchas gracias"""
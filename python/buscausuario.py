usuario=input("Dime un usuario: ")
cont=0
with open("/etc/passwd","r") as fichero: 
	for linea in fichero:
		if usuario == linea.split(":")[0]:
			cont=cont+1


if cont == 1: 
	print("El usuario existe.")
else:
	print("El usuario no existe.")
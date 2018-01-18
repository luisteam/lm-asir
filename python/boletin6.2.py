from crypt import crypt
import getpass

with open("shadow.txt","r") as f:
	claves=f.read()
	claves2=claves.split("\n")

	usuario=input("Usuario:")
	clave=getpass.getpass("Contraseña: ")

	for i in claves2:
		claves3=i.split(":")
		if claves3[0]==usuario:
			sal=claves3[1]
			sal=sal[0:12]
			

cencriptada=crypt(clave,sal)
cadencrypt=usuario+":"+cencriptada

for i in claves2:
	cad=i.split(":")
	if cad[0]==usuario:
		if cadencrypt==cad[0]+":"+cad[1]:
			cont=1

if cont==1:
	print("Login completado.")
else:
	print("Error.")
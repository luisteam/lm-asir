from crypt import crypt
import getpass

with open("shadow.txt","r") as f:
	claves=f.read()
	claves2=claves.split("\n")

	usuario=input("Usuario:")
	
	with open("crackeo.txt","r") as c:
		clave=c.read()
		clave2=clave.split("\n")


	for i in claves2:
		claves3=i.split(":")
		if claves3[0]==usuario:
			sal=claves3[1]
			sal=sal[0:12]


for i in claves2:
	cad=i.split(":")
	if cad[0]==usuario:
		for i in clave2:
			cencriptada=crypt(i,sal)
			cadencrypt=usuario+":"+cencriptada
			if cadencrypt==cad[0]+":"+cad[1]:
				cont=1
				crack=i
if cont==1:
	print("Login completado.")
	print("La clave es %s" % (crack))
else:
	print("Error.")
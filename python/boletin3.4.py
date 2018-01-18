lista=[]
edades=[]
mayores=[]
mayoresnom=[]

nombre=(str(input("Nombre del alumno: ")))
lista.append(nombre)
while nombre!= "*":
	edad=(int(input("Edad del alumno: ")))
	lista.append(edad)
	edades.append(edad)
	if edad >= 18:
		mayores.append(edad)
		mayoresnom.append(nombre)
	nombre=(str(input("Nombre del alumno: ")))
	lista.append(nombre)

#Mas edad
mayor=max(edades)
mayor1=lista.index(mayor)
mayor1=mayor1-1
edadm=lista.pop(mayor1)
print("El alumno de mayor edad es %s." % (edadm))
#Media de edad de la clase
media1=sum(edades)
media2=len(edades)
media=media1/media2
print("La edad media de la clase es: %.2f" % (media))
#busqueda
busca=input("Dime nombre de alumno en la base de datos: ")
busca1=lista.index(busca)
busca1=busca1+1
edad1=lista.pop(busca1)
print("La edad del alumno es %d años." % (edad1))
#Lista con mayores de edad
print("Los mayores de edad son: ")
eda=len(mayoresnom)
for i in range(0,eda):
	numero=(i+1)
	print("%d %s %d años." % (numero,mayoresnom.pop(0),mayores.pop(0)))
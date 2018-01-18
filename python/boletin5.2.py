import re

lista=[]
mayores=[]
vocales=[]
espacios=[]

cadena=(str(input("Dime una palabra: ")))
lista.append(cadena)
while cadena!= "*":
	cadena=(str(input("Dime una palabra: ")))
	lista.append(cadena)
	vocales.append(cadena)
	espacios.append(cadena)
lista.remove("*")

#OrdenAlfabetico
alf=sorted(lista, key = str.lower)
print("Aqui tienes la lista ordenada alfabeticamente: %s" % (alf))
#Mayorde5
alf.reverse()
for i in range(len(alf)):
	cadena1=alf.pop()
	tam=len(cadena1)
	if tam >= 5:
		mayores.append(cadena1)
print("Aqui tienes las cadenas mayores de 5 caracteres: %s" % (mayores))
#Vocales
cont=0
for i in range(len(vocales)):
	cadena2=vocales.pop()
	vocal=cadena2[0:1]

	if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
		cont=cont+1
print("El numero de cadenas que empiezan por vocal son: %d" % (cont))
#espacio
conts=0
for i in range(len(espacios)):
	cadena3=espacios.pop()
	cadena31=cadena3.count(' ')
	if cadena31 >= 1:
		conts=conts+1
if conts >= 1:
	print("Existen espacios entre algunas cadenas.")
#^coincidencias
cadena2=(input("Dime otra palabra: "))

for elemento in lista:
    if re.search("^"+cadena2, elemento):
        print(elemento)
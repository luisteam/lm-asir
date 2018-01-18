lista=[]

cadena=int(input("Digame cuantas palabras tiene la primera lista: "))
cadena1=cadena+1

for i in range(1,cadena1):
	lista.append(input("Digame la palabra {}: " .format(i)))

print("La primera lista es: ", lista)

lista2=[]

cadena2=int(input("Digame cuantas palabras tiene la segunda lista: "))
cadena3=cadena2+1

for i in range(1,cadena3):
	lista2.append(input("Digame la palabra {}: " .format(i)))

print("La segunda lista es: ", lista2)

lista1= set(lista)
lista22= set(lista2)
listamezcla= (lista1 & lista22)
listasolo1=(lista1 - lista22)
listasolo2=(lista22 - lista1)
listall=(lista1 | lista22)

if len(listamezcla) > 0 :
    print("Palabras que aparecen en las dos listas: {}".format(len(listamezcla)))
    print(listamezcla)
else:
    print("no hay palabras repetidas.")

print("Palabras que sólo aparecen en la primera lista: ", listasolo1)

print("Palabras que sólo aparecen en la segunda lista: ", listasolo2)

print("Todas las palabras: ", listall)
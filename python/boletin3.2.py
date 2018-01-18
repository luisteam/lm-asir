lista=[]

cadena=int(input("Digame cuantas palabras tiene la lista: "))
cadena1=cadena+1

for i in range(1,cadena1):
	lista.append(input("Digame la palabra {}: " .format(i)))

print("La lista creada es: ", lista)

menu='''Elige opción: 
1. Contar 
2. Modificar 
3. Eliminar 
0. Salir'''
print()
print(menu)
opcion=int(input())

if opcion == 1:
	busca=input("Digame la palabra a buscar: ")
	busca1=lista.count(busca)
	if busca1 != 1:
		print("La palabra %s aparece %d veces en la lista." % (busca,busca1))
	else:
		print("La palabra %s aparece %d vez en la lista." % (busca,busca1))

if opcion == 2:
	sust=input("Sustituir la palabra: ")
	sust2=input("por la palabra: ")
	sust3=lista.index(sust)
	lista.remove(sust)
	lista.insert(sust3,sust2)
	print("La lista es ahora: ", lista)

if opcion == 3:
	eliminar=input("Palabra a eliminar: ")
	lista.remove(eliminar)
	print("La lista es ahora: ", lista)

if opcion == 0:
	print("Adios!!")
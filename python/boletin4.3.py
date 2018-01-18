cadena=input("Dime una palabra: ")
contador=0
lista=[]

busca=" "
reemplazo=""
cadena=cadena.replace(busca, reemplazo)


lista.append(list(cadena))
lista1=lista.pop(0)
print(lista1)

for palabra in range(len(cadena)):
	busca=lista1.pop()
	print(busca)
	cantidad=lista1.count(busca)
	print(cantidad)
	if cantidad == 1:
		contador=contador+1

if contador == 0:
	print("No tiene caracteres repetidos")
else:
	print("Se repite algun caracter")
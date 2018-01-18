cad=input("binario: ")
resultado=0

for indice,valor in enumerate(cad[::-1]):
	if valor=="1":
		resultado=resultado+(2**indice)
print(resultado)
print("DIVISORES")
numero=int(input("Escriba un numero mayor que cero: "))

if numero <= 0:
	print("¡Le he pedido un numero entero mayor que cero!")
else:
	frase=("Los divisores de %d son"% (numero))
	print(frase, end=": ")
	for i in range(1, numero + 1):
		if numero % i == 0:
			print(i,end=" ")
print()
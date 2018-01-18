print("SUMA ENTRE VALORES")
valor1 = int(input("Escriba un numero entero: "))
valor2 = int(input("Escriba un numero mayor que %d: " % (valor1)))

if valor2 <= valor1:
	print("¡Le he pedido un número entero mayor que %d!" % (valor1))
else:
	suma = 0
	for i in range(valor1, valor2 + 1):
		suma = suma + i
	print("La suma desde %d hasta %d es %d" % (valor1,valor2,suma))

	for i in range(valor1,valor2):
		cadena=("%d + " % (i))
		print(cadena, end="")
	print("%d = %d" % (valor2,suma))
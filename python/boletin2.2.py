print("MAYORES QUE EL PRIMERO")
cantidad=int(input("¿Cuantos valores va a introducir: "))
if cantidad < 1:
	print("¡Imposible!")
else:
	valores=int(input("Escriba un numero: "))
	for i in range(cantidad - 1):
		numeromay=int(input("Escriba un numero mas grande que %d: " % (valores)))
		print(numeromay)
		if numeromay <= valores:
			print("¡%d no es mayor que %d!" % (numeromay,valores))
	print("Gracias por su colaboracion")

print("ECUACION A X + B = 0")

val = int(input("Valor A es: "))
val2 = int(input("Valor B es: "))

#nega= -(val2)
#div= nega/val

if val == 0:
	if val2 == 0:
		print("Todos los numeros son solucion.")
	else:
		print("La ecucacion no tiene solucion.")

if val != 0:
	if val2 !=0:
		nega= -(val2)
		div	= nega/val
		print("La ecuacion tiene una solucion: %d" % (div))
	else:
		print("La ecucacion no tiene solucion.")
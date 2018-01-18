from random import randint

bucle = int(input("Numero de preguntas: "))

if bucle < 1:
	print("El numero de preguntas debe ser al menos 1")
else:
	aciertos = 0
	for i in range(bucle):
		a = randint(2, 10)
		b = randint(2, 10)

		resultado = int(input("¿Cuanto es %d x %d? " % (a,b)))

		if resultado == a*b:
			print("¡Respuesta correcta!")
			aciertos = aciertos + 1
		else:
			print("¡Respuesta incorrecta!")
		print()

	resultadon="Ha contestado correctamente %d" % (aciertos)
	
	if (aciertos == 1):
		print(resultandon + " pregunta")
	else:
		print(resultadon + " preguntas")
	nota = (aciertos / bucle * 10)
	print("Le corresponde una nota de %.2f" % (nota))
	if nota >= 9:
		print("¡Enhorabuena!")

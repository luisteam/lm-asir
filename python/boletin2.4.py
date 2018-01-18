inf=int(input("Dime el limite inferior: "))
sup=int(input("Dime el limite superior: "))
dentro=0
fuera=0
maximo=(0)
suma=0

if sup <= inf or inf <= 0 or sup <=0:
	print("Error")
else:
	valor=float(input("Escribe un numero: "))
	while valor!=0:
		if valor >= sup or valor <= inf:
			fuera=fuera+1
			suma=suma+valor
			if valor > maximo:
				maximo = valor
			valor=float(input("Escribe un numero: "))
		else:
			dentro=dentro+1
			valor=float(input("Escribe un numero: "))
		
	media=float(suma)/fuera

	print("La cantidad de números dentro del intervalo es: %d" % (dentro))
	print("El máximo de los números fuera del intervalo es: %d" % (maximo))
	print("La media de los que no pertenecen al intervalo es: %.2f" % (media))

	if inf or sup == valor:
		print("Si se ha introducido un número igual a un límite del intervalo.")
numero1=int(input("Dame un numero: "))
numero2=int(input("Dame otro numero: "))

if numero1 + numero2 > 0:
	print("Es Positivo")
elif numero1 + numero2 < 0:
	print("Es Negativo")
else:
	print("Es cero")
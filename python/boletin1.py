num=int(input("Escribe el dividendo:"))
num2=int(input("Escribe el divisor:"))

if num ==0:
	print("Estas dividiendo entre 0.")
elif num2 ==0:
	print("Estas dividiendo entre 0.")
else:	
	coci=num//num2
	rest=num%num2 
	if rest ==0:
		print("La división es exacta. Cociente: %d Resto: %d" % (coci,rest))
	else:
		print("La división no es exacta. Cociente: %d Resto: %d" % (coci,rest))

num=int((input('Dime un numero: ')))

def cfactorial (numero):
	"""Calcula el factorial de un numero"""
	if numero == 1:
		return 1
	resultado=1
	for i in range(1,numero+1):
		resultado=resultado*i
	return resultado

fact=cfactorial(num)

print(fact)
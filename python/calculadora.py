def calculadora(numero1,numero2,operador):
	if "-" == operador:
		return(numero1-numero2)
	if "+" == operador:
		return(numero1+numero2)
	if "/" == operador:
		return(numero1/numero2)
	if "*" == operador:
		return(numero1*numero2)
	return None


entero1=int(input("Dime un numero: "))
entero2=int(input("Dime un numero: "))
operador=input("Dime el operador que desea: ")

print(calculadora(entero1,entero2,operador))
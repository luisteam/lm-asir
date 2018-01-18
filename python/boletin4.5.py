import random
digitos = ('0','1','2','3','4','5','6','7','8','9')
print("Bienvenido/a al Mastermind!")
print("Tenes que adivinar un numero de 4 cifras distintas")
palabra=input("Que código propones?: ")
contador1=0
contador2=0
intentos=1
codigo=""

for i in range(4):
	numero = random.choice(digitos)
	while numero in codigo:
		numero = random.choice(digitos)
	codigo = codigo + numero
	
while palabra!=codigo:
	intentos=intentos+1
	for i in range(4):
		if palabra[i]==codigo[i]:
			contador1=contador1+1
		elif palabra[i] in codigo:
			contador2=contador2+1

	print("Tu propuesta ( %s ) tiene %d aciertos y %d coincidencias." % (palabra,contador1,contador2))
	contador1=0
	contador2=0
	palabra=input("Propone otro codigo: ")


print("Felicitaciones! Adivinaste el codigo en, %d, intentos."%(intentos))
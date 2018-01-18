num=int(input("Dame un numero:"))
contador = 0
acumulador = 0
mayor = num
menor = num

while num!=0:
	if num % 2 == 0:
		print(num,"es par")
		contador = contador + 1
		if num > mayor or contador==1:
			mayor = num
	else:
		print(num,"es impar")
		if num < menor or acumulador==0:
			menor == num
		acumulador = acumulador + num
	if num==10:
		indicador=True

	num=int(input("Dame un numero:"))

print("Hemos Terminado")
print("Cantidad de pares",contador)
print("Suma de impares",acumulador)
print("El numero mayor de pares es", mayor)
print("El numero menor de impares es", menor)
if indicador:
	print("Has metido el 10")
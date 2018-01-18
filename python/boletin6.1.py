cuenta=input("Dime una cuenta bancaria(AAAA-BBBB-CC-DDDDDDDDDD): ")

datos=cuenta.split("-")
codbanco=datos[0]
cc=datos[2]
#AAAA-BBBB-CC-DDDDDDDDDD

lista=[]
for i in range(10):
	cliente=datos[3]
	lista.append(int(cliente[i]))

#lista = [1, 6, 7, 0, 0, 0, 0, 3, 3, 2]

def calcula_dc(lista):
 """Calcula el dígito de control de una CCC.
 Recibe una lista con 10 numeros enteros y devuelve el DC
 correspondiente"""
 pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
 aux = []
 for i in range(10):
     aux.append(lista[i]*pesos[i])
 resto = 11 - sum(aux) %11
 if resto == 10:
     return 1
 elif resto == 11:
     return 0
 else:
     return resto


if int(cc) == calcula_dc(lista):
	print("Cuenta bancaria valida.")
else:
	print("Error: Cuenta invalida.")

with open("bancos.txt","r") as f:
	bancos=f.readlines()

	encontrado=False

	for banco in bancos:
		cadena=banco.split(",")
		if codbanco == cadena[0]:
			encontrado=True
			print(cadena[1])
			break

	if not encontrado:
		print("No existe el banco") 

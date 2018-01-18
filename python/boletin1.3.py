print("COMPARADOR DE NUMEROS")

val = int(input("Valor uno es: "))
val2 = int(input("Valor dos es: "))
val3 = int(input("Valor tres es: "))

if val == val2:
	if val2 == val3:
		print("Ha escrito el mismo numero 3 veces.")
	else:
		print("Ha esrito el mismo numero 2 veces.")

if val != val3:
	if val2 == val3:
		print("Ha escrito 2 numeros veces.")

if val != val2:
	if val != val3:
		if val2 != val3: 
			print("Ninguno coincide.")

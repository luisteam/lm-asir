cad1=input("Dime una frase: ")
cad2=input("Dime otra frase: ")
caduno=cad1.upper()
caddos=cad2.upper()
fra1=caduno.split()
fra2=caddos.split()
cont=0

for frase in fra1:
	if frase in fra2:
		cont=cont+1

if cont>=1:
	print("La segunda cadena es una subcadena de la primera.")
else:
	print("La segunda cadena no es una subcadena de la primera.")
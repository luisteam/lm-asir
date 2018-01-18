cad=input("Cadena: ")
caracter=input("Caracer: ")
cad2=""
cont=0
for letra in cad[::-1]:
	cad2=cad2+letra
	cont+=1
	if cont!=len(cad) and cont%3==0:
		cad2=cad2+caracter
print(cad2[::-1])

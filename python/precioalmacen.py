with open("almacen.txt") as f:
	lineas=f.readlines()

busca=input("Dime un producto: ")

encontrado=False
for linea in lineas:
	datos=linea.split(",")
	if busca==datos[0]:
		encontrado=True
		operandos=list(map(int,datos[1:]))
		print(busca,operandos[0]*operandos[1])
		
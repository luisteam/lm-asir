almacen=[]
articulo=[]

code=int(input("Codigo articulo: "))
while code!=0:
	articulo.append(code)
	name=input("Nombre: ")
	articulo.append(name)
	unit=int(input("Cantidad: "))
	articulo.append(unit)
	price=float(input("Precio: "))
	articulo.append(price)
	almacen.append(articulo)
	articulo=[]
	code=int(input("Codigo articulo: "))
#1
for fila in almacen:
	for elem in fila:
		if fila.index(elem) == 0:
			codigo=elem
			
		if fila.index(elem) == 1:
			nombre=elem
			
		if fila.index(elem) == 3:
			precio=elem
	iva=precio*0.21+precio		
	print("El articulo %s con el codigo %d tiene un precio de %.2f euros." % (nombre, codigo, iva))
#2
for fila in almacen:
	for elem in fila:
		if fila.index(elem) == 0:
			codigo=elem
			
		if fila.index(elem) == 1:
			nombre=elem
			
		if fila.index(elem) == 3:
			precio=elem
			if precio<=10:
				print("El articulo %s con el codigo %d tiene un precio menor o igual a 10 euros." % (nombre, codigo))
#3
busca=int(input("Dime el codigo de un articulo: "))
if len(almacen) < busca:
	print("No existe el articulo.")
else:
	for i in range(len(almacen)):
		if almacen[i][0] == busca:
			print(almacen[i][1])
with open("/home/luis/Documentos/python/datos.txt","r") as f:
	lineas=f.readlines()
for linea in lineas:
	print(linea.split(",")[0])
	notas=linea.split(",")[1:]
	notas=list(map(int,notas))
	print(sum(notas)/len(notas))
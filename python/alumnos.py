lista=[]
continua="s"

num=int(input("Introduzca el numero d alumnos: "))
for i in range(num):
	notas=[]
	nombre=input("Introduzca el nombre: ")
	while continua=="s":
		nota=int(input("Introduce nota: "))
		notas.append(nota)
		continua=input("Quiere introducir otra nota?(s/n): ")
	lista.append([nombre,notas])
	continua="s"

for alum in lista:
	if sum(alum[1])/len(alum[1])>5:
		print("%d > %f"%(alum[0],(sum(alum[1])/len(alum[1]))))

encontrado=False	
nombre=input("Dime un nombre: ")
for alum in lista:
	if alum[0]==nombre:
		encontrado=True
		for nota in alum[1]:
			print(nota,end=" ")

if not encontrado:
	print("No existe alumno")
print()
lista=[]

num=int(input("Dime un numero: "))
while num!=0:
	lista.append(num)
	num=int(input("Dime un numero: "))

print("Ha introducido %d numeros." % (len(lista)))
print("El numero mas alto es: %d" % (max(lista)))
print(sorted(lista))
print("La media es %.2f: " % (sum(lista)/len(lista)))
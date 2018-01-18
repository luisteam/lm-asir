lista=[]
num=int(input("Dime el numero de dias: "))
num1=num+1
for i in range(1,num1):
	maximo=int(input("Dime el maximo del dia %d: " % (i)))
	minimo=int(input("Dime el minimo del dia %d: " % (i)))
	ldia=[]
	ldia.append(maximo)
	ldia.append(minimo)
	lista.append([ldia])

print (lista)
cont=1
for ldia in lista:
	for i in ldia:
		print("La temp.media del dia %d es %.2f" % (cont,(sum(i)/len(i))))
	cont = cont+1
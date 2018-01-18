print("Añadiendo numeros")

l1=[]

for i in range(5):
	num = int(input("Dime hasta 5 numeros: "))
	l1.append(num)

print(l1)
print("La media es %f" % (sum(l1)/len(l1)))

l2=[]

for elem in l1:
	l2.append(elem**2)
print(l2)

for elem1,elem2 in zip(l1,l2):
	print("%d => %d"%(elem1,elem2))
	
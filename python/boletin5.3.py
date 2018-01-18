import math
print("ECUACION ax^2 + bx + c = 0")

val = int(input("Valor A es: "))
val2 = int(input("Valor B es: "))
val3 = int(input("Valor C es: "))
raiz=(val2*val2)-(4*val*val3)

if val == 0:
	#ecuacion de primer grado x=-c/b
	print("X es %2f" % (-val3/val2))

elif raiz < 0:
	print("Raices complejas.")

else:
	raiz=math.sqrt(raiz)
	print("X es %d" % ((-val2+raiz)/(2*val)))
	print("X es %d" % ((-val2-raiz)/(2*val)))
year = int(input("¿En que año estamos?:"))
year2 = int(input("Ahora inventate uno:"))

if year < year2:
	cont = (year) - (year2)
	print("Faltan %d años para llegar al año %d." % (abs(cont),year2))
elif year > year2:
	cont = (year) - (year2)
	print("Han pasado %d años desde el año %d." % (abs(cont),year2))
else:
	print("¡Son el mismo año!")
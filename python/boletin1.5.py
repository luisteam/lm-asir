print("CONVERTIDOR DE CM A KM, M Y CM")
cent=int(input("Escribe en centimetros: "))

km = cent / 100000
m = (cent % 100000) / 100
cm = ((cent % 10000000) % 100)

if km != "0" != m:
	print (km)
elif km != "0" == m and cm != "0":
	print (km)
elif km != "0" and m == "0" == cm:
	print (km)
        
if m != "0" != cm:
	print (m)
elif m != "0" == cm:
	print (m)
        
if cm != "0" and km == "0" == m:
	print (cm)        
elif cm != "0" and (km != "0" or m != "0"):
	print (cm)


print(" %d centimetros son %d km, %d m, %d cm." % (cent , km , m , cm))
#import datetime

dia=int(input("Día: "))
mes=int(input("mes: "))
year=int(input("año: "))

date=("%d/%d/%d" % (dia,mes,year))
print("Fecha: %s" % (date))

if (dia < 1 or dia > 31):
	print("Día incorrecto")
	raise SystemExit

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
	if (dia < 1 or dia > 31):
		print("Fecha incorrecta")
		raise SystemExit
elif mes==4 or mes==6 or mes==9 or mes==11:
	if (dia < 1 or dia > 30):
		print("Fecha incorrecta")
		raise SystemExit
elif mes==2:
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		if (dia < 1 or dia > 29):
			print("Fecha incorrecta")
			raise SystemExit
	else:
		if (dia < 1 or dia > 28):
			print("Fecha incorrecta")
			raise SystemExit
else:
	print("Mes incorrecto")
	raise SystemExit
#libreria
#date1=("%d/%d/%d" % (year,mes,dia))
#fecha = datetime.datetime.strptime(date1, '%Y/%m/%d')
#cont=(fecha.strftime("%j"))

#print("Día Juliano: %s" % (cont))
cont=0
e= 31
f= 28
m= 31
a= 30
ma= 31
j= 30
jl= 31
ag= 31
s= 30
o= 31
n= 30
d= 31

if mes == 1:
	cont=cont+e
	rest=e

elif mes == 2:
	cont=cont+e+f
	rest=f

elif mes == 3:
	cont=cont+e+f+m
	rest=m

elif mes == 4:
	cont=cont+e+f+m+a
	rest=a

elif mes == 5:
	cont=cont+e+f+m+a+ma
	rest=ma

elif mes == 6:
	cont=cont+e+f+m+a+ma+j	
	rest=j

elif mes == 7:
	cont=cont+e+f+m+a+ma+j+jl
	rest=jl

elif mes == 8:
	cont=cont+e+f+m+a+ma+j+jl+ag	
	rest=ag

elif mes == 9:
	cont=cont+e+f+m+a+ma+j+jl+ag+s	
	rest=s

elif mes == 10:
	cont=cont+e+f+m+a+ma+j+jl+ag+s+o
	rest=o

elif mes == 11:
	cont=cont+e+f+m+a+ma+j+jl+ag+s+o+n
	rest=n

elif mes == 12:
	rest=d
	cont=cont+e+f+m+a+ma+j+jl+ag+s+o+n+d

if mes >= 2:
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		cont=cont+1
		if mes == 2:
			if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
				cont=cont-1

print("Día Juliano: %d" % (cont-(rest-dia)))
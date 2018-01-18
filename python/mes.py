mes=int(input("Dame un mes:"))
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
	print("Tiene 31 dias")
elif mes==4 or mes==6 or mes==9:
	print("Tiene 30 dias")
elif mes==2:
	print("28 o 29 dias")
else:
	print("Mes incorrecto")
letras="TRWAGMYFPDXBNJZSQVHLCKE"
dni=input("Dime tu DNI")

if len(dni)!=9:
	print("DNI Incorrecto")
elif not dni[:8].isdigit():
	print("DNI Incorrecto")
elif letras[int(dni[:8])%23]!=dni[8]:
	print("DNI Incorrecto")
else:
	print("DNI Correcto")
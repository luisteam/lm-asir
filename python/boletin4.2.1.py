cad=input("Dime una palabra polindroma(Ej: reconocer): ")

if cad[::-1]==cad:
	print("Es una palabra polindroma.")
else:
	print("No es una palabra polindroma.")
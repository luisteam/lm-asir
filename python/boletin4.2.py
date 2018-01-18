cad=input("Dime una frase polindroma(Ej: Yo hago yoga hoy): ")
busca=" "
reemplazo=""
cad1=cad.replace(busca, reemplazo)
cad2=cad1.lower()
if cad2[::-1]==cad2:
	print("Es una frase polindroma.")
else:
	print("No es una frase polindroma.")
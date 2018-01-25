#pasar_a_segundos

def pasar_a_segundos(cadena):
	horas=0
	minutos=0
	segundos=0

	tiempo=cadena.split(":")
	horas=int(tiempo[0])
	minutos=int(tiempo[1])
	segundos=int(tiempo[2])

	resultado=(((horas*60)+minutos)*60)+segundos

	print(resultado)
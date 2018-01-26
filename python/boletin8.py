from boletin81 import pasar_a_segundos
from boletin82 import calcular_coste
from boletin83 import convertir_a_euros

coste=[]
Lllamadas=[]
total=[]

tarifa=input("Tarifa centimos por segundo: ")
llamadas=input("Numero de llamadas:" )

for i in range(int(llamadas)):
	horas=int(input("Horas llamada %d: " % (i)))
	minutos=int(input("Minutos llamada %d: " % (i)))
	segundos=int(input("Segundos llamada %d: " % (i)))
	csegundos=pasar_a_segundos(horas,minutos,segundos)
	centimos=calcular_coste(csegundos,tarifa)
	euros=convertir_a_euros(centimos)
	coste.append(i)
	coste.append(euros)
	Lllamadas.append(coste)
	total.append(euros)
	coste=[]

for i in range(len(Lllamadas)):
	print("La llamada %d cuesta %f Euros" % (Lllamadas[i,0],Lllamadas[i,1]))


#3 3 25
#1650.75 Euros

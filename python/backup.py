import csv
import os

diccionario={}
almacen=[]

def media(suma, asignaturas):
	resultado = suma/asignaturas
	print(resultado)

for row in csv.reader(open("notas.csv")):
	diccionario['%s' % row[0]]={'Nombre': row[1], 'Apellidos': row[0],'Curso': row[2],'Notas':{'FH': row[3], 'LM': row[4], 'ISO': row[5], 'FOL': row[6], 'PAR': row[7], 'SGBD': row[8]}}
	almacen.append(row[0])

lista=[diccionario]

for name in almacen:
	persona=diccionario[name]
	
	curso=persona["Curso"]
	nombre=persona["Nombre"]
	notas=persona["Notas"]
	media1=notas["FH"]
	media2=notas["LM"]
	media3=notas["ISO"]
	media4=notas["FOL"]
	media5=notas["PAR"]
	media6=notas["SGBD"]
	if media1 != "FH":
		suma=[int(media1),int(media2),int(media3),int(media4),int(media5),int(media6)]
		print(sum(suma)/6)
	suma=[]	
#print("La nota media de %s es %.2f" % (nombre,media(suma,6)))
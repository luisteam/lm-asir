#alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
#            {"nombre":"Rafaela", ... },...]

import csv
import os

diccionario={}
almacen=[]
suma=[]

def media(suma, asignaturas):
	resultado = suma/asignaturas
	return resultado

for row in csv.reader(open("notas.csv")):
	diccionario['%s' % row[0]]={'Nombre': row[1], 'Apellidos': row[0],'Curso': row[2],'Notas':{'FH': row[3], 'LM': row[4], 'ISO': row[5], 'FOL': row[6], 'PAR': row[7], 'SGBD': row[8]}}
	if row[0] != 'Nombre':
		almacen.append(row[0])

lista=[diccionario]

#----------------Menu---------------------------------
print("A: Alumnos + Nota media")
print("B: Dime Curso y Asignatura")
print("C: Dime Curso y muestro porcentaje aprobados de cada asignatura")
print("D: Buscar curso y crear fichero con alumnos+nota media")
print("\n")
print("---- USAR MAYUSCULAS PARA CURSO----")
print("\n")

opcion=input("Dime una opcion: ")

#------------------Apartado 1-------------------------
if opcion=="A" or opcion=="a":	
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
			suma=sum(suma)
			
		print("La nota media de%s es: %.2f" % (nombre,media(suma,6)))
		suma=[]
#--------------Apartado 2-----------------------------
if opcion=="B" or opcion=="b":
	curso=input("Dime el curso: ")
	asignatura=input("Dime la asignatura: ")

	for name in almacen:
		persona=diccionario[name]
		clase=persona["Curso"]
		
		nombre=persona["Nombre"]
		notas=persona["Notas"]
			
		media1=notas["FH"]
		media2=notas["LM"]
		media3=notas["ISO"]
		media4=notas["FOL"]
		media5=notas["PAR"]
		media6=notas["SGBD"]

		if curso==clase and asignatura=="FH":
			print(nombre,media1)
		if curso==clase and asignatura=="LM":
			print(nombre,media2)
		if curso==clase and asignatura=="ISO":
			print(nombre,media3)
		if curso==clase and asignatura=="FOL":
			print(nombre,media4)
		if curso==clase and asignatura=="PAR":
			print(nombre,media5)
		if curso==clase and asignatura=="SGBD":
			print(nombre,media6)
#--------------Apartado 3-----------------------------
if opcion=="C" or opcion=="c":
	curso=input("Dime el curso: ")
	
	aprobadosfh=0
	suspensosfh=0

	aprobadoslm=0
	suspensoslm=0

	aprobadosiso=0
	suspensosiso=0

	aprobadosfol=0
	suspensosfol=0

	aprobadospar=0
	suspensospar=0

	aprobadossgbd=0
	suspensossgbd=0

	for name in almacen:
		persona=diccionario[name]
		clase=persona["Curso"]
		
		nombre=persona["Nombre"]
		notas=persona["Notas"]
			
		media1=notas["FH"]
		media2=notas["LM"]
		media3=notas["ISO"]
		media4=notas["FOL"]
		media5=notas["PAR"]
		media6=notas["SGBD"]

		if curso==clase:
			if int(media1) >= 5:
				aprobadosfh=aprobadosfh+1
			else:
				suspensosfh=suspensosfh+1
			
			if int(media2) >= 5:
				aprobadoslm=aprobadoslm+1
			else:
				suspensoslm=suspensoslm+1
			
			if int(media3) >= 5:
				aprobadosiso=aprobadosiso+1
			else:
				suspensosiso=suspensosiso+1

			if int(media4) >= 5:
				aprobadosfol=aprobadosfol+1
			else:
				suspensosfol=suspensosfol+1

			if int(media5) >= 5:
				aprobadospar=aprobadospar+1
			else:
				suspensospar=suspensospar+1

			if int(media6) >= 5:
				aprobadossgbd=aprobadossgbd+1
			else:
				suspensossgbd=suspensossgbd+1

			total1=(aprobadosfh+suspensosfh)
			porcentaje1=(aprobadosfh/total1)*100

			total2=(aprobadoslm+suspensoslm)
			porcentaje2=(aprobadoslm/total2)*100

			total3=(aprobadosiso+suspensosiso)
			porcentaje3=(aprobadosiso/total3)*100

			total4=(aprobadosfol+suspensosfol)
			porcentaje4=(aprobadosfol/total4)*100

			total5=(aprobadospar+suspensospar)
			porcentaje5=(aprobadospar/total5)*100

			total6=(aprobadossgbd+suspensossgbd)
			porcentaje6=(aprobadossgbd/total6)*100

	print("Porcentaje de aprobados es: \nFH: %.2f \nLM: %.2f \nISO: %.2f \nFOL: %.2f \nPAR: %.2f \nSGBD: %.2f" % (porcentaje1,porcentaje2,porcentaje3,porcentaje4,porcentaje5,porcentaje6))
#--------------Apartado 4-----------------------------
if opcion=="D" or opcion=="d":
	curso=input("Dime el curso: ")
	with open('nombredelcurso.txt','w') as archivo:

		for name in almacen:
			persona=diccionario[name]
			curso=persona["Curso"]
			nombre=persona["Nombre"]
			apellido=persona["Apellidos"]
			notas=persona["Notas"]
			media1=notas["FH"]
			media2=notas["LM"]
			media3=notas["ISO"]
			media4=notas["FOL"]
			media5=notas["PAR"]
			media6=notas["SGBD"]
			if media1 != "FH":
				suma=[int(media1),int(media2),int(media3),int(media4),int(media5),int(media6)]
				suma=sum(suma)
				
				linea=("%s %s: %.2f \n" % (nombre,apellido,media(suma,6)))
				archivo.write(linea)

			suma=[]

		print("Exportacion completada.")
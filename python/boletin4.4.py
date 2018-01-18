temperaturas='''
     Utrera,29,12
     Dos Hermanas,32,14
     Sevilla,30,15
     Alcalá de Guadaíra,31,14
     '''
#Utrera
temperaturas[6:18]
nombre1=temperaturas[6:12]
val1=temperaturas[13:15]
val2=temperaturas[16:18]
media=(int(val1)+int(val2))/2
print("%s tiene una media de %d grados." % (nombre1,media))

#DH
temperaturas[24:42]
nombre2=(temperaturas[24:36])
val3=temperaturas[37:39]
val4=temperaturas[40:42]
media2=(int(val3)+int(val4))/2
print("%s tiene una media de %d grados." % (nombre2,media2))

#SE
temperaturas[48:61]
nombre3=(temperaturas[48:55])
val5=temperaturas[56:58]
val6=temperaturas[59:61]
media3=(int(val5)+int(val6))/2
print("%s tiene una media de %d grados." % (nombre3,media3))

#ALC
temperaturas[67:91]
nombre4=(temperaturas[67:85])
val7=temperaturas[86:88]
val8=temperaturas[89:91]
media4=(int(val7)+int(val8))/2
print("%s tiene una media de %d grados." % (nombre4,media4))

pregunta=input("Dime una poblacion:")
nombre=pregunta.lower()
if nombre==nombre1.lower():
  print("%s tiene una maxima de %dºC y minima de %dºC." % (nombre1,int(val1),int(val2)))
elif nombre==nombre2.lower():
  print("%s tiene una maxima de %dºC y minima de %dºC." % (nombre2,int(val3),int(val4)))
elif nombre==nombre3.lower():
  print("%s tiene una maxima de %dºC y minima de %dºC." % (nombre3,int(val5),int(val6)))
elif nombre==nombre4.lower():
  print("%s tiene una maxima de %dºC y minima de %dºC." % (nombre4,int(val7),int(val8)))
else:
  print("Nombre incorrecto.")
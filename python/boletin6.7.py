from urllib.request import urlopen
temp=[]
pres=[]
hum=[]
contador=-1
temp1=[]

response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
lineas=response.readlines()
for i in lineas:
	contador=contador+1
	if lineas[1358] in i:

		lintemp=str(lineas[(contador+2)])
		lintemp=lintemp.split(">")
		temp=lintemp[1]
		temp=temp.split("<")
		temp=temp[0]
		temp=temp.split("&")
		temp=temp[0]

		linhum=str(lineas[(contador+7)])
		linhum=linhum.split(">")
		hum=linhum[1]
		hum=hum.split("<")
		hum=hum[0]
		hum=hum.split("%")
		hum=hum[0]

		linpres=str(lineas[(contador+8)])
		linpres=linpres.split(">")
		pres=linpres[1]
		pres=pres.split(" ")
		pres=pres[0]

final=("Dos Hermanas(Sevilla): \nTemperatura: %s° \nPresión: %shPa \nHumedad: %s" % (temp,pres,hum))
print(final+"%")

#<td>Ahora</td>
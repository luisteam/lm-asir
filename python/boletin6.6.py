import json

#{ "_id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ],
# "pop" : 15338, "state" : "MA" }

ciudad=""
estado=""

try:

	busca=input("Dime una ciudad de USA: ")

	with open("zips.json","r") as f:
		while ciudad != busca.upper():
			linea=f.readline()
			diccionario=json.loads(linea)
			ciudad=diccionario["city"]
			estado=diccionario["state"]

		geolocalizacion=diccionario["loc"]
		latitud=geolocalizacion[0]
		longitud=geolocalizacion[1]
		print("http://www.openstreetmap.org/search?query=akaska#map=15/%s/%s" % (latitud,longitud))
		print("Las coordenadas de %s(%s) Latitud: %s Longitud: %s" % (ciudad,estado,latitud,longitud))


except json.decoder.JSONDecodeError:
	print("La ciudad introducida no es correcta o no existe.")

#json.decoder.JSONDecodeError
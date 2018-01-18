import json

#{ "_id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ],
# "pop" : 15338, "state" : "MA" }

numero=0

with open("zips.json","r") as f:
	diccionario =json.loads(f.readline())
	Numero_de_codigo_postales =1
	estado=diccionario["state"]

	for linea in f:
		diccionario=json.loads(linea)
		if diccionario ["state"] == estado:
			Numero_de_codigo_postales +=1
			if Numero_de_codigo_postales >= 1:
				numero=numero+1
		else:
			if Numero_de_codigo_postales != 0:
				print("Estado:",estado, "Números De Código postal",Numero_de_codigo_postales)
				
				estado=diccionario["state"]
				Numero_de_codigo_postales=0

	if Numero_de_codigo_postales != 0:
		print("Estado:",estado, "Números De Código postal",Numero_de_codigo_postales)
	
	print("Existen", numero, "numeros postales")

ciudad=""
estado=""

with open("zips.json","r") as f:
	while ciudad != "AKASKA":
		linea=f.readline()
		diccionario=json.loads(linea)
		ciudad=diccionario["city"]
		estado=diccionario["state"]

	geolocalizacion=diccionario["loc"]
	latitud=geolocalizacion[0]
	longitud=geolocalizacion[1]
	print("http://www.openstreetmap.org/search?query=akaska#map=15/%s/%s" % (latitud,longitud))
	print("Las coordenadas de %s(%s) Latitud: %s Longitud: %s" % (ciudad,estado,latitud,longitud))
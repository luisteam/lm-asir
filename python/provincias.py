from lxml import etree

def nombre_provincias(doc):
	lista=[]
	provincias=doc.findall("provincia/nombre")
	for provincia in provincias:
		lista.append(provincia.text)
	return


doc = etree.parse('provinciasypoblaciones.xml')
lista_provincias=nombre_provincias(doc)
for prov in lista_provincias:
	print(prov)




def numero_localidades(doc):
	lista=[]
	provincias=doc.findall("provincia")
	for prov in provincias:
		nombre=prov.find("nombre").text
		localidades=len(prov.find("localidades"))
		lista.append((nombre,localidades))
	return lista

doc = etree.parse('provinciasypoblaciones.xml')
lista_provincias=nombre_provincias(doc)
for prov in lista_provincias:
	print(prov)
lista_num_localidades=numero_localidades(doc)
print(lista_num_localidades)


### Ejercicio 4
def poblaciones(prov,arbol):
	lista=[]
	provincias = arbol.findall('provincia')
	#Pedimos al usuario el nombre de la provincia:
	#Recorremos la lista de provincias
	for provincia in provincias:
		#obtenemos el nombre de la procinvia
		nombre = provincia.find('nombre')

		if nombre.text == prov:
		#almacenamos los elementos <localidad> en una lista
			localidades = provincia.findall('localidades/localidad')
			for localidad in localidades:
				lista.append(localidad.text)
			break
	return lista


### Ejercicio 5
def provinciav1(nombre_localidad,arbol):
	lista=[]
	provincias = arbol.findall('provincia')
	for provincia in provincias:
		localidades=provincia.findall("localidades/localidad")
		for localidad in localidades:
			if localidad.text==nombre_localidad:
				return provincia.find("nombre").text

### Ejercicio 6
lista_id=[]
id=input("id:")
while id!="0":
	lista_id.append(id)
	id=input("id:")

lista=provincias



### Ejercicio 1 xml users
def usuarios(arbol):
	lista=[]
	usuarios=arbol.findall("user")
	for user in usuarios:
		lista.append(user.find("firstname").text+" "+user.find("lastname"))
	return lista
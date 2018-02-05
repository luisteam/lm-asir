from lxml import etree
doc = etree.parse('books.xml')

titulos=doc.findall("book/tittle")
for titulo in titulos:
	print(titulo.text)


libros=doc.findall("book")
for libro in libros:
	print(libro.find("tittle").text)
	print(libro.find("price").text)
	#para mostrar varios autores
	autores=libro.findall("author")
	for autor in autores:
		print(autor.text)
	titulo=libro.find("tittle")
	print(titulo.attrib["lang"])





from lxml import etree
doc = etree.parse('books.xml')

libros=doc.findall("book")
for libro in libros:
	print(libro.find("tittle").text)
	autores=libro.findall("author")
	if len(autores)==0:
		print("No tiene autores")
	else:
		for autor in autores:
			print(autor.text)




from lxml import etree
doc = etree.parse('books.xml')

libros=doc.findall("book")
for libro in libros:
	if libro.find("prestado")!=None:
		print(libro.find("tittle").text)
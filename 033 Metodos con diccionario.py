teclados{
'teclado1' = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
},

'teclado2' = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
},
}

print(len(teclado1)+len(teclado2)) #cuenta los elementos del diccionario
del teclador1 # borra por complero el diccionario
teclado1.clear()
teclado2.update({"Color": "Negro"}) # agredar un elemento al diccionario


print(teclado1)

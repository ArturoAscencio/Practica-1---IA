teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

teclado1['Precio'] = '85'
print(teclado1['Precio'])

for x, y in teclado2.items():
    print(x,': ',y)

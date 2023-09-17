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

consulta = teclado1['Modelo'], teclado2['Precio'],teclado2['Modelo']
print(consulta)

muetrateclado = dict(teclado1)
print(muetrateclado)

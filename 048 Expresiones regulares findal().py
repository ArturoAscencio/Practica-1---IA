import re

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto) #findall() encuentra todo lo que le pongas en este caso es la letra "e"
print(busqueda)

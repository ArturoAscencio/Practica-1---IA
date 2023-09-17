import re

texto = "Bienvenidos a Programación fácil y bienvenidos al curso de Python."
buscar = re.findall("[c-g]", texto) # devuelve una lista con las coincidencias de entre c y g
print(buscar)

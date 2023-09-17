import re

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto) #split divide una cadena de caracteres segun lo que pusiste para que busque en este caso es el "espacio"
print(busqueda)

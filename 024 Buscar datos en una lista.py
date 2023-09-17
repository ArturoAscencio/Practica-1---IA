#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
entrada = input('Introduce el nombre de tu navegador:  ')
navegadores = ['chome','firefox','opera','safari'] 
if entrada in navegadores: # el in es para saber si esta dentro de la lista
    print('El navegador que buscas esta en la lista')
    
else:
    print('El navegador que buscas no esta en la lista')
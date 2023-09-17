edad = int(input('¿Cual es su edad?\n'))
if edad <= 0:
    print('Ninguna ersona puede tener esa edad.')
    
elif edad >= 1 and edad <=17:
    print('Usted es menor de edad')
    
elif edad <100:
    print('Usted es mayor de edad')
    
else:
    print('Edad no valida')

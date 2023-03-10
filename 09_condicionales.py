### Condicionales ### 
# La regla basica y fundamental de los IF es que para que se ejecute una accion el resultado de la condicion debe ser siempre 'TRUE', por el contrario si el resultado es FALSE y queremos que ejecute otro tipo de respuesta usamos el 'ELSE'

my_condicion = False
if my_condicion: # Es lo mismo que if my_coondition == True: 
    print('Se ejecuta la condicion del IF')


my_condicion = 5 * 5

if my_condicion == 10: 
    print('Se ejecuta la condicion del 2 IF')

if my_condicion > 10 and my_condicion < 20: 
    print('ES mayor que 10 y menor que 20')
elif my_condicion == 25: 
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor que 20 o distinto de 25')

 


print('La ejecucion continua')

# Podemos comprobar si una string esta vacio o no, TRUE si tiene texto y FALSE si no tiene texto
my_string = ''
if my_string: 
    print('Mi cadena tiene texto')
else: 
    print('Mi cadena esta vacia')

# Podemos poner condiciones con textos especificos
my_string = 'Mi cadena de texto'

if my_string == 'Mi cadena de texto': 
    print('My cadena es igual')
else: 
    print('mi cadena distinta')

# Podemos intercambiar el valor TRUE que tiene por defecto el IF a FALSE usando el operador logico 'NOT'

my_string = 'Texto'

if not my_string == 'Texto':
    print('ESTA bien')
else:
    print('Esta mal')
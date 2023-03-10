# STRINGS
mi_primer_string = 'Hola amor'
mi_segundo_string = 'como estas'
mi_tercer_straing = 'Bienvenido a Medallo \nEsta es la ciudad del arte y de las putas \ndiviertete bebe'
intero = 5 

"""FORMATEO"""
# El % sirve para cuando realmente queremos formatear o especificar el tipo de dato de una variable
print("Ella dice: %s\nEl dice: %s\ny el amigo dice: %s\ny el matematico dice: %d" %(mi_primer_string, mi_segundo_string, mi_tercer_straing, intero))

# El .format sirve para cuando queremos imprimir el dato exacto de nuestas variables
print("Ella dice: {}\nEl dice: {}\ny el amigo dice: {}\ny el matematico dice: {}" .format(mi_primer_string, mi_segundo_string, mi_tercer_straing, intero) )

# Una mej0r manera de usar el format: es mas optimizable y rapido de usar
print(f"Ella dice: {mi_primer_string}\nEl dice: {mi_segundo_string}\ny el amigo dice: {mi_tercer_straing}\ny el matematico dice: {intero}") 

"""DESEMPAQUETADO"""
fruta = "greipfruit"  
print(len(fruta))
a, b, c, d, e, f, g, h, i, j = fruta 
print(a)
print(e)

# Division 
fruta_slice = fruta[1:2]
print(fruta_slice)

# Reverse 
fruta_rverse = fruta[::-1]
print(fruta_rverse)

# Funciones 
print(fruta.capitalize())
print(fruta.upper())
print(fruta.lower())
print(fruta.count("r"))
print(fruta.isnumeric())
print("10".isnumeric())
print(fruta.upper().isupper())
print(fruta.lower().islower())
print(fruta.startswith("gr"))



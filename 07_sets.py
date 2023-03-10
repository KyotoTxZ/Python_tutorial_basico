### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un dictionary

my_other_set = {'Juan', 'Diego', 18, 1.75}

print(type(my_other_set)) # pero al insertar elemntos al estilo lista lo reconoce como un SET

my_other_set.add('LOro') 

my_other_set.add('Juan') # Un set no admite repetidos

print(my_other_set) # Un set no es una estructura ordenada, la manera de guardar los elementos es desordenada

# podemos validar con booleanos si un elemento existe dentro de un set
print('Juan' in my_other_set)
print('Juani' in my_other_set)

my_other_set.remove('Juan')
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

# al igual que con las tuplas podemos transformar un set a una lista y realizar cambios
my_set = {'Mela', 'Pela', 21, 1.50} 
my_set_list = list(my_set) 
print(my_set_list[1]) 
print(type(my_set_list)) 

# Concatenar sets entre si, para ello utilizamos el method union
my_other_set = {'Almendra', 'Conejo', 19}

my_new_set = my_other_set.union(my_set)
print(my_new_set)

# No podemos concatenar un mismo set entre si porque no acepta repetidos: 

print(my_other_set.union(my_other_set))

# Tambien podemos utilizar el union para agregar  mas elementos diferentes a un set: 
print(my_set.union({'ala', 100, 'madrid'}))

# Con difference Podemos ver los elementos que pertenecen a una variable frente a otra 
print(my_new_set.difference(my_set))



"""PARA QUE SE UTILIZAN LOS SETS"""
# Los sets (conjuntos) en Python se utilizan en varios casos importantes, incluyendo:

# Eliminación de elementos duplicados: los sets no permiten elementos duplicados, por lo que se pueden utilizar para eliminar duplicados de una lista o secuencia.

# Operaciones matemáticas: los sets permiten realizar operaciones matemáticas como la unión, intersección y diferencia de conjuntos.

# Verificación de pertenencia: se pueden utilizar sets para verificar si un elemento está en un conjunto o no.

# Filtrado de datos: se pueden utilizar sets para filtrar elementos en un conjunto dado.

# En resumen, los sets son una herramienta útil y eficiente en Python para trabajar con conjuntos de datos y realizar operaciones matemáticas y de pertenencia. 
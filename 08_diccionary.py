### DICTIONARYS ### 
# Su esctructura se basa en Clave - valor, clave siendi el primero elemento con y el valor es o los que esatn al frente de este. 
my_dict = dict()
print(my_dict)

my_other_dict = {}
print(type(my_dict)) 

my_dict = {
    'nombre': 'Juan', 
    'apellido': 'Baron', 
    'edad': 18, 
    1: 'stuck',
}

my_other_dict = {
    'nombre': 'Juan', 
    'apellido': 'Baron', 
    'edad': 18, 
    1: 'stuck',
    'lenguajes': {'Python', 'Java', 'C+'}
}

print(my_other_dict['lenguajes'])
print(my_dict[1])


# CAMBIAR VALORES DE CLAVES YA INEGRADAS EN EL DICT
my_dict['nombre'] = 'Diego'
print(my_dict)

# AGREGAR NUEVAS CLAVES CON SUS VALORES A UN DICT
my_dict['Barrio'] = 'Mirador'
print(my_dict)


# del sirve para eliminar un elementos de manera individual en los Dict

del my_dict['Barrio']
print(my_dict) 

# Buscamos por clave 
print('Baron' in my_dict)  # false
print('apellido' in my_dict ) # True

# Para buscar por valor 
print(my_dict['apellido'])


# OPERACIONES PARA DICT

print(my_dict.items()) # Un listado de cada uno de los items 
print(my_dict.keys()) # Muestra las calves del dict
print(my_dict.values()) # Muestra los valores del dict
print(dict.fromkeys(('apellido', 'age'))) # crear dicts sin valores 

# pasar una lista vacia a un diccionario vacio 
my_list = ['tamaño', 'color', 18]
print(dict.fromkeys(my_list))

# Crear un nuevo dict vacio con un dict con valores
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Insertar en todas las claves el mismo valor
my_new_dict = dict.fromkeys(my_dict, ['Lorenzo', 'Garza'] )
print(my_new_dict) 

# SI cambiamos un dict a otro formato solo nos muestra las claves
print(list(my_other_dict))
print(tuple(my_other_dict))
print(set(my_other_dict))

# para mostrar los valores usamos el method .values()
print(list(my_other_dict.values()))

# el tipo es dict_values
my_values = my_other_dict.values()
print(type(my_values))



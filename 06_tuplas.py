### TUPLAS ###

my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (1, 2, 3, 4, 5)

my_tuple = (18, 1.73, 'Juan', 'Baron',)
print(my_tuple)

print(my_tuple[2])

print(my_tuple.count(18))

## Index es un method que nos muestra el indice en el que encuentra un elemento, y si hay dos o mas elementos dentro, nos muestra el indice del elemento mas cercano, 
print(my_tuple.index('Baron'))


## AQUI estamos cambiando el valor del elemento(index 1) pero cuando lo imprimimos nos muestra un error.  
##my_tuple[1] = 1.80 '''error'''
##print(my_tuple)

'''LA MAYOR DIFERENCIA ENTRE UNA LISTA Y UNA TUPLA ES QUE: EN LA TUPLA UNA VEZ SE HALLAN ESCRITOS LOS ELEMENTOS, ESTOS NO SE PODRAN CAMBIAR POR OTROS VALORES, NI AGREGAR NI ELIMINAR SOLO DESDE (LA TUBLA RAIZ) 
*SON VALOLRES CONSTANTES* ''' 

## Pero si se puede concatenar tuplas entre si
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

## Mostrar elementos entre un indice inicial y un indice final
print(my_sum_tuple[2:6])


## SI QUEREMOS EDITAR EL CONTENIDO DE UNA TUPLA POR UN MOTIVO U OTRO, NOSOTROS PODRIAMOS TRANSFORMAR EL TIPO A UNA LISTA, REALIZAR EL CAMBIO Y VOLVER A PONERLE EL TIPO TUPLE
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple [2] = 'Diego'
my_tuple.append('Desarrollador')

my_tuple = tuple(my_tuple)
print(type(my_tuple))

print(my_tuple)

## CON del podremos eliminar la variable en su totalidad
del my_tuple 

# print(my_tuple)
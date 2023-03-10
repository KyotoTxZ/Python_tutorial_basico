# # # LISTAS # # #

my_list = list()


# Las posiciones de una lista comienzan en 0 - infinito
my_first_list = [1, 2, 3, 4, 5, 6, 7]

print(len(my_first_list))

my_list = [18, 1.73, "Juan", 'mp40',] 
print(my_list[3])  
 
print(my_list.count("Juan")) 

# Desempaquetar una lista, el nombre no importa, la posicion SI ya que se muestra ordenaqda
age, height, name, sexual_gender = my_list
print(sexual_gender)

# Concatenar Listas 
print(my_first_list + my_list)

# Methodos para listas
my_list.append('Juans')
my_list.insert(2, 'Negras')
print(my_list)

my_list.remove('Negras')
print(my_list)

my_pop_element = my_list.pop(1)
print(my_pop_element) 

my_copy_list = my_list.copy()


my_list.clear()
print(my_list)
print(my_copy_list)


my_copy_list.reverse()
print(my_copy_list)

## Sort sirve para ordenar una lista de NUMEROS (int and Floats) de menor a mayor por defecto, pero nosotros podemos agregarle parametros para ordenar la lista con distientas condiciones o reglas. 
lista_num = [1,2,3,4,5,1.5]
lista_num.sort()
print(lista_num)
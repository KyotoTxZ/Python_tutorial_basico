

# declarar variables
mi_variable = "0"
print(mi_variable)

mi_int_variable = 5

mi_boolean_var = True
print(mi_boolean_var)



# convertir un tipo de dato a otro mediante funciones 
mi_int_to_str_variable = str(mi_int_variable)
print(type(mi_int_to_str_variable))



# Concatenacion de variables
print(mi_int_variable, mi_variable, mi_boolean_var)

print("esta es la edad de mi novia:", mi_int_variable)



# (len) sirve para contar la cantidad exacta de caracteres o indices que tiene una String 
print(len("padreando por la street tio")) 



# Variables en una sola linea 
name, lastname, age,  heigt = "Juan", "Braon", 18, 1.73
print("Mi nombre es:", name, lastname, "mi edad es:", age, "y mido:", heigt )



# inputs o entradas son para recibir data, almacenarla luego en una variable y luego poder mostrarla en consola
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)




# forzamos el tipo
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address)) # pero no sirve ya que python maneja un tipado debil 





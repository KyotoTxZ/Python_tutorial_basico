### funciones ### 

def my_function (): 
    print("esto es una funcion")

my_function()

# le podemos psar parametros para con o sin informacion 
def sum_two_values (first_number, second_number): 
    print(first_number + second_number)

sum_two_values("tu ","mama")
sum_two_values(20, 10)
sum_two_values(2.6, 1.8)

def sum_two_values_with_return (first_number, second_number): 
    my_suma = first_number + second_number
    return my_suma 

my_result = sum_two_values_with_return(10, 5)
print (my_result) 


def print_name (name, surname): 
    print(f"{name} {surname} ") 
    
print_name(surname="Baron", name="Diego")

## podemos colocar valores predeterminados para los parametros si no los escribimos
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Diego", "Baron",)


## El * Nos permite escribir y manejar una cantidad de elementos infinitas que sea dinamica y flexible. 
def print_texts (*nums):
    for num in nums:
        print(num)

print_texts(1, 2, 4, 2.3, 8)


# podemos manejar y usar metodos para alterarlos de manera conjunta
def print_texts (*texts): 
    for text in texts: 
        print(text.upper()) 

print_texts("Juan", "ricardo", "Lorezo", "Braiano")
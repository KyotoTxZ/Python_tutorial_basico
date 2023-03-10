### Bucles/Loops ### 

# while / el while hace que un codigo se repita varias veces en funcion de una condicion
my_condition = 0 

while my_condition < 10: 
    print(my_condition) 
    my_condition += 2
if my_condition == 10: 
    print("es igual que 10") 
print(" la ejecucion continua ")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("es igual que 15")
        break # break condition sirve para detener el bucle con una condicion
    print(my_condition)  
    
# (FOR) se va a repetir tantas veces como elementos tengamos iterables dentro de algun conjunto de datos

my_first_list = [1, 2, 3, 4, 5, 6, 7] 
for i in my_first_list: 
    print(i)
    


my_tuple = (18, 1.73, 'Juan', 'Baron',)
for i in my_tuple:
    print(i)

# Mostramos los keys de los diccionarios 
my_dict = {
    'nombre': 'Juan', 
    'apellido': 'Baron', 
    'edad': 18, 
    1: 'stuck',
}
for i in my_dict: 
    print(i) 
    if i == 'edad':
        break 
        # 'continue' sirve para decirle al for que cuando no se ejecute alguna condicional o dato especifico continue pintando los dmas valore 
        # se desaconseja utilizarlo
    print("mi edad")
# elif i == 1: ## no se puede utilizar el elif 
else: 
    print('el bucle dict ha finalizado') # cuando usamos break rompemos el bucle y el else ya no se muestra

# Mostrar los valores 
# for i in list(my_dict.values()):
#     print(i)

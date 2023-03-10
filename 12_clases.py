## clases ## 
# sirve para crear una logica especifica y clasificar nuestro codigo en base a ello.

# por buenas practicas es recomendable escribir el nombre de las clases con CamelCase
class MyEmptyPerson: 
    pass 

class Person:
    def __init__(self, name, surname, priv, alias = 'alias',  ): # init es un constructor de clase
       self.name = name 
       self.surname = surname  
       self.alias = alias 
       self.__priv = priv # con __ creamos un parametro provado  
       self.full_name = f"{name} {surname} ({alias})" # podemos concatenar parametros
       # self se refiere a la clase en si misma, es una propiedad intrinseca a la clase que pertenece
       # pass 
       
    # un metodo/funcion que sirve para ejecutar acciones 
    def walk (self): # necesitamos pasarle el self como prop a los metodos para poder a los otros parametros de la clase
        print(f'{self.full_name} esta caminando') 
        
    def get_priv (self):
        raise self.__priv # ahora podemos accerder a este valor por medio de un metodo

my_person = Person("juan", "John", "luke", "kieas")
print(f'{my_person.name} {my_person.surname} {my_person.alias}')  


# podemos cambiar el valor de los parametros 
my_person.full_name = "Hector de leon"
my_person.walk() 

# my_person.__priv # Las props privadas no se pueden acceder asi no mas 


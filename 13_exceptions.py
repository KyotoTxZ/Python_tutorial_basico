### exception Handling ### 

num1, num2 = 5, 1 

num2 = "1" 
# num2 = 1 

# try except 
try:  
    print(num1 + num2) 
    print("exito") 
    print("________")
except: 
    print("error") # se ejecuta cuando el codigo tiene excepciones y no puede continuar corriendo el codigo
    
# try except else 
try:  
    print(num1 + num2) 
    print("exito") 
except: 
    print("error") 
else: # se ejecuta cuando el codigo no tiene excepciones y puede continuar corriendo 
    print("continua sin problemas") 
finally: 
    # Da igual que tenga excepciones o no: siempre se ejecuta siempre 
    print("finished") 
    


# Excepciones por tipo, para capturar errores especificos para ejecutar acciones especificas para cada una. 
try:  
    print(num1 + num2) 
    print("exito") 
except ValueError: # errores solo de valor
    print("value error")
except TypeError: # errores solo de tipo 
    print("type error")


# Captura de la info del error especifico en la exception 
try:  
    print(num1 + num2) 
    print("exito") 
except ValueError as error: # capturamos los datos del error en una variable la cual podemos utilizar para otras funciones
    print(error) 
except Exception as error:  # una forma de controlar cualquier tipo de error 
    print(error)  





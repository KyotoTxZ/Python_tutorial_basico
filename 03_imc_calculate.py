# # Operacion basica para calcular el indice de masa corporal con Python # #
# OPERACION: masa / (altura) * (altura)
print("¿Cual es tu peso?:")
peso = input() 
print("¿Cual es tu altura:")
altura = input()

imc = ( int(peso) / ( float(altura)**2 ) )

print(imc)
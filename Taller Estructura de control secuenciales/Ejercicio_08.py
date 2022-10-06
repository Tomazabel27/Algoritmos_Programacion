import math
#Entradas
lado1=float(input("Ingrese lado 1:"))
lado2=float(input("Ingrese lado 2:"))
lado3=float(input("Ingrese lado 3:"))
#Caja negra
s = (lado1 + lado2 + lado3) / 3
area = math.sqrt( s * ( s - lado1 ) * ( s - lado2 ) * ( s - lado3 ) )
#Salida
print ("El área es: " +str(area))
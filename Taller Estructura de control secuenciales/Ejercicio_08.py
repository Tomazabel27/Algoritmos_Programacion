from ast import Import
import math

#entradas
lado1=float(input("Ingrese lado 1:"))
lado2=float(input("Ingrese lado 2:"))
lado3=float(input("Ingrese lado 3:"))
#Caja
s=(lado1+lado2+lado3)/2
area=math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
print ("El área es: "+str(area) )
import math
#entradas
lado1=float(("Ingrese lado uno: "))
lado2=float(("Ingrese lado dos: "))
lado3=float(("Ingrese lado tres: "))
#caja negra
s=(lado1+lado2+lado3)/2
area=math.sqrt(s*(s-lado1)s*(s-lado2)s*(s-lado3))
#salidas
print("El area es:",+str(area))
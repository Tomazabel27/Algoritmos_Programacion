#Entradas
sueldo=int(input("Escriba su sueldo actual:"))
#Caja negra
porcentaje15=(sueldo*0.15)
porcentaje12=(sueldo*0.12)
nuevosueldo=""
if(sueldo<900000):
    nuevosueldo=(sueldo+porcentaje15)
elif(sueldo>=900000):
    nuevosueldo=(sueldo+porcentaje12)
#Salida
print("Su nuevo saldo sera de: $",nuevosueldo,"COP")
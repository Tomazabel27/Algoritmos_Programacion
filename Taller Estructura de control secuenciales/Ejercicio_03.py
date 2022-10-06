#Entradas
salario= int (input("Ingrese su salario: "))
venta1= int (input("Ingrese valor de su primera venta: "))
venta2= int (input("Ingrese valor de su segunda venta: "))
venta3= int (input("Ingrese valor de su tercera venta: "))

#Caja negra
com1=venta1*0.10
com2=venta2*0.10
com3=venta3*0.10
total=salario+com1+com2+com3
#Salida
print ("Su ingreso por la primera comision es: ", com1)
print ("Su ingreso por la segunda comision es: ", com2)
print ("Su ingreso por la tercera comision es: ", com3)
print ("Su ingreso total del mes es: ", total)
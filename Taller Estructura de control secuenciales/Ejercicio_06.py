#Entradas
test= int (input("Ingrese el total de estudiantes: "))
numh= int (input("Ingrese el numero de hombres: "))
numm= int (input("Ingrese el numero de mujeres: "))
#Caja negra
porcm= round((100*numm) / test), 2
porch= round((100*numh) / test), 2
#Salida
print ("El porcentaje de hombres es de: ",porch,"%")
print ("El porcentaje de mujeres es de: ",porcm,"%")
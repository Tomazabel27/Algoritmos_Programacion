#Entradas
lectant= int (input("Ingrese aqui el monto de la lectura electrica anterior: "))
lectact= int (input("Ingrese aqui el monto de la lectura electrica actual: "))
kilov= float (input("Ingrese aqui el valor del kilovateo: "))
#Caja negra
costofinal=(lectant-lectact)*kilov
#Salisdas
print("Debe pagar: $",costofinal,"COP por la luz este mes")
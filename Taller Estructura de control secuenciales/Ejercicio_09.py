#Entradas
horas= int (input("Ingrese las horas que trabajo al día: "))
dias= int (input("Ingrese los dias que trabajo en el mes: "))
Preciohora= int (input("Ingrese el valor que le pagaban por hora: "))
#Caja negra
horaames=horas*dias
salario= horaames*Preciohora
salariodesc=salario*0.2
salarioneto=salario-salariodesc
#Salida
print ("Usted trabajó:",horaames,"horas")
print ("Su salario por las horas trabajas es de: $",salario)
print ("Su salario neto es de: $",salarioneto)
#Entradas
name= (input("Ingrese su nombre: "))
horasndia= int (input("Ingrese el numero de horas normales que trabajó al día: "))
dias= int (input("Ingrese los días que trabajó: "))
valorhn= int (input("Ingrese lo que le pagaban por hora normal: "))
horase= int (input("Ingrese el numero de horas extra que trabajó: "))
#Caja negra
horasn=horasndia*dias
horastotales=horasn+horase
aumentohn=valorhn*0.25
valorhe=valorhn+aumentohn
pagohn=horasn*valorhn
pagohe=horase*valorhe
salariobase=pagohe+pagohn
decu1=salariobase*0.05
decu2=salariobase*0.02
decu3=salariobase*0.07
deduccion1=salariobase-decu1
deduccion2=salariobase-decu2
deduccion3=salariobase-decu3
dedut=(decu1+decu2+decu3)
decucciontotal=salariobase-dedut
asig1=salariobase+173000
asig2=salariobase+250000
asig3=salariobase+180000
asigt=(173000+250000+180000)
asignaciontotal=salariobase+asigt
salarioneto=salariobase-dedut+asigt
#Salida
print (name, "su sueldo en diciembre fue: ")
print ("Usted trabajó:",horasn,"horas normales y",horase,"horas extra dando un total de:",horastotales,"horas")
print ("Su salario base es de $",salariobase,"COP")
print ("Su salario menos el 5%, es: $",deduccion1,"COP")
print ("Su salario menos el 2%, es: $",deduccion2,"COP")
print ("Su salario menos el 7%, es: $",deduccion3,"COP")
print ("Su salario menos todas las deducciones es de: $",decucciontotal,"COP")
print ("Su salario más $ 173,000 COP es de: $",asig1,"COP")
print ("Su salario más $ 250,000 COP es de: $",asig2,"COP")
print ("Su salario más $ 180,000 COP es de: $",asig3,"COP")
print ("Su salario sumado con todas las asignaciones es de $",asignaciontotal,"COP")
print ("Su salario neto es de $:",salarioneto,"COP")
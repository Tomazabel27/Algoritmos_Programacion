#Entradas
aust= int (input("Ingrese la cantidad en chelines austríacos: "))
grieg= int (input("Ingrese la cantidad en dracmas griegos: "))
peset= int (input("Ingrese la cantidad en pesetas: "))
#Caja negra
austpeset= aust*9568.71
griegfran= grieg/22695
dolar= peset/122499
ital= peset/(9289/100)
#salida
print (aust,"cheline(s) autríaco(s) es/son:",austpeset,"peseta(s)")
print (grieg,"dracma(s) griego(s) es/son:",griegfran,"franco(s) frances(es)")
print (peset,"peseta(s) es/son:",ital,"liria(s) italiana(s)")
print (peset,"peseta(s) es/son:",dolar,"dólar(es) EEUU")
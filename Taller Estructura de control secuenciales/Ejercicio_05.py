#Entradas
cp1= int (input("Ingrese su primera calificacion parcial: "))
cp2= int (input("Ingrese su segunda calificacion parcial: "))
cp3= int (input("Ingrese su tercera calificacion parcial: "))
ef= int (input("Ingrese su calificacion del examen final: "))
tf= int (input("Ingrese su calificacion del trabajo final: "))
#Caja negra
prom= (cp1+cp2+cp3) / 3
porc1= prom*0.55
porc2= ef*0.30
porc3= tf*0.15
nf=round(porc1+porc2+porc3), 2
#Salida
print ("Su nota final es: ", nf)
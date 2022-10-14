from datetime import datetime
hoy = datetime.now()
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year
#Entradas
fecha=input("Escriba su fecha de nacimiento dd/mm/yyyy:")
(dia,mes,año)=fecha.split("/")
dian=int(dia)
mesn=int(mes)
añon=int(año)
nh=float(input("Escriba su nivel de hemoglobina en porcentaje:"))
sexo=input("Escriba su sexo:")
#Caja negra
#-------Edad---------
edad=0
if(mes_actual>mesn):
    edad=año_actual-añon
elif(mes_actual<mesn):
    edad=(año_actual-añon)-1
elif(mes_actual==mesn):
    if(dia_actual>dian):
        edad=año_actual-añon
    elif(dia_actual<dian):
        edad=(año_actual-añon)-1
    elif(dia_actual==dian):
        edad=año_actual-añon
edadm=edad*12
#--------Anemia----------
estado=""
if(edadm>=0 and edadm<=1):
    if(nh>=13 and nh<=26):
        estado="negativo"
    elif(nh<13):
        estado="positivo"
elif(edadm>1 and edadm<=6):
    if(nh>=10 and nh<=18):
        estado="negativo"
    elif(nh<10):
        estado="positivo"
elif(edadm>6 and edadm<=12):
    if(nh>=11 and nh<=15):
        estado="negativo"
    elif(nh<11):
        estado="positivo"
elif(edad>1 and edad<=5):
    if(nh>=11.5 and nh<=15):
        estado="negativo"
    elif(nh<11.5):
        estado="positivo"
elif(edad>5 and edad<=10):
    if(nh>=12.6 and nh<=15.5):
        estado="negativo"
    elif(nh<12.6):
        estado="positivo"
elif(edad>10 and edad<=15):
    if(nh>=13 and nh<=15.5):
        estado="negativo"
    elif(nh<13):
        estado="positivo"
elif(sexo=="mujer"):
    if(edad>15):
        if(nh>=12 and nh<=16):
            estado="negativo"
        elif(nh<12):
            estado="positivo"
elif(sexo=="hombre"):
    if(edad>15):
        if(nh>=14 and nh<=18):
            estado="negativo"
        elif(nh<14):
            estado="positivo"
#Salida
print("los resultados de si tiene anemia basado en algunos resultados es:",estado)
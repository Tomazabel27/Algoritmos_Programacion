#Entrada
import math
metros= int (input("Ingrese la cantidad de metros: "))
#Caja negra
inchtotal= (metros*1) / 0.0254
ft= math. trunc(inchtotal/12)
inch= (inchtotal)-12*ft
#Salida
print (metros,"metros son:", ft,"' +", inch,"''")
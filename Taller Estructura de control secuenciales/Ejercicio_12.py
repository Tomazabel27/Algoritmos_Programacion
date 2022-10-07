#Entradas matematicas
import math
nota1= int (input("Ingrese la nota de su primera tarea de matemáticas: "))
nota2= int (input("Ingrese la nota de su segunda tarea de matemáticas: "))
nota3= int (input("Ingrese la nota de su tercera tarea de matemáticas: "))
examen1= int (input("Ingrese la nota de su examen de matemáticas: "))
#caja negra matematicas
promtareasmate=(nota1+nota2+nota3) / 3
porentajetaeasmate=promtareasmate*0.1
porcentajexamenmate=examen1*0.9
promediofinalmate=porcentajexamenmate+porentajetaeasmate
#salida matematicas
print("Su promedio en matemáticas es de:",promediofinalmate)
#entradas fisica
nota4= int (input("Ingrese la nota de su primera tarea de física: "))
nota5= int (input("Ingrese la nota de su segunda tarea de física: "))
examen2= int (input("Ingrese la nota de su examen de física: "))
#caja negra física
promtareasfisic=(nota4+nota5) / 2
porentajetaeasfisic=promtareasfisic*0.2
porcentajexamenfisic=examen2*0.8
promediofinalfisic=porcentajexamenfisic+porentajetaeasfisic
#salidas fisica
print("Su promedio en física es de:",promediofinalfisic)
#entradas quimica
nota6= int (input("Ingrese la nota de su primera tarea de química: "))
nota7= int (input("Ingrese la nota de su segunda tarea de química: "))
nota8= int (input("Ingrese la nota de su tercera tarea de química: "))
examen3= int (input("Ingrese la nota de su examen de química: "))
#caja negra quimica
promtareasquim=(nota6+nota7+nota8) / 3
porentajetaeasquim=promtareasquim*0.15
porcentajexamenqui=examen3*0.85
promediofinalquim=porcentajexamenqui+porentajetaeasquim
#Salidas
print("Su promedio en química es de:",promediofinalquim)
#caja negra final
promfinal=(promediofinalmate+promediofinalfisic+promediofinalquim) / 3
#salida final
print("Su promedio final general es:",promfinal)
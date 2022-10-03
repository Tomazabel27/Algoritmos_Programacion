Algoritmo Inicio_Velocidades
	//entradas
	Escribir "Ingrese distancia"
	leer D
	Escribir "Ingrese velocidad del primer vehiculo"
	Leer v1
	Escribir "Ingrese velocidad del segundo vehiculo"
	leer v2
	//caja negra
	thoras<-D/v2
	tseg<-thoras*3600
	vmin<-trunc(tseg/60)
	vseg<-tseg mod (60)
	//salida
	Escribir "Le tomará " vmin " Minutos y " vseg " segundos en alcanzar al otro vehículo"
FinAlgoritmo

Algoritmo Inicio_Iniciales
	//entradas
	Escribir "Por favor ingresa tu nombre: "
	Leer nombre
	Escribir "Por favor ingresa tu primer apellido: "
	leer apellido1
	Escribir "por favor ingresa tu segundo apellido: "
	leer apellido2
	//caja negra
	n<-SubCadena(nombre,1,1) 
	pa<-SubCadena(apellido1,1,1) 
	sa<-SubCadena(apellido2,1,1) 
	//salida
	Escribir "Sus iniciales son: " n pa sa
FinAlgoritmo

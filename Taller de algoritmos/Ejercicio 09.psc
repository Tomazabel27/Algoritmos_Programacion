Algoritmo Inicio_Comisiones
	//entradas
	Escribir "Digite el salario base del vendedor "
	Leer salario
	escribir "Digite el valor de la primera venta "
	leer venta1
	escribir "Digite el valor de la segunda venta "
	leer venta2
	escribir "Digite el valor de la tercera venta "
	leer venta3
	//caja negra
	comision1<-venta1*0.1
	comision2<-venta2*0.1
	comision3<-venta3*0.1
	comisiontotal<-comision1+comision2+comision3
	total<-salario+comisiontotal
	//salidas
	escribir "Su salario es de: " salario " y el total de sus comisiones es: " comisiontotal " y su total de ingresos es de " total
FinAlgoritmo
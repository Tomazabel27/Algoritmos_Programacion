Algoritmo Inicio_Notas
	Escribir "Ingrese sus notas "
	Escribir "Digite las Notas parciales"
	leer Notaparcial1
	leer Notaparcial2
	Leer Notaparcial3
	Escribir "Digite la nota del examen final"
	Leer NotaExamen
	Escribir "Digite la nota del trabajo final"
	Leer NotaTrabajoFinal
	NotaParciales<-(Notaparcial1+Notaparcial2+Notaparcial3/3)*0.55
	NotaExamenF<-NotaExamen*0.30
	NotaTFinal<-NotaTrabajoFinal*0.15
	NotaFinal<-NotaParciales+NotaExamenF+NotaTFinal
	NotaFinalredon<-redon(NotaParciales+NotaExamenF+NotaTFinal)
	Escribir "El estudiante final tiene una nota final de: " NotaFinal " o " NotaFinalredon
FinAlgoritmo

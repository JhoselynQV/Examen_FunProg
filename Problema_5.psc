Algoritmo sueldo6_JNQV
    //Definicion de variables y datos de entrada
	Definir años_sueldo Como Entero
	Definir porcentaje, sueldo, sueldo_inicial Como Real
	porcentaje<-0
	sueldo_inicial<-0
	Escribir "Ingrese el sueldo"
	Leer sueldo
	Escribir "Ingrese los años de sueldo a calcular"
	Leer años_sueldo
	//Proceso y datos de saida
	sueldo_inicial=sueldo
	Para i<-1 hasta años_sueldo hacer
		porcentaje= sueldo_inicial*10/100
		sueldo_inicial=sueldo_inicial+porcentaje
		Escribir "Año: ", i
		Escribir "Aumento:", porcentaje
		Escribir "Sueldo final del Año: ", sueldo_inicial
	FinPara
	//Datos de salida
	Escribir "Los años de sueldo a calcular son:", sueldo_inicial
FinAlgoritmo
	

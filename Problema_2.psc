Algoritmo sueldopunto_JNQV
    //Definicion de variables y datos de entrada
	Definir punt Como Entero
	Definir min Como Real
	Escribir "Ingrese el sueldo minimo"
	Leer min
	Escribir "Ingrese la cantidad de puntos por desempeño"
	Leer punt
	//Proceso y datos de salida
	Si punt>=50 y punt<=100 Entonces
		salario1=(min*10/100)
		Escribir "El bono por puntos de desempeño es:",salario1
	FinSi
	Si punt>=101 y punt<=150 Entonces
		salario2=(min*50/100)
		Escribir "El bono por puntos de desempeño es:",salario2
	FinSi
	Si punt>=151 Entonces
		salario3=min
		Escribir "El bono por puntos de desempeño es:",salario3
	FinSi
FinAlgoritmo


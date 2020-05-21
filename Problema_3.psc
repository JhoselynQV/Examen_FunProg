Algoritmo vacuna_JNQV
	//Definicion de variables y datos de entrada
	Definir edad Como Entero
	Definir gen Como Caracter
	Definir F,M Como Caracter
	Escribir "Ingresa tu edad"
	Leer edad
	Escribir "Escribe tu genéro"
	Leer gen
	//Proceso y datos de salida
	Si edad<=15 Entonces
		Escribir "La vacuna que necesitas es:A"
	FinSi
	Si edad>=16 y edad<=69 Entonces
		Si gen=='M' 
			Escribir "La vacuna que necesitas es:A"	
		SiNo
			Escribir "La vacuna que necesitas es:B"
		FinSi
	FinSi
	Si edad>70 Entonces
		Escribir "La vacuna que necesitas es:C"
	FinSi
FinAlgoritmo


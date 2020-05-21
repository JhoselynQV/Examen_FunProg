Algoritmo calculadora_JNQV
    //Definicion de variables y datos de entrada
	Definir num1,num2 Como Real
	num1=0
	num2=0
	menu=0
	Escribir "Ingrese el primer numero"
	Leer num1
	Escribir "Ingrese el segundo numero"
	Leer num2
	Escribir "Menu de procesos"
	Escribir "(1) suma"
	Escribir "(2) resta"
	Escribir "(3) multiplicacion"
	Escribir "(4) división"
	Escribir "(5) potencia"
	Leer menu;
	//Proceso y datos de salida
	Segun menu hacer
		1: r1=num1+num2
			Escribir "El resultado de la suma es:",r1
		2: r2=num1-num2
			Escribir "El resultado de la resta es:",r2
		3: r3=num1*num2
			Escribir "El resultado de la multiplicaion es:",r3
		4: r4=num1/num2
			Escribir "El resultado de la division es:",r4
		5: r5=num1^num2
			Escribir "El resultado de la potencia es:",r5
		De Otro modo:
			Escribir "Syntax ERROR"
	FinSegun
FinAlgoritmo
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definicion de variables y datos de entrada
	num1 = float()
	num2 = float()
	num1 = 0
	num2 = 0
	menu = 0
	print("Ingrese el primer numero")
	num1 = float(input())
	print("Ingrese el segundo numero")
	num2 = float(input())
	print("Menu de procesos")
	print("(1) suma")
	print("(2) resta")
	print("(3) multiplicacion")
	print("(4) división")
	print("(5) potencia")
	menu = float(input())
	# Proceso y datos de salida
	if menu==1:
		r1 = num1+num2
		print("El resultado de la suma es:",r1)
	elif menu==2:
		r2 = num1-num2
		print("El resultado de la resta es:",r2)
	elif menu==3:
		r3 = num1*num2
		print("El resultado de la multiplicaion es:",r3)
	elif menu==4:
		r4 = num1/num2
		print("El resultado de la division es:",r4)
	elif menu==5:
		r5 = num1**num2
		print("El resultado de la potencia es:",r5)
	else:
		print("Syntax ERROR")


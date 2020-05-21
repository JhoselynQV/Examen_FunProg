# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definicion de variables y datos de entrada
	punt = int()
	min = float()
	print "Ingrese el sueldo minimo"
	min = float(raw_input())
	print "Ingrese la cantidad de puntos por desempeño"
	punt = int(raw_input())
	# Proceso y datos de salida
	if punt>=50 and punt<=100:
		salario1 = (min*10/100)
		print "El bono por puntos de desempeño es:",salario1
	if punt>=101 and punt<=150:
		salario2 = (min*50/100)
		print "El bono por puntos de desempeño es:",salario2
	if punt>=151:
		salario3 = min
		print "El bono por puntos de desempeño es:",salario3


# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definicion de variables y datos de entrada
	not1 = float()
	not2 = float()
	not3 = float()
	not4 = float()
	und1 = float()
	und2 = float()
	und3 = float()
	und4 = float()
	suma = float()
	print("Ingresa la nota de la unidad 1")
	not1 = float(input())
	print("Ingrese la nota de la unidad 2")
	not2 = float(input())
	print("Ingrese la nota de la unidad 3")
	not3 = float(input())
	print("Ingrese la nota de la unidad 4")
	not4 = float(input())
	# Proceso y datos de salida
	und1 = (not1*10/100)
	und2 = (not2*15/100)
	und3 = (not3*25/100)
	und4 = (not4*50/100)
	final = (und1+und2+und3+und4)
	# Datos de salida
	print("La nota final es:",final)


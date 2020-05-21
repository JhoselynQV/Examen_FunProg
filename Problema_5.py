# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definicion de variables y datos de entrada
	anos_sueldo = int()
	porcentaje = float()
	sueldo = float()
	sueldo_inicial = float()
	porcentaje = 0
	sueldo_inicial = 0
	print("Ingrese el sueldo")
	sueldo = float(input())
	print("Ingrese los años de sueldo a calcular")
	anos_sueldo = int(input())
	# Proceso y datos de saida
	sueldo_inicial = sueldo
	for i in range(1,anos_sueldo+1):
		porcentaje = sueldo_inicial*10/100
		sueldo_inicial = sueldo_inicial+porcentaje
		print("Año: ",i)
		print("Aumento:",porcentaje)
		print("Sueldo final del Año: ",sueldo_inicial)
	# Datos de salida
	print("Los años de sueldo a calcular son:",sueldo_inicial)


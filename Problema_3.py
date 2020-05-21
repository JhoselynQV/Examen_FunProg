# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definicion de variables y datos de entrada
	edad = int()
	gen = str()
	f = str()
	m = str()
	print("Ingresa tu edad")
	edad = int(input())
	print("Escribe tu genéro")
	gen = input()
	# Proceso y datos de salida
	if edad<=15:
		print("La vacuna que necesitas es:A")
	if edad>=16 and edad<=69:
		if gen=="M":
			print("La vacuna que necesitas es:A")
		else:
			print("La vacuna que necesitas es:B")
	if edad>70:
		print("La vacuna que necesitas es:C")


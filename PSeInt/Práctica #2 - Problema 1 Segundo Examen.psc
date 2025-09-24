Algoritmo Problema_1_Segundo_Examen
	Leer Frec, Value, Tipo
	w = 2 * PI * Frec
	n = 50
	Mientras n <> 0 Hacer
		Si Tipo = "C" Entonces
			Zreal = 0
			Zimag = -1 / (w * Value)
		SiNo
			Si Tipo = "L" Entonces
				Zreal = 0
				Zimag = w * Value
			SiNo
				Zreal = Value
				Zimag = 0
			FinSi
		FinSi
		Escribir Zreal,Zimag
		Leer Value, Tipo
		n = n - 1
	FinMientras
FinAlgoritmo


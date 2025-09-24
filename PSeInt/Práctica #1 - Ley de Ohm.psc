Algoritmo Ley_de_Ohm
	rep = ""
	Mientras rep <> "salir" Hacer
		Leer I,V,R
		Si I == 0 Entonces
			Resultado = V/R
			Unidad = "Amperes"
		SiNo
			Si V == 0 Entonces
				Resultado = I * R
				Unidad = "Voltios"
			SiNo
				Resultado = V/I
				Unidad = "Ohms"
			FinSi
		FinSi
		Escribir Resultado, Unidad
		Leer rep
	FinMientras
FinAlgoritmo

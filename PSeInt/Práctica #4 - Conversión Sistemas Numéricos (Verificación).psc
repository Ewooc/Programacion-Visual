Algoritmo Verificación
	Leer ValorEntrada, SistemaEntrada, SistemaSalida
	
	Si ValorEntrada = "" // Valor vacío
		Escribir "Valor no ingresado"
	SiNo
		Si SistemaEntrada = "Binario"
			Si ValorEntrada no es Binario
				Escribir "Valor no es binario"
			FinSi
		SiNo
			Si SistemaEntrada = "Octal"
				Si ValorEntrada no es Octal
					Escribir "Valor no es octal"
				FinSi
			SiNo			
				Si SistemaEntrada = "Hexadecimal"
					Si ValorEntrada no es Hexadecimal
						Escribir "Valor no es hexadecimal"
					FinSi
				SiNo
					Si ValorEntrada no es Decimal
						Escribir "Valor no es decimal"
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo


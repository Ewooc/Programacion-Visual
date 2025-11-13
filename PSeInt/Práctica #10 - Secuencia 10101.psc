Algoritmo Secuencia_10101
	Estado <- "A"
	Mientras Estado <> "F" Hacer // Si todavía no acaba
		
		Mientras Estado = "A" Hacer /// Estado A
			Leer Dígito
			Si Dígito = 1 Entonces
				Estado <- "B" // Pasar al Estado B
			SiNo
				// Permanecer en Estado A
			FinSi
		FinMientras
		
		Mientras Estado = "B" Hacer /// Estado B
			Leer Dígito
			Si Dígito = 0 Entonces
				Estado <- "C" // Pasar al Estado C
			SiNo
				// Permanecer en Estado B
			FinSi
		FinMientras
		
		Mientras Estado = "C" Hacer /// Estado C
			Leer Dígito
			Si Dígito = 1 Entonces
				Estado <- "D" // Pasar al Estado D
			SiNo
				Estado <- "A" // Regresar al Estado A
			FinSi
		FinMientras
		
		Mientras Estado = "D" Hacer /// Estado D
			Leer Dígito
			Si Dígito = 0 Entonces
				Estado <- "E" // Pasar al Estado E
			SiNo
				Estado <- "B" // Regresar al Estado B
			FinSi
		FinMientras
		
		Mientras Estado = "E" Hacer /// Estado E
			Leer Dígito
			Si Dígito = 1 Entonces
				Estado <- "F" // Llegar al Último Estado
			SiNo
				Estado <- "A" // Regresar al Estado A
			FinSi
		FinMientras
		
	FinMientras // Ya acabó la secuencia
	
	Escribir "Secuencia 1-0-1-0-1 Detectada"
FinAlgoritmo

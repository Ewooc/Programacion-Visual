Algoritmo Verificación
	Leer ValorDetectado // Binario a 8 bits
	
	Si ValorDetectado > 0 Entonces
		
		Si ValorDetectado < 255 Entonces
			
			Si ValorDetectado es Binario Entonces
				// Cumple con la verificación
				Escribir "Valor permitido"
				
			SiNo
				Escribir "No es Binario"
			FinSi
			
		SiNo
			Escribir "No se puede mayor a 255"
		FinSi
		
	SiNo
		Escribir "No se puede menor a 0"
	FinSi

FinAlgoritmo


Algoritmo Verificación_Instrucciones
	Leer Instrucción
	Si Instrucción es Binario Entonces
		Si Dígitos_Instrucción = 8 Entonces // Binario de 8 dígitos
			Si PC > 8 Entonces
				Escribir "Límite de Instrucciones alcanzado"
			SiNo
				// Pasa la verificación
			FinSi
		SiNo
			Escribir "Instrucción inválida"
		FinSi
	SiNo
		Escribir "Instrucción no es Binario"
	FinSi
FinAlgoritmo


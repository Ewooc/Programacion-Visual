Algoritmo Procesador_B�sico
	Acc <- 0
	B <- 0
	PC <- 0
	RI <- 0
	Mientras PC < 8 Hacer
		Leer Instrucci�n
		RI <- Instrucci�n // Pasa al registro de instrucciones
		M <- Dato_Instrucci�n // Pasa los �ltimos 6 d�gitos binarios
		Si Operaci�n_Instrucci�n = "01" Entonces
			Acc <- M // Pasa el valor de memoria al acumulador
		SiNo
			Si Operaci�n_Instrucci�n = "10" Entonces
				B <- Acc // Transfiere el valor del acumulador al registro B
			SiNo
				Si Operaci�n_Instrucci�n = "11" Entonces
					Acc <- Acc + B // Suma los valores del acumulador y del registro B
				SiNo // Operaci�n_Instrucci�n = "00"
					// No hacer nada
				FinSi
			FinSi
		FinSi
		Escribir PC, RI, Acc, B
		PC <- PC + 1 // Aumenta en 1 el contador del programa
	FinMientras
FinAlgoritmo


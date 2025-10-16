Algoritmo Procesador_Básico
	Acc <- 0
	B <- 0
	PC <- 0
	RI <- 0
	Mientras PC < 8 Hacer
		Leer Instrucción
		RI <- Instrucción // Pasa al registro de instrucciones
		M <- Dato_Instrucción // Pasa los últimos 6 dígitos binarios
		Si Operación_Instrucción = "01" Entonces
			Acc <- M // Pasa el valor de memoria al acumulador
		SiNo
			Si Operación_Instrucción = "10" Entonces
				B <- Acc // Transfiere el valor del acumulador al registro B
			SiNo
				Si Operación_Instrucción = "11" Entonces
					Acc <- Acc + B // Suma los valores del acumulador y del registro B
				SiNo // Operación_Instrucción = "00"
					// No hacer nada
				FinSi
			FinSi
		FinSi
		Escribir PC, RI, Acc, B
		PC <- PC + 1 // Aumenta en 1 el contador del programa
	FinMientras
FinAlgoritmo


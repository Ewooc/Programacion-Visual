Algoritmo Conversión
	Leer ValorEntrada, SistemaEntrada, SistemaSalida
	ValorIngresado <- Dec*(ValorEntrada) // Pasar a decimal el valor inicial
	// Hacer la conversión independientemente del sistema de entrada y salida

	Si SistemaSalida = "Binario"
		ValorConvertido <- Bin*(ValorIngresado)
		// Convierte el valor a binario
	SiNo
		Si SistemaSalida = "Octal"
			ValorConvertido <- Oct*(ValorIngresado)
			// Convierte el valor a octal
		SiNo
			Si SistemaSalida = "Hexadecimal"
				ValorConvertido <- Hex*(ValorIngresado)
				// Convierte el valor a hexadecimal
			SiNo
				Si SistemaSalida = "BCD"
					ValorConvertido <- BCD*(ValorIngresado)
					// Convierte el valor a bcd
				SiNo
					ValorConvertido <- ValorIngresado
					// Dejar el valor en decimal
				FinSi
			FinSi
		FinSi
	FinSi
	
	Escribir ValorConvertido
FinAlgoritmo



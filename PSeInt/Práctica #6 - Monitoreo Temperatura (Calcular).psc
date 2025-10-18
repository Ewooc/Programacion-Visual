Algoritmo Monitoreo_Temperatura
	suma <- 0
	contador <- 1
	TemperaturaMAX <- 0
	TemperaturaMin <- 999999
	
	Mientras contador <> 17 Hacer // 16 Registros por día
		
		Leer ValorDetectado // Binario a 8 bits
		ValorSeñal <-  Decimal_ValorDetectado // Convertir a decimal
		ValorTemperatura <- (ValorSeñal * 100) / 255 // Regla de 3
		
		suma <- suma + ValorTemperatura // Agregar a la suma
		TemperaturaProm <- suma / contador // Calcular promedio
		
		Si ValorTemperatura > TemperaturaMAX Entonces // Máximo
			TemperaturaMAX <- ValorTemperatura
		FinSi
		
		Si ValorTemperatura < TemperaturaMin Entonces // Mínimo
			TemperaturaMin <- ValorTemperatura
		FinSi
		
		Escribir TemperaturaProm, TemperaturaMAX, TemperaturaMin
		contador <- contador + 1
		
	FinMientras
FinAlgoritmo


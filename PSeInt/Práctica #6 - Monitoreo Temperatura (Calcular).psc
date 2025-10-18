Algoritmo Monitoreo_Temperatura
	suma <- 0
	contador <- 1
	TemperaturaMAX <- 0
	TemperaturaMin <- 999999
	
	Mientras contador <> 17 Hacer // 16 Registros por d�a
		
		Leer ValorDetectado // Binario a 8 bits
		ValorSe�al <-  Decimal_ValorDetectado // Convertir a decimal
		ValorTemperatura <- (ValorSe�al * 100) / 255 // Regla de 3
		
		suma <- suma + ValorTemperatura // Agregar a la suma
		TemperaturaProm <- suma / contador // Calcular promedio
		
		Si ValorTemperatura > TemperaturaMAX Entonces // M�ximo
			TemperaturaMAX <- ValorTemperatura
		FinSi
		
		Si ValorTemperatura < TemperaturaMin Entonces // M�nimo
			TemperaturaMin <- ValorTemperatura
		FinSi
		
		Escribir TemperaturaProm, TemperaturaMAX, TemperaturaMin
		contador <- contador + 1
		
	FinMientras
FinAlgoritmo


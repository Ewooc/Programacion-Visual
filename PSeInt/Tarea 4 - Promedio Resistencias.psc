Algoritmo Promedio_Resistencias
	
	Dimension Comercial[14] // Lista de Resistencias Comerciales
	Comercial[1] <- 1.0 
	Comercial[2] <- 1.2
	Comercial[3] <- 1.5
	Comercial[4] <- 1.8
	Comercial[5] <- 2.2
	Comercial[6] <- 2.7
	Comercial[7] <- 3.3
	Comercial[8] <- 3.9
	Comercial[9] <- 4.7
	Comercial[10] <- 5.6
	Comercial[11] <- 6.8
	Comercial[12] <- 8.2
	Comercial[13] <- 9.1
	Comercial[14] <- 10
	
	Leer res // Inicio de lectura
	
	Mientras res <> "exit" Hacer // Ciclo
		
		Si res = "restart" Entonces // Reinicia valores
			div <- 0
			suma <- 0
			prom <- 0
			Escribir "Valores Reiniciados"
			
		SiNo
			suma <- suma + ConvertirANumero(res) // Calcular Promedio
			div <- div + 1
			prom <- suma / div
			
			expo <- 0
			Mientras prom >= 10 Hacer // Disminuye promedio para valores entre 1 a 10
				prom <- prom / 10
				expo <- expo + 1 // Grado de exponente (x10)
			Fin Mientras
			
			n <- 1
			Mientras Comercial[n] < prom Hacer // Verificar Resistencia Comercial más cercana
				n <- n + 1
			Fin Mientras
			
			Si expo < 3 Entonces // Resistencias menores a 1K 
				resistencia <- prom * 10 ^ expo // Regresa valor inicial
				comercio <- Comercial[n] * 10 ^ expo
				Escribir "Resistencia: " resistencia " Ohms"
				Escribir "Comercial: " comercio " Ohms"
				
			SiNo
				Si expo < 6 Entonces // Resistencias entre 1K y 1M
					expo <- expo - 3 // Elimina Kilo del número
					resistencia <- prom * 10 ^ expo
					comercio <- Comercial[n] * 10 ^ expo
					Escribir "Resistencia: " resistencia " Kilo Ohms"
					Escribir "Comercial: " comercio " Kilo Ohms"
					
				SiNo // Resistencias mayores a 1M
					expo <- expo - 6 // Elimina Mega del número
					resistencia <- prom * 10 ^ expo
					comercio <- Comercial[n] * 10 ^ expo
					Escribir "Resistencia: " resistencia " Mega Ohms"
					Escribir "Comercial: " comercio " Mega Ohms"
					
				Fin Si
			Fin Si
		Fin Si
		
		Leer res // Solicita nueva resistencia para agregar
		
	Fin Mientras
FinAlgoritmo


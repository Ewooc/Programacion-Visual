Algoritmo Simulador
	Leer Voltaje, ResistenciaFocos, CantidadFocos, Material, Conexi�n
	Mientras Voltaje <> 0 Hacer
		
		// Algoritmo Comprobar_Material
		Si Material = "Plata" Entonces
			Rmaterial <- 0.8
		SiNo
			Si Material = "Acero" Entonces
				Rmaterial <- 5
			SiNo // Por defecto: "Cobre"
				Rmaterial <- 1
			FinSi
		FinSi
		
		// Algoritmo Comprobar_Conexi�n
		Si Conexi�n = "paralelo" Entonces
			Req <- (ResistenciaFocos / CantidadFocos) + Rmaterial
		SiNo // Por defecto: "serie"
			Req <- (ResistenciaFocos * CantidadFocos) + Rmaterial
		FinSi
		
		// Calcular Corriente total
		CorrienteI <- Voltaje / Req
		Escribir CorrienteI
		Leer Voltaje, ResistenciaFocos, CantidadFocos, Material, Conexi�n
		
	FinMientras
FinAlgoritmo


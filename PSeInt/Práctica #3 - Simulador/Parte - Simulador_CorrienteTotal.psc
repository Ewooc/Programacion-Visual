Algoritmo Simulador_CorrienteTotal
	Leer Voltaje, ResistenciaFocos, CantidadFocos, Material, Conexi�n
	Mientras Voltaje <> 0 Hacer
		// Algoritmo Comprobar_Material()
		// Algoritmo Comprobar_Conexi�n()
		CorrienteI <- Voltaje / Req
		Escribir CorrienteI
		Leer Voltaje, ResistenciaFocos, CantidadFocos, Material, Conexi�n
	FinMientras
FinAlgoritmo

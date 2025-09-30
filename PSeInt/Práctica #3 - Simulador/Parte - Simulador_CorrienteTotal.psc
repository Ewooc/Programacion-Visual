Algoritmo Simulador_CorrienteTotal
	Leer Voltaje, ResistenciaFocos, CantidadFocos, Material, Conexión
	Mientras Voltaje <> 0 Hacer
		// Algoritmo Comprobar_Material()
		// Algoritmo Comprobar_Conexión()
		CorrienteI <- Voltaje / Req
		Escribir CorrienteI
		Leer Voltaje, ResistenciaFocos, CantidadFocos, Material, Conexión
	FinMientras
FinAlgoritmo

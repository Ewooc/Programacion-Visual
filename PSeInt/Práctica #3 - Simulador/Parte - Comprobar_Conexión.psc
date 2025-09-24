Algoritmo Comprobar_Conexión
	Si Conexión = "paralelo" Entonces
		Req <- (ResistenciaFocos / CantidadFocos) + Rmaterial
	SiNo // Por defecto: "serie"
		Req <- (ResistenciaFocos * CantidadFocos) + Rmaterial
	FinSi
FinAlgoritmo

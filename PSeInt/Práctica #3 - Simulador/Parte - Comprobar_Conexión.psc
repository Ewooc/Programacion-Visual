Algoritmo Comprobar_Conexi�n
	Si Conexi�n = "paralelo" Entonces
		Req <- (ResistenciaFocos / CantidadFocos) + Rmaterial
	SiNo // Por defecto: "serie"
		Req <- (ResistenciaFocos * CantidadFocos) + Rmaterial
	FinSi
FinAlgoritmo

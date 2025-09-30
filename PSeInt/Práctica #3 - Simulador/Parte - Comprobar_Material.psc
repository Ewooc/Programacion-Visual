Algoritmo Comprobar_Material
	Si Material = "Plata" Entonces
		Rmaterial <- 1.55
	SiNo
		Si Material = "Acero" Entonces
			Rmaterial <- 72
		SiNo // Por defecto: "Cobre"
			Rmaterial <- 1.77
		FinSi
	FinSi
FinAlgoritmo

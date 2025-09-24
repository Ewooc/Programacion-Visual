Algoritmo Comprobar_Material
	Si Material = "Plata" Entonces
		Rmaterial <- 0.8
	SiNo
		Si Material = "Acero" Entonces
			Rmaterial <- 5
		SiNo // Por defecto: "Cobre"
			Rmaterial <- 1
		FinSi
	FinSi
FinAlgoritmo

Algoritmo Materiales_Semiconductores
	Lista <- InfoMateriales // Generar lista de los materiales disponibles
	Leer Material
	
	Si Material Pertenece A Lista_InfoMateriales
		Escribir Nombre, Símbolo, Z, Valencia, Tipo, Aplicaciones
		
	SiNo
		Escribir "El material no forma parte de la lista"
		
	FinSi
	
FinAlgoritmo



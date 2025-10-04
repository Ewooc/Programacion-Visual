Algoritmo Resistencia_Alambre
	Leer M, L, C
	P <- M * 10^(-8) // Obtener Resistividad
	A <- PI * ( C/2000 )^2 // Obtener Área
	R <- P * (L/A) // Calcular Resistencia
	Escribir R
FinAlgoritmo


Algoritmo Divisor_Voltaje
	Leer IDSS , VP , VDD , R1 , R2 , RD , RS
	
	// Calcular constantes 'l' y 'm'
	l <- (VP^2) / (2*RS*IDSS)
	m <- 2 * ( (R2/(R1+R2)) * VDD - VP )
	
	// Calcular VGSQ e IDQ
	VGSQ <- VP - l + raiz( l^2 + l * m )
	IDQ <- IDSS * ( 1 - (VGSQ/VP) )^2
	
	Escribir IDQ , VGSQ
FinAlgoritmo

Algoritmo Verificaci�n_Instrucciones
	Leer Instrucci�n
	Si Instrucci�n es Binario Entonces
		Si D�gitos_Instrucci�n = 8 Entonces // Binario de 8 d�gitos
			Si PC > 8 Entonces
				Escribir "L�mite de Instrucciones alcanzado"
			SiNo
				// Pasa la verificaci�n
			FinSi
		SiNo
			Escribir "Instrucci�n inv�lida"
		FinSi
	SiNo
		Escribir "Instrucci�n no es Binario"
	FinSi
FinAlgoritmo


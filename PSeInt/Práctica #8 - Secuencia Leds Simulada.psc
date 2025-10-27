Algoritmo Secuencia_Leds
	secuencia = 0
	Mientras secuencia < 10 Hacer
		Leer Instrucción /// 3 caracteres, separados A-B-C
		// Apagar todos los focos para después comprobar
		FocoA = "Apagado"
		FocoB = "Apagado"
		FocoC = "Apagado"
		// Verificar si se tiene que encender algún foco
		Si Instrucción_A = "1" Entonces /// Primer caracter
			FocoA = "Encendido"
		FinSi
		Si Instrucción_B = "1" Entonces /// Segundo caracter
			FocoB = "Encendido"
		FinSi
		Si Instrucción_C = "1" Entonces /// Tercer caracter
			FocoC = "Encendido"
		FinSi
		
		Mostrar FocoA, FocoB, FocoC
		secuencia = secuencia + 1
		
	FinMientras
FinAlgoritmo

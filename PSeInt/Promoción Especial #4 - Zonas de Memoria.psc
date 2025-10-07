Algoritmo Zonas_de_Memoria
	Leer Tama�oROM, Tama�oLibre, Tama�oRAM
	
	Posici�nROM <- Algoritmo_Hex*(Tama�oROM) // Pasar a hexadecimal
	Posici�nLibre <- Algoritmo_Hex*(Tama�oLibre) // Pasar a hexadecimal
	Posici�nRAM <- Algoritmo_Hex*(Tama�oRAM) // Pasar a hexadecimal
	
	InicioROM <- "000000" // Valor independiente
	FinRom <- Posici�nROM - 1
	InicioLibre <- Posici�nROM
	FinLibre <- Posici�nROM + Posici�nLibre - 1
	InicioRAM <- Posici�nROM + Posici�nLibre
	FinRAM <- Posici�nROM + Posici�nLibre + Posici�nRAM
	
	Escribir InicioROM," ROM ",FinRAM
	Escribir InicioLibre, " Espacio Libre ", FinLibre
	Escribir InicioRAM," RAM ",FinRAM
	
FinAlgoritmo





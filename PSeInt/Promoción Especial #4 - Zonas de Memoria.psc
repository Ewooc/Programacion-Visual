Algoritmo Zonas_de_Memoria
	Leer TamañoROM, TamañoLibre, TamañoRAM
	
	PosiciónROM <- Algoritmo_Hex*(TamañoROM) // Pasar a hexadecimal
	PosiciónLibre <- Algoritmo_Hex*(TamañoLibre) // Pasar a hexadecimal
	PosiciónRAM <- Algoritmo_Hex*(TamañoRAM) // Pasar a hexadecimal
	
	InicioROM <- "000000" // Valor independiente
	FinRom <- PosiciónROM - 1
	InicioLibre <- PosiciónROM
	FinLibre <- PosiciónROM + PosiciónLibre - 1
	InicioRAM <- PosiciónROM + PosiciónLibre
	FinRAM <- PosiciónROM + PosiciónLibre + PosiciónRAM
	
	Escribir InicioROM," ROM ",FinRAM
	Escribir InicioLibre, " Espacio Libre ", FinLibre
	Escribir InicioRAM," RAM ",FinRAM
	
FinAlgoritmo





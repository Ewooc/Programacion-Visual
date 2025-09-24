##### Lista de Resistencias Comerciales
Comercial = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 9.1, 10]

##### Función Calcular Resultado
def Calcular_Resultado():
    resistencia = prom * (10 ** expo)
    comercio = Comercial[n] * (10 ** expo)
    print("Resistencia: "+str(resistencia)+" "+str(Ohm))
    print("Comercial: "+str(comercio)+" "+str(Ohm))

##### Definir valores
div = 0
suma = 0
prom = 0

print("")
res = input("Ingrese Resistencia: ") # Inicio de Lectura

##### Ciclo
while res != "exit":
	
    if res == "restart": # Reiniciar valores
        div = 0
        suma = 0
        prom = 0
        print("Valores Reiniciados")

    ##### Proceso
    else:
        suma = suma + float(res)
        div = div + 1
        prom = suma / div # Promedio
		
        expo = 0
        while prom >= 10: # Disminuye promedio para valores entre 1 a 10
            prom = prom / 10
            expo = expo + 1 # Grado de exponente (x10)
        
        n = 1
        while Comercial[n] < prom: # Verificar Resistencia comercial más cercana
            n = n + 1

        if expo < 3: # Resistencias menores a 1K
            Ohm = "Ω"
            Calcular_Resultado()

        elif expo < 6: # Resistencias entre 1K y 1M
            expo = expo - 3 # Elimina Kilo del número
            Ohm = "KΩ"
            Calcular_Resultado()

        else: # Resistencias mayores a 1M
            expo = expo - 6 # Elimina Mega del número
            Ohm = "MΩ"
            Calcular_Resultado()
    
    res = input("Ingrese Resistencia: ") # Solicita nueva resistencia para agregar

print("Fin")



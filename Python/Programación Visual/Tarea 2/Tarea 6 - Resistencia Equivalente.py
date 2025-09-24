def Determinar_Prefijo():
    if Eq < 1e3: ##### Menor a 1000 (1K)
        Req = Eq
        pref = "Ω"
    elif Eq < 1e6: ### Entre 1K y 1M
        Req = Eq / 1e3
        pref = "KΩ"
    else: ############ Mayor a 1M
        Req = Eq / 1e6
        pref = "MΩ"
    print("Equivalente: "+f"{Req:3.2f}"+" "+str(pref))

print("") ##### Inicio del Programa #####

n = 1  # Se inicia a enumerar las resistencias
R = float(input("Valor Resistencia #"+str(n)+": ")) # Primera Resistencia
Eq = R # Se guarda el primer valor
n += 1
R = float(input("Valor Resistencia #"+str(n)+": ")) # Segunda Resistencia
C = input("Conexión serie (s), paralelo (p): ") # Tipo de conexión

while R != 0: # Ciclo para calcular Equivalente
    if C == "s": ### Conexión en Serie
        Eq = Eq + R
        n += 1
        Determinar_Prefijo()
    elif C == "p": # Conexión en Paralelo
        Eq = 1 / ( (1/Eq) + (1/R) )
        n += 1
        Determinar_Prefijo()
    else: ########## Conexión no válida
        print("Opción no válida")  
    R = float(input("Valor Resistencia #"+str(n)+": ")) # Siguiente Resistencia
    C = input("Conexión serie (s), paralelo (p): ") # Tipo de conexión

print("Fin")


###################################
###     ###     #####   ###     ###
##### ##### #######  ######## #####
##### #####    ######  ###### #####
##### ##### ##########  ##### #####
##### #####     ###    ###### #####
###################################

import math

def Calcular_Impedancia():
    comp = input("Componente (R) (C) (L): ")
    if comp == "C": # Componente Capacitor
        return complex(0, -1 / (w * val))
    elif comp == "L": # Componente Inductor
        return complex(0, w * val)
    else: # Componente Resistencia (Default)
       return complex(val, 0)


def Determinar_Prefijo(valor: complex):
    if valor.real < 1e3: ##### Menor a 1000 (1K)
        Zeq_raea = valor
        pref = "Ω"
    elif valor.real < 1e6: ### Entre 1K y 1M
        Zeq = valor / 1e3
        pref = "KΩ"
    else: ############ Mayor a 1M
        Zeq = valor / 1e6
        pref = "MΩ"
    return f"{Zeq:10.2f}{pref}" # esto es como "102.12MΩ"


print("") ##### Inicio del Programa #####

f = float(input("Frecuencia del Circuito: ")) # Frecuencia en Hz
w = 2*(math.pi)*f # Calcular Frecuencia angular

n = 1  # Se inicia a enumerar los componentes
val = float(input("Valor Componente #"+str(n)+": ")) # Primer Componente
Eq = Calcular_Impedancia() # Asigna directamente el primer valor

n += 1
val = float(input("Valor Componente #"+str(n)+": ")) # Segundo Componente

while val != 0: # Ciclo para calcular Equivalente
    Z = Calcular_Impedancia()

    conex = str(input("Conexión serie (s), paralelo (p): "))

    if conex == "p": # Conexión en Paralelo
        Eq = 1 / ( (1/Eq) + (1/Z) )

    else: # Conexión en Serie (Default)
        Eq = Eq + Z
        
    print(f"{Determinar_Prefijo(Eq.real)} + {Determinar_Prefijo(Eq.imag)}i")
    n += 1
    val = float(input("Valor Componente #"+str(n)+": ")) # Siguiente Componente

print("Fin")


import math

def Mostrar_Resultado(num_complejo: complex):
    modulo = math.sqrt((num_complejo.real ** 2) + (num_complejo.imag ** 2)) # Obtiene el módulo del número complejo

    if num_complejo.real == 0: # Cuando no haya componente real, asignar 90°
        fase = 90
    else:
        fase = math.degrees(math.atan(num_complejo.imag / num_complejo.real)) # Desfase (en grados) del número complejo

    if modulo < 1e3: # Menor a 1K
        pref = "Ω"
    elif modulo < 1e6: # Entre 1K a 1M
        modulo = modulo / 1e3
        pref = "KΩ"
    else: # Mayor a 1M
        modulo = modulo / 1e6
        pref = "MΩ"

    print(f"   Impedancia: {modulo:.2f} ({fase:.2f}°) {pref}") # Imprime resultado de la forma " 12.34 (56°) Ω "


def Calcular_Impedancia(frec_angular: float, valor: float):
    componente = input("Componente (R) (C) (L): ") # Ingresar tipo de componente
    
    if componente == "C": # Componente Capacitor
        return complex(0, -1 / (frec_angular * valor))
    elif componente == "L": # Componente Inductor
        return complex(0, frec_angular * valor)
    else: # Componente Resistencia (Default)
       return complex(valor, 0)


print("") ##### Inicio del Programa #####

f = float(input("Frecuencia del Circuito: ")) # Frecuencia en Hz
w = 2 * math.pi * f # Calcular Frecuencia angular

n = 1  # Se inicia a enumerar los componentes
valor = float(input(f"Valor Componente #{n}: ")) # Primer Componente
Zeq = Calcular_Impedancia(w, valor) # Asigna directamente el primer valor

n += 1
valor = float(input(f"Valor Componente #{n}: ")) # Segundo Componente

while valor != 0:
    Z = Calcular_Impedancia(w, valor) # Valor de Impedancia agregado
    conexion = input("Conexión serie (S), paralelo (P): ")

    if conexion == "P": # Conexión en Paralelo
        Zeq = 1 / ((1 / Zeq) + (1 / Z))
    else: # Conexión en Serie (Default)
        Zeq = Zeq + Z
    
    Mostrar_Resultado(Zeq)
    n += 1
    valor = float(input(f"Valor Componente #{n}: ")) # Siguiente Componente

print("Fin")


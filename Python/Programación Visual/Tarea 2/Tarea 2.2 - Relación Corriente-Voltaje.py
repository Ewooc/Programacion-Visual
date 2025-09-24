# - Variables
Is   = float(input("Corriente de saturación Is [A]: "))
n    = float(input("Factor de idealidad n  [-]: "))
T    = float(input("Temperatura T [K]: "))
Vmin = float(input("Voltaje mínimo Vmin [V]: "))
Vmax = float(input("Voltaje máximo Vmax [V]: "))
N    = int(input("Cantidad de valores N: "))

# - Constantes
k = 1.380649e-23   # J/K
q = 1.602176634e-19 # C
Vt = k * T / q     # voltaje térmico
e = 2.718281828459045 # Euler

# - Generar Tabla
dif = float((Vmax-Vmin)/N)
for i in range(N+1):
    V = (Vmin+(dif*i))
    I = Is * (e**(V / (n * Vt)) - 1)
    print(f"{V:10.6f} {I:15.6e}")
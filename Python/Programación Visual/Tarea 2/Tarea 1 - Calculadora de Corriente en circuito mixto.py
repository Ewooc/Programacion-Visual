###### Input
input("Calculadora de Corriente (I) en circuito mixto   ")
input("No se admite una corriente total menor a 1 mA ni mayor a 50 mA   ")
vt = float(input("Voltaje (V): "))
r1 = float(input("Resistencia 1 (kΩ): "))
r2 = float(input("Resistencia 2 (kΩ): "))
r3 = float(input("Resistencia 3 (kΩ): "))

###### Operaciones
r4 = float(1/((1/r2)+(1/r3))) # Resistencia 2 y 3
rt = float(r4+r1) # Resistencia Total
it = float(vt/rt) # Corriente Total

i1 = float(it) # Intensidad 1
v4 = float(r4*it) # Voltaje 2 y 3
i2 = float(v4/r2) # Intensidad 2
i3 = float(v4/r3) # Intensidad 3

###### Resultados
if it < 1:
    print("Corriente insuficiente (Itotal = "+str(it)+" mA), intente de nuevo")

elif it > 50:
    print("Exceso de corriente (Itotal = "+str(it)+" mA), intente de nuevo")

else:
    print("Los valores para las corrientes son...")
    print("I1 = "+str(i1)+" mA")
    print("I2 = "+str(i2)+" mA")
    print("I3 = "+str(i3)+" mA")
    print("Itotal = "+str(it)+" mA")
p = 0
s = 1
k = 9e9
n = int(input("Número de Cargas: "))
while n > 0 :
    q = float(input("Valor de carga "+str(s)+" [C]: "))
    x = float(input("Coordenada en x: "))
    y = float(input("Coordenada en y: "))
    r = float((x**2+y**2)**(1/2))
    print("r = "+str(r)+" m")
    p = p + q / r
    n = n - 1
    s = s + 1
V = float(k*p)
print("Potencial Eléctrico = "+f"{V:10.2f}"+" V")

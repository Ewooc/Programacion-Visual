rep = ""
while rep == "":
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    c = float(input("Ingrese c: "))
    d = b**2 - 4*a*c
    if d>0:
        x1 = (-b+d**(1/2))/(2*a)
        x2 = (-b-d**(1/2))/(2*a)
        print("La ecuación tiene 2 soluciones:")
        print("x1 = "+str(x1))
        print("x2 = "+str(x2))
    elif d==0:
        x = -b/2*a
        print("La ecuación tiene 1 solución:")
        print("x = "+str(x))
    else:
        print("No tiene soluciones reales")
    rep = input("Pulse enter para iniciar de nuevo ")
print("Fin")


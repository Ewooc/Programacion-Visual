def Ingresar_Número():
    return complex(input("Ingrese número complejo: ").replace("i", "j"))

def Imprimir_Resultado():
    if z.imag >= 0:
        print(f"Resultado: {z.real}+{z.imag}i")
    else:
        print(f"Resultado: {z.real}{z.imag}i")

rep = ""
while rep == "":
    print("")
    
    z1 = Ingresar_Número()
    op = input("Suma (+), Multiplica (*), Eleva (/): ")
    
    if op == "/":
        n = float(input("Ingrese exponente real: "))
        z = z1 ** n
        Imprimir_Resultado()

    elif op == "*":    
        z2 = Ingresar_Número()
        z = z1 * z2
        Imprimir_Resultado()

    elif op == "+":
        z2 = Ingresar_Número()
        z = z1 + z2
        Imprimir_Resultado()

    else:
        print("Operación Inválida")

    rep = input("Pulse enter para iniciar de nuevo ")

print("Fin")


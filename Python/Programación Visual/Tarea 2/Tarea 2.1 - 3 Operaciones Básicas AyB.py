A = input("Valor de A: ")
while A != "-":
    A = float(A)
    C = input("Suma (+), Multiplica (*), Eleva (/): ")    
    B = float(input("Valor de B: "))
    
    if C == "+":
        D = float(A+B)
        print("Resultado: "+str(D))
    
    elif C == "*":
        D = float(A*B)
        print("Resultado: "+str(D))
    
    elif C == "/":
        D = float(A**B)
        print("Resultado: "+str(D))
    
    else:
        print("No se ingresó una operación válida")
        
    A = input("Valor de A: ")
    
print("Fin")
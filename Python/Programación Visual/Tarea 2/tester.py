minimo = float(input("minimo "))
maximo = float(input("maximo "))
cantidad = int(input("Numero "))

dif = float((maximo-minimo)/cantidad)

for i in range(cantidad+1):
    step = (minimo+(dif*i))
    I = 5678.34e2


    print(f"{step:10.6f} {I:15.6e}")
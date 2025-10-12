# Práctica 4 - Conversión Sistemas Numéricos
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

from tkinter import *
from tkinter import messagebox

ven = Tk()
ven.title("Convertidor Sistema Numérico")
ven.geometry("360x310")

ValorEntrada = StringVar()
ValorSalida = StringVar()
SistemaEntrada = IntVar()
SistemaSalida = IntVar()

def Verificación():
    if ValorEntrada.get() == "":
        messagebox.showerror("Valor no ingresado","No se ingresó un valor")
        return

    ValorIngresado = ValorEntrada.get().lower() # Tomar el valor ingresado pasando sus caracteres en minúscula para la verificación
    TotalCaracteres = len(ValorIngresado)
    Posición = 0
    while Posición < TotalCaracteres:
        CaracterPermitido = ValorIngresado[Posición]
        if SistemaEntrada.get() == 2: # Si es Binario
            ValorPermitido = ["0","1"]
            if CaracterPermitido not in ValorPermitido:
                messagebox.showerror("Valor no permitido","El valor ingresado no es permitido \n en el Sistema Numérico de Entrada")
                return
        elif SistemaEntrada.get() == 10: # Si es Decimal
            ValorPermitido = ["0","1","2","3","4","5","6","7","8","9"]
            if CaracterPermitido not in ValorPermitido:
                messagebox.showerror("Valor no permitido","El valor ingresado no es permitido \n en el Sistema Numérico de Entrada")
                return
        elif SistemaEntrada.get() == 8: # Si es Octal
            ValorPermitido = ["0","1","2","3","4","5","6","7"]
            if CaracterPermitido not in ValorPermitido:
                messagebox.showerror("Valor no permitido","El valor ingresado no es permitido \n en el Sistema Numérico de Entrada")
                return
        elif SistemaEntrada.get() == 16: # Si es Hexadecimal
            ValorPermitido = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
            if CaracterPermitido not in ValorPermitido:
                messagebox.showerror("Valor no permitido","El valor ingresado no es permitido \n en el Sistema Numérico de Entrada")
                return
        Posición += 1
    
    Conversión() ### Si el valor ingresado está permitido, pasar a la conversión


def Conversión():
    # Siempre convertir cualquier sistema a decimal, para después del decimal convertir a otro sistema particular
    valordecimal = int(ValorEntrada.get(), SistemaEntrada.get())

    ########## Otra manera más rápida de verificar si el dato ingresado es válido #######
    #try:
    #    valordecimal = int(ValorEntrada.get(), SistemaEntrada.get())
    #except ValueError as ex:
    #    messagebox.showerror("Error", str(ex))
    #    print(ex)
    #    return
    
    if SistemaSalida.get() == 2: # Si se busca Binario
        valornuevo = bin(valordecimal)[2:]

    elif SistemaSalida.get() == 8: # Si se busca Octal
        valornuevo = oct(valordecimal)[2:]
    
    elif SistemaSalida.get() == 16: # Si se busca Hexadecimal
        valornuevo = hex(valordecimal)[2:]#.upper()
    
    elif SistemaSalida.get() == 32: # Si se busca BCD
        valordecimal = str(valordecimal)
        TotalCaracteres = len(valordecimal)
        Posición = 0
        valornuevo = ""
        while Posición < TotalCaracteres:
            dígito = int( valordecimal[Posición] )
            dígitonuevo = bin(dígito)[2:].zfill(4)+" " # Rellenar con "0" a la izquierda e ingresar espacio en blanco a la derecha
            valornuevo += dígitonuevo
            Posición += 1
             
    else: # Si ya es Decimal
        valornuevo = str(valordecimal)
        
    ValorSalida.set(" "+valornuevo)
    

def Salir():
    ven.destroy()


##### Entradas
Label(ven,text="Valor",font=("Corbel",14),bg="#BB54E4").place(x=10,y=10,width=60,height=30)
Entry(ven,textvariable=ValorEntrada,font=("Cambria Math",12),bg="#D09BE5").place(x=80,y=10,width=270,height=30)

Label(ven,text="Sistema Numérico",font=("Corbel",14),bg="#B17BEE").place(x=10,y=50,width=230,height=30)
Label(ven,text="de Entrada",font=("Corbel",14),bg="#54E4AD").place(x=10,y=80,width=115,height=30)
Radiobutton(ven,text="Decimal",variable=SistemaEntrada,value=10,font=("Corbel",11),bg="#88EBC5",anchor="w").place(x=10,y=110,width=115,height=37.5)
Radiobutton(ven,text="Binario",variable=SistemaEntrada,value=2,font=("Corbel",11),bg="#88EBC5",anchor="w").place(x=10,y=147.5,width=115,height=37.5)
Radiobutton(ven,text="Octal",variable=SistemaEntrada,value=8,font=("Corbel",11),bg="#88EBC5",anchor="w").place(x=10,y=185,width=115,height=37.5)
Radiobutton(ven,text="Hexadecimal",variable=SistemaEntrada,value=16,font=("Corbel",11),bg="#88EBC5",anchor="w").place(x=10,y=222.5,width=115,height=37)

Label(ven,text="de Salida",font=("Corbel",14),bg="#7CA7EB").place(x=125,y=80,width=115,height=30)
Radiobutton(ven,text="Decimal",variable=SistemaSalida,value=10,font=("Corbel",11),bg="#93B6F0",anchor="w").place(x=125,y=110,width=115,height=30)
Radiobutton(ven,text="Binario",variable=SistemaSalida,value=2,font=("Corbel",11),bg="#93B6F0",anchor="w").place(x=125,y=140,width=115,height=30)
Radiobutton(ven,text="Octal",variable=SistemaSalida,value=8,font=("Corbel",11),bg="#93B6F0",anchor="w").place(x=125,y=170,width=115,height=30)
Radiobutton(ven,text="Hexadecimal",variable=SistemaSalida,value=16,font=("Corbel",11),bg="#93B6F0",anchor="w").place(x=125,y=200,width=115,height=30)
Radiobutton(ven,text="BCD",variable=SistemaSalida,value=32,font=("Corbel",11),bg="#93B6F0",anchor="w").place(x=125,y=230,width=115,height=30)


##### Salidas
Label(ven,text="Resultado",font=("Corbel",14),bg="#DED35B").place(x=10,y=270,width=90,height=30)
Label(ven,textvariable=ValorSalida,font=("Cambria Math",12),bg="#E8DF7D",anchor="w").place(x=110,y=270,width=240,height=30)


##### Botones
Button(ven,text="Calcular",command=Verificación,font=("Corbel",14),bg="#F9B62F").place(x=250,y=50,width=100,height=100)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=250,y=160,width=100,height=100)


SistemaEntrada.set(10) # Valores por defecto
SistemaSalida.set(10)

ven.mainloop()


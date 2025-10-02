from tkinter import *

ven = Tk()
ven.title("Test")
ven.geometry("600x200")

valorentrada = StringVar()
valorsalida = IntVar()
sistemaentrada = IntVar()
sistemasalida = IntVar()



def Conversión():
    # Siempre convertir cualquier sistema a decimal, para después del decimal convertir a otro sistema particular
    valordecimal = int(valorentrada.get(), sistemaentrada.get())
    
    if sistemasalida.get() == 2: # Se busca Binario
        valornuevo = bin(valordecimal)
    elif sistemasalida.get == 8: # Se busca Octal
        valornuevo = oct(valordecimal)
    elif sistemasalida.get == 16: # Se busca Hexadecimal
        valornuevo = hex(valordecimal)
    else: # Si ya es Decimal
        valornuevo = valordecimal
        
    valorsalida.set(valornuevo)
    

def Salir():
    ven.destroy()


##### Entradas
Label(ven,text="Valor",font=("Corbel",14),bg="light blue").place(x=10,y=10,width=60,height=30)
Entry(ven,textvariable=valorentrada,font=("Cambria Math",12),bg="light blue").place(x=80,y=10,width=100,height=30)

Radiobutton(ven,text="Decimal",variable=sistemaentrada,value=10).place(x=10,y=40,width=80,height=20)
Radiobutton(ven,text="Binario",variable=sistemaentrada,value=2).place(x=10,y=70,width=80,height=20)
Radiobutton(ven,text="Octal",variable=sistemaentrada,value=8).place(x=10,y=100,width=80,height=20)
Radiobutton(ven,text="Hexadecimal",variable=sistemaentrada,value=16).place(x=10,y=130,width=80,height=20)

Radiobutton(ven,text="Decimal",variable=sistemasalida,value=10).place(x=100,y=40,width=80,height=20)
Radiobutton(ven,text="Binario",variable=sistemasalida,value=2).place(x=100,y=70,width=80,height=20)
Radiobutton(ven,text="Octal",variable=sistemasalida,value=8).place(x=100,y=100,width=80,height=20)
Radiobutton(ven,text="Hexadecimal",variable=sistemasalida,value=16).place(x=100,y=130,width=80,height=20)



##### Salidas
Label(ven,textvariable=valorsalida,font=("Cambria Math",12),bg="light blue").place(x=80,y=160,width=100,height=30)


##### Botones
Button(ven,text="Calcular",command=Conversión,font=("Corbel",14),bg="orange").place(x=400,y=10,width=60,height=20)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="red").place(x=400,y=40,width=60,height=20)


ven.mainloop()
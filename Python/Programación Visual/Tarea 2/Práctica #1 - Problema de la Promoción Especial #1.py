# Práctica #1 - Problema de la Promoción Especial #1
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A 

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Promoción Especial #1, Problema 1 - Ley de Ohm")
ventana.geometry("460x200")

I = DoubleVar()
V = DoubleVar()
R = DoubleVar()
Resultado = DoubleVar()
Prefijo = StringVar()

def Calcular():
    if I.get() == 0:
        if R.get() == 0:
            messagebox.showerror("Error","No se puede dividir entre 0")
        elif V.get() == 0:
            messagebox.showwarning("Advertencia","No hay corriente")
        else:
            ValorResultado = V.get() / R.get()
            Unidad = "A"

    elif V.get() == 0:
        if R.get() == 0:
            messagebox.showwarning("Advertencia","No hay voltaje")
        else:
            ValorResultado = I.get() * R.get()
            Unidad = "V"
            
    else:
        ValorResultado = V.get() / I.get()
        Unidad = "Ω"
    
    Mostrar_Resultado(ValorResultado, Unidad)


def Mostrar_Resultado(Valor, Pref):
    if Valor < 1e-5: # Menor a 1μ
        NuevoValor = Valor * 1e6
        Prefijo.set("μ"+str(Pref))

    elif Valor < 1e-2: # Entre 1μ a 1m
        NuevoValor = Valor * 1e3
        Prefijo.set("m"+str(Pref))
    
    elif Valor < 1e3: # Entre 1m a 1K
        NuevoValor = Valor
        Prefijo.set(str(Pref))

    elif Valor < 1e6: # Entre 1K a 1M
        NuevoValor = Valor / 1e3
        Prefijo.set("K"+str(Pref))
    
    else: # Mayor a 1M
        NuevoValor = Valor / 1e6
        Prefijo.set("M"+str(Pref))
    
    Resultado.set(round(NuevoValor,2))


def Salir():
    salir = messagebox.askquestion("Saliendo . . .","Salir?")
    if salir == "yes":
        ventana.destroy()


### Entradas
Label(ventana,text="Corriente (A):",font=("Corbel", 14),bg="#83FE73").place(x=5,y=5,width=140,height=30) ####### Texto
Label(ventana,text="Voltaje (V):",font=("Corbel", 14),bg="#73B2FE").place(x=5,y=40,width=140,height=30)
Label(ventana,text="Resistencia (R):",font=("Corbel", 14),bg="#FE7373").place(x=5,y=75,width=140,height=30)
Entry(ventana,textvariable=I,font=("Cambria Math", 12),bg="#ffffff").place(x=150,y=5,width=130,height=30) ####### Valores
Entry(ventana,textvariable=V,font=("Cambria Math", 12),bg="#ffffff").place(x=150,y=40,width=130,height=30)
Entry(ventana,textvariable=R,font=("Cambria Math", 12),bg="#ffffff").place(x=150,y=75,width=130,height=30)
Label(ventana,text="A",font=("Corbel", 14),bg="#83FE73").place(x=285,y=5,width=25,height=30) ####### Unidades
Label(ventana,text="V",font=("Corbel", 14),bg="#73B2FE").place(x=285,y=40,width=25,height=30)
Label(ventana,text="Ω",font=("Corbel", 14),bg="#FE7373").place(x=285,y=75,width=25,height=30)

### Salidas
Label(ventana,text="Resultado:",font=("Corbel", 16),bg="#C04FC0").place(x=5,y=145,width=140,height=30)
Label(ventana,textvariable=Resultado,font=("Cambria Math", 12),bg="#ffffff").place(x=150,y=145,width=130,height=30)
Label(ventana,textvariable=Prefijo,font=("Cambria Math", 12),bg="#ffffff").place(x=285,y=145,width=25,height=30)
Label(ventana,text="valor",font=("Corbel", 12)).place(x=150,y=175,width=130,height=20)
Label(ventana,text="unidad",font=("Corbel", 12)).place(x=268,y=175,width=60,height=20)

### Comandos (Botones)
Button(ventana,text="Calcular",command=Calcular,font=("Corbel", 14),bg="#F9B62F").place(x=340,y=10,width=100,height=80)
Button(ventana,text="Salir",command=Salir,font=("Corbel", 14),bg="#D0235D").place(x=340,y=100,width=100,height=80)

messagebox.showinfo("Te damos la bienvenida!","Gracias por utilizar la calculadora")

ventana.mainloop()


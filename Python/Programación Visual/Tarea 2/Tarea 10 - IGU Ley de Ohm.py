# De la Promoción Especial #1, Problema 1

from tkinter import *

ventana = Tk()
ventana.title("Promoción Especial #1, Problema 1 - Ley de Ohm")
ventana.geometry("440x180")

I = DoubleVar()
V = DoubleVar()
R = DoubleVar()
Resultado = DoubleVar()
Unidad = StringVar()

def Calcular():
    if I.get() == 0:
        Ires = V.get() / R.get()
        Resultado.set(Ires)
        Unidad.set("A")
    elif V.get() == 0:
        Vres = I.get() * R.get()
        Resultado.set(Vres)
        Unidad.set("V")
    else:
        Rres = V.get() / I.get()
        Resultado.set(Rres)
        Unidad.set("Ω")

def Salir():
    ventana.destroy()

### Entradas
Label(ventana,text="Corriente (A):",bg="#83FE73").place(x=5,y=5,width=90,height=30) ####### Texto
Label(ventana,text="Voltaje (V):",bg="#73B2FE").place(x=5,y=40,width=90,height=30)
Label(ventana,text="Resistencia (R):",bg="#FE7373").place(x=5,y=75,width=90,height=30)
Entry(ventana,textvariable=I,bg="#ffffff").place(x=100,y=5,width=195,height=30) ####### Valores
Entry(ventana,textvariable=V,bg="#ffffff").place(x=100,y=40,width=195,height=30)
Entry(ventana,textvariable=R,bg="#ffffff").place(x=100,y=75,width=195,height=30)
Label(ventana,text="A",bg="#83FE73").place(x=300,y=5,width=15,height=30) ####### Unidades
Label(ventana,text="V",bg="#73B2FE").place(x=300,y=40,width=15,height=30)
Label(ventana,text="Ω",bg="#FE7373").place(x=300,y=75,width=15,height=30)

### Salidas
Label(ventana,text="Resultado:",bg="#C04FC0").place(x=5,y=130,width=90,height=30)
Label(ventana,textvariable=Resultado,bg="#ffffff").place(x=100,y=130,width=195,height=30)
Label(ventana,textvariable=Unidad,bg="#ffffff").place(x=300,y=130,width=15,height=30)
Label(ventana,text="valor").place(x=100,y=165,width=195,height=10)
Label(ventana,text="unidad").place(x=290,y=165,width=35,height=10)

### Comandos (Botones)
Button(ventana,text="Calcular",command=Calcular,bg="#F9B62F").place(x=340,y=10,width=80,height=60)
Button(ventana,text="Salir",command=Salir,bg="#D0235D").place(x=340,y=80,width=80,height=60)

ventana.mainloop()


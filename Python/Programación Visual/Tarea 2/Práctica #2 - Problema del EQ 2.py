# Práctica #2 - Problema #1 del Examen Quincenal #2
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A


import math
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Examen Quincenal #2, Problema #1 - Impedancia")
ventana.geometry("420x200")

Tipo = IntVar()
Value = DoubleVar()
Frec = DoubleVar()
Zreal = DoubleVar()
Zimag = DoubleVar()
Prefijo = StringVar()
Unidad = StringVar()


def Comprobar_Valores(): ##### Verificar si se ingresó Valor de componente y Frecuencia del circuito
    if Value.get() == 0:
            messagebox.showerror("Error","No hay un valor de componente")    
    else:
        if Frec.get() == 0:
            messagebox.showwarning("Advertencia","No hay frecuencia del circuito")
        else:
            Calcular_Impedancia()


def Calcular_Impedancia(): ##### Realiza el cálculo de la impedancia de cada componente
    w = 2 * math.pi * Frec.get()
    real = 0.0
    imag = 0.0
    if Tipo.get() == 1: # Resistencia
        real = Value.get()
        real = Determinar_Prefijo(real)
    elif Tipo.get() == 2: # Inductor
        imag = w * Value.get()
        imag = Determinar_Prefijo(imag)
    elif Tipo.get() == 3: # Capacitor
        imag = 1 / ( w * Value.get() ) # Valor positivo para no interferir en notación
        imag = Determinar_Prefijo(imag)
        imag = -1 * imag # Regresar a valor negativo
    else: # Si no se eligió tipo
        Prefijo.set("-")
        messagebox.showerror("Error","No se eligió tipo")
    Zreal.set(real)
    Zimag.set(imag)


def Determinar_Prefijo(Valor): ##### Hace la conversión a notación de ingeniería
    if Valor < 1e-5: # Menor a 1μ
        NuevoValor = Valor * 1e6
        Prefijo.set("μΩ")
    elif Valor < 1e-2: # Entre 1μ a 1m
        NuevoValor = Valor * 1e3
        Prefijo.set("mΩ")
    elif Valor < 1e3: # Entre 1m a 1K
        NuevoValor = Valor
        Prefijo.set("Ω")
    elif Valor < 1e6: # Entre 1K a 1M
        NuevoValor = Valor / 1e3
        Prefijo.set("KΩ")
    else: # Mayor a 1M
        NuevoValor = Valor / 1e6
        Prefijo.set("MΩ")
    return round(NuevoValor,2)


def Fijar_Unidad(): ##### Para indicar que el valor tiene una unidad determinada
    if Tipo.get() == 1: # Resistencia
        Unidad.set("Ω")
    elif Tipo.get() == 2: # Inductor
        Unidad.set("H")
    elif Tipo.get() == 3: # Capacitor
        Unidad.set("F")


def Salir(): ##### Cierra la ventana
    salir = messagebox.askquestion("Saliendo . . .","Salir?")
    if salir == "yes":
        ventana.destroy()


##### Entradas
Label(ventana,text="Frecuencia:",font=("Corbel", 14),bg="#73B2FE").place(x=10,y=10,width=100,height=30)
Entry(ventana,textvariable=Frec,font=("Cambria Math", 12),bg="#ffffff").place(x=115,y=10,width=120,height=30)
Label(ventana,text="Hz",font=("Corbel", 14),bg="#73B2FE").place(x=240,y=10,width=30,height=30)

Label(ventana,text="Valor:",font=("Corbel", 14),bg="#83FE73").place(x=10,y=50,width=60,height=30)
Entry(ventana,textvariable=Value,font=("Cambria Math", 12),bg="#ffffff").place(x=75,y=50,width=160,height=30)
Label(ventana,textvariable=Unidad,font=("Corbel", 14),bg="#83FE73").place(x=240,y=50,width=30,height=30) # Indica unidad del valor

Label(ventana,text="Tipo de",font=("Corbel", 14),bg="#FE7373").place(x=290,y=20,width=110,height=25)
Label(ventana,text="Componente",font=("Corbel", 14),bg="#FE7373").place(x=290,y=45,width=110,height=25)
Radiobutton(ventana,variable=Tipo,value=1,command=Fijar_Unidad).place(x=290,y=75,width=25,height=20) # Resistencia
Label(ventana,text="R",font=("Corbel", 10)).place(x=290,y=95,width=20,height=20)
Radiobutton(ventana,variable=Tipo,value=2,command=Fijar_Unidad).place(x=335,y=75,width=25,height=20) # Inductor
Label(ventana,text="L",font=("Corbel", 10)).place(x=335,y=95,width=20,height=20)
Radiobutton(ventana,variable=Tipo,value=3,command=Fijar_Unidad).place(x=380,y=75,width=25,height=20) # Capacitor
Label(ventana,text="C",font=("Corbel", 10)).place(x=380,y=95,width=20,height=20)


##### Salidas
Label(ventana,text="Impedancia:",font=("Corbel",14),bg="#C04FC0").place(x=10,y=140,width=110,height=30)

Label(ventana,textvariable=Zreal,bg="#E6C4E6").place(x=130,y=140,width=100,height=30)
Label(ventana,text="valor real",font=("Corbel", 10)).place(x=130,y=170,width=100,height=20)

Label(ventana,textvariable=Zimag,bg="#E6C4E6").place(x=240,y=140,width=100,height=30)
Label(ventana,text="valor imaginario",font=("Corbel", 10)).place(x=240,y=170,width=100,height=20)

Label(ventana,textvariable=Prefijo,bg="#DEAADE").place(x=350,y=140,width=30,height=30)
Label(ventana,text="unidad",font=("Corbel", 10)).place(x=341,y=170,width=50,height=20)


##### Comandos
Button(ventana,text="Calcular",command=Comprobar_Valores,font=("Corbel", 14),bg="#F9B62F").place(x=30,y=90,width=100,height=40)
Button(ventana,text="Salir",command=Salir,font=("Corbel", 14),bg="#D0235D").place(x=150,y=90,width=100,height=40)


Unidad.set("-")
messagebox.showinfo("Te damos la bienvenida!","Gracias por utilizar la calculadora")

ventana.mainloop()



# Práctica #3 - Problema del Examen Quincenal #3
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

import math
from tkinter import *
from tkinter import messagebox

ven = Tk()
ven.title("Resistencia Alambre")
ven.geometry("550x150")

R = DoubleVar()
M = StringVar()
L = DoubleVar()
C = IntVar()
pref = StringVar()

# Generar lista para verificación del calibre
Calibre=[1.45, 1.291, 1.15, 1.02362, 0.9116, 0.8128, 0.7229, 0.6438, 0.5733, 0.5106, 0.4547, 0.4049, 0.3606, 0.3211, 0.2859, 0.2546]

def Obtener_Resistividad(): # P
    Material = M.get().lower()
    if Material == "plata":
        ValorP = 1.47e-8
    elif Material == "cobre":
        ValorP = 1.72e-8
    elif Material == "oro":
        ValorP = 2.44e-8
    elif Material == "aluminio":
        ValorP = 2.75e-8
    elif Material == "tungsteno":
        ValorP = 5.25e-8
    elif Material == "acero":
        ValorP = 20e-8
    elif Material == "plomo":
        ValorP = 22e-8
    elif Material == "mercurio":
        ValorP = 95e-8
    elif Material == "manganina":
        ValorP = 44e-8
    elif Material == "constantan":
        ValorP = 49e-8
    elif Material == "nikelcromio":
        ValorP = 100e-8
    elif Material == "":
        messagebox.showerror("No hay material","Introduzca un material")
        R.set(0)
        pref.set("-")
    else:
        messagebox.showerror("Material no válido","Introduzca un material válido")
        R.set(0)
        pref.set("-")
    return ValorP


def Obtener_Área(): # A
    RadioAlambre = Calibre[ C.get() - 15 ] / 2000 # Restar 15 para obtener posición en la lista
    ValorA = math.pi * (RadioAlambre ** 2) # Calcular área
    return ValorA


def Calcular_Resistencia(): # R
    P = Obtener_Resistividad()
    A = Obtener_Área()
    Res = P * (L.get() / A)
    Determinar_Prefijo(Res)


def Determinar_Prefijo(Valor): ##### Hace la conversión a notación de ingeniería
    if Valor < 1e-5: # Menor a 1μ
        NuevoValor = Valor * 1e6
        pref.set("μΩ")
    elif Valor < 1e-2: # Entre 1μ a 1m
        NuevoValor = Valor * 1e3
        pref.set("mΩ")
    elif Valor < 1e3: # Entre 1m a 1K
        NuevoValor = Valor
        pref.set("Ω")
    else: # Mayor a 1K
        NuevoValor = Valor / 1e3
        pref.set("KΩ")
    R.set( round(NuevoValor,4) )


def Mostrar_Materiales():
    messagebox.showinfo("Lista de Materiales Disponibles",
                        "Plata, Cobre, Oro, " \
                        "Aluminio, Tungsteno, " \
                        "Acero, Plomo, Mercurio, " \
                        "Manganina, Constantan, " \
                        "Nikelcromio")


def Salir():
    ven.destroy()


##### Entradas
Label(ven,text="Longitud",font=("Corbel",14),bg="#BB54E4").place(x=10,y=10,width=100,height=30)
Entry(ven,textvariable=L,font=("Cambria Math",12),bg="#D09BE5").place(x=120,y=10,width=80,height=30)
Label(ven,text="m",font=("Corbel",14),bg="#D09BE5").place(x=205,y=10,width=30,height=30)
Scale(ven,variable=L,from_=0,to=1000,resolution=0.001,orient=HORIZONTAL).place(x=240,y=2,width=289,height=60)

Label(ven,text="Calibre",font=("Corbel",14),bg="#54E4AD").place(x=10,y=50,width=100,height=30)
Scale(ven,variable=C,from_=15,to=30,orient=HORIZONTAL).place(x=117,y=42,width=167,height=60)

Label(ven,text="Material",font=("Corbel",14),bg="#A6E454").place(x=290,y=50,width=100,height=30)
Entry(ven,textvariable=M,font=("Cambria Math",12),bg="#D4FAA3").place(x=400,y=50,width=100,height=30)

##### Salidas
Label(ven,text="Resistencia",font=("Corbel",14),bg="#DD637E").place(x=10,y=90,width=100,height=30)
Label(ven,textvariable=R,font=("Cambria Math",12),bg="#E39DAD").place(x=120,y=90,width=160,height=30)
Label(ven,textvariable=pref,font=("Cambria Math",12),bg="#E39DAD").place(x=285,y=90,width=35,height=30)

##### Botones
Button(ven,text="i",command=Mostrar_Materiales,font=("Cambria Math",12),bg="#48A6E4").place(x=505,y=50,width=20,height=20)
Button(ven,text="Calcular",command=Calcular_Resistencia,font=("Corbel",14),bg="#F9B62F").place(x=333,y=90,width=90,height=30)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=435,y=90,width=90,height=30)

ven.mainloop()


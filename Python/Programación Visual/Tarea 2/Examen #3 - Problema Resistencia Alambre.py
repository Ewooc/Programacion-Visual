# Examen 3 - Problema Resistencia Alambre
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

import math
from tkinter import *

ven = Tk()
ven.title("Resistencia Alambre")
ven.geometry("550x240")

R = DoubleVar()
M = DoubleVar()
L = DoubleVar()
C = IntVar()
pref = StringVar()

# Generar una lista para verificación del calibre
Calibre=[1.45, 1.291, 1.15, 1.02362, 0.9116, 0.8128, 0.7229, 0.6438, 0.5733, 0.5106, 0.4547, 0.4049, 0.3606, 0.3211, 0.2859, 0.2546]


def Calcular_Resistencia():
    P = M.get() * 1e-8 # Obtener resistividad del material
    radio = Calibre[ C.get() - 15 ] / 2000 # Restar 15 para obtener posición en la lista
    A = math.pi * (radio ** 2) # Obtener área de sección transversal
    Res = P * (L.get() / A) # Calcular resistencia
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


def Salir():
    ven.destroy()


##### Entradas
Label(ven,text="Longitud",font=("Corbel",14),bg="#BB54E4").place(x=10,y=10,width=100,height=30)
Entry(ven,textvariable=L,font=("Cambria Math",12),bg="#D09BE5").place(x=120,y=10,width=80,height=30)
Label(ven,text="m",font=("Corbel",14),bg="#D09BE5").place(x=205,y=10,width=30,height=30)
Scale(ven,variable=L,from_=0,to=1000,resolution=0.001,orient="horizontal").place(x=240,y=2,width=289,height=60)

Label(ven,text="Calibre",font=("Corbel",14),bg="#54E4AD").place(x=10,y=140,width=100,height=30)
Scale(ven,variable=C,from_=15,to=30,orient="horizontal").place(x=117,y=132,width=207,height=60)

Label(ven,text="Material",font=("Corbel",14),bg="#A6E454").place(x=10,y=50,width=100,height=80)
Radiobutton(ven,text="Plata",variable=M,value=1.47,font=("Corbel",10),bg="#D6DCDD").place(x=120,y=50,width=90,height=20)
Radiobutton(ven,text="Cobre",variable=M,value=1.72,font=("Corbel",10),bg="#CC8544").place(x=225,y=50,width=90,height=20)
Radiobutton(ven,text="Oro",variable=M,value=2.44,font=("Corbel",10),bg="#CFB851").place(x=330,y=50,width=90,height=20)
Radiobutton(ven,text="Aluminio",variable=M,value=2.75,font=("Corbel",10),bg="#85805F").place(x=435,y=50,width=90,height=20)
Radiobutton(ven,text="Tungsteno",variable=M,value=5.25,font=("Corbel",10),bg="#8DB18D").place(x=120,y=80,width=90,height=20)
Radiobutton(ven,text="Acero",variable=M,value=20,font=("Corbel",10),bg="#A5B7D0").place(x=225,y=80,width=90,height=20)
Radiobutton(ven,text="Plomo",variable=M,value=22,font=("Corbel",10),bg="#688E97").place(x=330,y=80,width=90,height=20)
Radiobutton(ven,text="Manganina",variable=M,value=44,font=("Corbel",10),bg="#B17E6E").place(x=435,y=80,width=90,height=20)
Radiobutton(ven,text="Constantán",variable=M,value=49,font=("Corbel",10),bg="#AFA6DF").place(x=120,y=110,width=90,height=20)
Radiobutton(ven,text="Mercurio",variable=M,value=95,font=("Corbel",10),bg="#7DA5A1").place(x=225,y=110,width=90,height=20)
Radiobutton(ven,text="Nikelcromio",variable=M,value=100,font=("Corbel",10),bg="#978665").place(x=330,y=110,width=90,height=20)

##### Salidas
Label(ven,text="Resistencia",font=("Corbel",14),bg="#DD637E").place(x=10,y=180,width=100,height=30)
Label(ven,textvariable=R,font=("Cambria Math",12),bg="#E39DAD").place(x=120,y=180,width=160,height=30)
Label(ven,textvariable=pref,font=("Cambria Math",12),bg="#E39DAD").place(x=285,y=180,width=35,height=30)

##### Botones
Button(ven,text="Calcular",command=Calcular_Resistencia,font=("Corbel",14),bg="#F9B62F").place(x=333,y=155,width=90,height=50)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=435,y=155,width=90,height=50)

M.set(1.47) # Valor por defecto (inicial): Plata

ven.mainloop()


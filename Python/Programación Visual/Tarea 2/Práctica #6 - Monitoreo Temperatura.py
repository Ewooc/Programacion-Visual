# Práctica 6 - Monitoreo Temperatura
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

from tkinter import *
from tkinter import messagebox

ven = Tk()
ven.title("Monitoreo Temperatura")
ven.geometry("270x210")

Temperatura = StringVar() # Señal a 8 bits
Tmax = DoubleVar()
Tmin = DoubleVar()
Suma = DoubleVar()
Contador = IntVar()
Promedio = DoubleVar()

valoresbinario={"0","1"}
Tmax.set(0)
Tmin.set(1e50)
Suma.set(0)
Contador.set(0)
Promedio.set(0)

def Verificar():
    valoringresado = Temperatura.get()
    valorprueba = set(Temperatura.get())
    if valoringresado == "":
        messagebox.showerror("Error","Valor no ingresado")
        return
    if not valorprueba.issubset(valoresbinario):
        messagebox.showerror("Error","Valor no binario")
        return
    if int(valoringresado,2) > 255:
        messagebox.showerror("Error","Valor superior a 255")
        return
    CalcularTemp()

def CalcularTemp():
    Contador.set( Contador.get() + 1 )
    if Contador.get() == 17:
        messagebox.showinfo("Día Completado","Ya pasó un día, registrando valores para el siguiente")
        Tmax.set(0)
        Tmin.set(1e50)
        Suma.set(0)
        Contador.set(1)
        Promedio.set(0)
    valorseñal = int(Temperatura.get(),2)
    valortemperatura = round(valorseñal*100 / 255,4)
    if valortemperatura < Tmin.get():
        Tmin.set(valortemperatura)
    if valortemperatura > Tmax.get():
        Tmax.set(valortemperatura)
    sumaactual = round(Suma.get() + valortemperatura,4)
    promedioactual = round(sumaactual / Contador.get(),4)
    Suma.set( sumaactual )
    Promedio.set( promedioactual )

def Salir():
    ven.destroy()

##### Entradas
Label(ven,text="Valor Detectado",font=("Corbel",14),bg="#93EA83").place(x=10,y=10,width=140,height=30)
Entry(ven,textvariable=Temperatura,font=("Cambria Math",12),bg="#ADF5A0").place(x=160,y=10,width=100,height=30)

##### Salidas
Label(ven,text="Valor Máximo",font=("Corbel",14),bg="#EB5280").place(x=10,y=90,width=140,height=30)
Label(ven,textvariable=Tmax,font=("Cambria Math",12),bg="#E87094").place(x=160,y=90,width=100,height=30)
Label(ven,text="Valor Mínimo",font=("Corbel",14),bg="#9183EA").place(x=10,y=130,width=140,height=30)
Label(ven,textvariable=Tmin,font=("Cambria Math",12),bg="#A195EE").place(x=160,y=130,width=100,height=30)
Label(ven,text="Promedio",font=("Corbel",14),bg="#EAD583").place(x=10,y=170,width=140,height=30)
Label(ven,textvariable=Promedio,font=("Cambria Math",12),bg="#F0DF9C").place(x=160,y=170,width=100,height=30)

##### Botones
Button(ven,text="Ingresar",command=Verificar,font=("Corbel",14),bg="#F9B62F").place(x=20,y=50,width=120,height=30)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=170,y=50,width=80,height=30)

ven.mainloop()

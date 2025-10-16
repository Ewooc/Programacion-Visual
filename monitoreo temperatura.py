from tkinter import *
from tkinter import messagebox

ven = Tk()
ven.title("Monitoreo de Temperatura")
ven.geometry("400x200")

Temperatura = StringVar() # Señal a 8 bits
Tmax = DoubleVar()
Tmin = DoubleVar()
Suma = DoubleVar()
Contador = IntVar()
Promedio = DoubleVar()
###
señal = DoubleVar()
temp = DoubleVar()

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
    ###
    señal.set(valorseñal)
    temp.set(valortemperatura)
    ###
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
Label(ven,text="Valor Detectado").place(x=10,y=10,width=100,height=30)
Entry(ven,textvariable=Temperatura).place(x=10,y=40,width=100,height=30)

##### Salidas
Label(ven,text="Valor Máximo").place(x=10,y=80,width=100,height=30)
Label(ven,textvariable=Tmax).place(x=120,y=80,width=60,height=30)
Label(ven,text="Valor Mínimo").place(x=10,y=120,width=100,height=30)
Label(ven,textvariable=Tmin).place(x=120,y=120,width=60,height=30)
Label(ven,text="Promedio").place(x=10,y=160,width=100,height=30)
Label(ven,textvariable=Promedio).place(x=120,y=160,width=60,height=30)

Label(ven,text="señal").place(x=240,y=20,width=60,height=30)
Label(ven,textvariable=señal).place(x=300,y=20,width=60,height=30)
Label(ven,text="temp").place(x=240,y=60,width=60,height=30)
Label(ven,textvariable=temp).place(x=300,y=60,width=60,height=30)
Label(ven,text="suma").place(x=240,y=100,width=60,height=30)
Label(ven,textvariable=Suma).place(x=300,y=100,width=60,height=30)
Label(ven,text="cont").place(x=240,y=140,width=60,height=30)
Label(ven,textvariable=Contador).place(x=300,y=140,width=60,height=30)

##### Botones
Button(ven,text="Ingresar",command=Verificar).place(x=140,y=10,width=60,height=30)
Button(ven,text="Salir",command=Salir).place(x=140,y=40,width=60,height=30)


ven.mainloop()







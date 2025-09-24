
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Título Genérico")
ventana.geometry("100x100")

Variable1 = DoubleVar()
Variable2 = DoubleVar()
Variable3 = StringVar()

def Función1():
    # Procesos de la Función1 generando Cosa1 y Cosa2
    Cosa1 = Variable1.get()
    Cosa2 = Variable2.get()
    Función2(Cosa1, Cosa2)

def Función2(Algo1,Algo2):
    # Procesos de la Función2 con Algo1 y Algo2 de otro lado
    Resultado = Algo1 + Algo2
    Variable3.set(Resultado)

def Salir():
    salir = messagebox.askquestion("Título","Mensaje") # Pregunta SI/NO
    if salir == "yes":
        ventana.destroy()


### Entradas
Label(ventana,text="Texto Genérico 1",font=("Tipografía", 14),bg="Color").place(x=0,y=0,width=0,height=0)
Entry(ventana,textvariable=Variable1,font=("Tipografía", 12),bg="Color").place(x=0,y=0,width=0,height=0)

### Salidas
Label(ventana,textvariable=Variable3,font=("Tipografía", 16),bg="Color").place(x=0,y=0,width=0,height=0)

### Comandos (Botones)
Button(ventana,text="Opción1",command=Función1,font=("Tipografía", 14),bg="Color").place(x=0,y=0,width=0,height=0)
Button(ventana,text="Salir",command=Salir,font=("Tipografía", 14),bg="Color").place(x=0,y=0,width=0,height=0)

messagebox.showinfo("Título","Mensaje") # Información genérica
messagebox.showwarning("Título","Mensaje") # Advertencia
messagebox.showerror("Título","Mensaje") # Error

ventana.mainloop()


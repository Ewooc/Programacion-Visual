from tkinter import *

ven = Tk()
ven.title("Secuencia 1-0-1-0-1")
ven.geometry("1060x550")

Valor = IntVar()
xcoord = IntVar()
Ciclos = IntVar()

Ciclos.set(0)
xcoord.set(30)

def Click():
    x = xcoord.get()
    if Valor.get() == 0:
        if x == 210 or x == 570:
            xcoord.set( xcoord.get() + 180 )
        elif x == 390 or x == 750:
            xcoord.set( 30 )
        elif x == 930:
            xcoord.set( 30 )

    elif Valor.get() == 1:
        if x == 30 or x == 390:
            xcoord.set( xcoord.get() + 180 )
        elif x == 570 or x == 930:
            xcoord.set( 210 )
        elif x == 750:
            Ciclos.set( Ciclos.get() + 1 )
            xcoord.set( 930 )
    Posición.place(x=xcoord.get())

def Reset():
    xcoord.set( 30 )
    Posición.place(x=xcoord.get())
    Ciclos.set(0)

def CambiarValor():
    if Valor.get() == 1:
        Valor.set(0)
    else:
        Valor.set(1)

def Salir():
    ven.destroy()

############################# | IGU | #############################

###### | Estados | ######
Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=30,y=120,width=90,height=100) # 1
Label(ven,text="A",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=56,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=120,y=120,width=90,height=100)
Label(ven,text="1",font=("Consolas",16)).place(x=120,y=130,width=90)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=210,y=120,width=90,height=100) # 2
Label(ven,text="B",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=236,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=300,y=120,width=90,height=100)
Label(ven,text="0",font=("Consolas",16)).place(x=300,y=130,width=90)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=390,y=120,width=90,height=100) # 3
Label(ven,text="C",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=416,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=480,y=120,width=90,height=100)
Label(ven,text="1",font=("Consolas",16)).place(x=480,y=130,width=90)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=570,y=120,width=90,height=100) # 4
Label(ven,text="D",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=596,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=660,y=120,width=90,height=100)
Label(ven,text="0",font=("Consolas",16)).place(x=660,y=130,width=90)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=750,y=120,width=90,height=100) # 5
Label(ven,text="E",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=776,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=840,y=120,width=90,height=100)
Label(ven,text="1",font=("Consolas",16)).place(x=840,y=130,width=90)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=930,y=120,width=90,height=100) # 6
Label(ven,text="F",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=956,y=152,width=36)

Label(ven,text="Ciclos\nCompletados",font=("Corbel", 20)).place(x=820,y=290,width=150,height=60)
Label(ven,textvariable=Ciclos,font=("Consolas", 24)).place(x=825,y=360,width=140,height=50)

##### | Botones | #####
Label(ven,text="Valor a\nIngresar",font=("Corbel", 20)).place(x=35,y=310,width=150,height=80)
Button(ven,textvariable=Valor,command=CambiarValor,font=("Consolas",20),bg="#09799B").place(x=180,y=320,width=60,height=60)

Button(ven,text="Click",command=Click,font=("Corbel",16),bg="#03CD72").place(x=320,y=320,width=100,height=60)
Button(ven,text="Reset",command=Reset,font=("Corbel",16),bg="#EA9E1C").place(x=470,y=320,width=100,height=60)
Button(ven,text="Salir",command=Salir,font=("Corbel",16),bg="#EA1C9F").place(x=620,y=320,width=100,height=60)

##### Flecha de Posición Actual
Posición = Label(ven,text="↓",font=("Cambria Math",32))
Posición.place(x=xcoord.get(),y=60,width=90,height=38)

ven.mainloop()
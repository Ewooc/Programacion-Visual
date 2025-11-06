from tkinter import *

ven = Tk()
ven.title("Máquina de Estados")
ven.geometry("1410x550")

Entrada1 = IntVar()
Entrada2 = IntVar()
Entrada3 = IntVar()
Entrada4 = IntVar()
Entrada5 = IntVar()
xcoord = IntVar()
Ciclos = IntVar()

Ciclos.set(0)
xcoord.set(30)

def Click():
    if Entrada5.get() == 1:
        if xcoord.get() == 30:
            xcoord.set( 750 )
        elif xcoord.get() == 750:
            xcoord.set( 1290 )
        else:
            xcoord.set( 210 )

    elif Entrada4.get() == 1:
        if xcoord.get() == 30 or xcoord.get() == 390 or xcoord.get() == 930:
            xcoord.set( xcoord.get() + 360 )
        elif xcoord.get() == 750:
            xcoord.set( 570 )

    elif Entrada3.get() == 1:
        if xcoord.get() == 750:
            xcoord.set( 930 )
        elif xcoord.get() == 1290:
            xcoord.set( 30 )
            Ciclos.set( Ciclos.get() + 1 )
        
    elif Entrada2.get() == 1:
        if xcoord.get() > 30 and xcoord.get() != 750:
            xcoord.set( xcoord.get() - 180 )
            Posición.place(x=xcoord.get())

    elif Entrada1.get() == 1:
        if xcoord.get() != 750 and xcoord.get() != 1290:
            xcoord.set( xcoord.get() + 180 )
    Posición.place(x=xcoord.get())

def Reset():
    xcoord.set( 30 )
    Posición.place(x=xcoord.get())
    Ciclos.set(0)

def Valor1():
    if Entrada1.get() == 1:
        Entrada1.set(0)
    else:
        Entrada1.set(1)

def Valor2():
    if Entrada2.get() == 1:
        Entrada2.set(0)
    else:
        Entrada2.set(1)

def Valor3():
    if Entrada3.get() == 1:
        Entrada3.set(0)
    else:
        Entrada3.set(1)

def Valor4():
    if Entrada4.get() == 1:
        Entrada4.set(0)
    else:
        Entrada4.set(1)

def Valor5():
    if Entrada5.get() == 1:
        Entrada5.set(0)
    else:
        Entrada5.set(1)

def Salir():
    ven.destroy()

############################# | IGU | #############################

###### | Estados | ######
Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=30,y=120,width=90,height=100) # 1
Label(ven,text="A",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=56,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=120,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=210,y=120,width=90,height=100) # 2
Label(ven,text="B",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=236,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=300,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=390,y=120,width=90,height=100) # 3
Label(ven,text="C",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=416,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=480,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=570,y=120,width=90,height=100) # 4
Label(ven,text="D",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=596,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=660,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=750,y=120,width=90,height=100) # 5
Label(ven,text="E",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=776,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=840,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=930,y=120,width=90,height=100) # 6
Label(ven,text="F",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=956,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=1020,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=1110,y=120,width=90,height=100) # 7
Label(ven,text="G",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=1136,y=152,width=36)
Label(ven,text="→",font=("Cambria Math",48),fg="#2B2B2B").place(x=1200,y=120,width=90,height=100)

Label(ven,text="•",font=("Corbel",200),fg="#999999").place(x=1290,y=120,width=90,height=100) # 8
Label(ven,text="H",font=("Corbel",24),fg="#2B2B2B",bg="#999999").place(x=1316,y=152,width=36)

Label(ven,text="Ciclos\nCompletados",font=("Corbel", 20)).place(x=1130,y=290,width=150,height=60)
Label(ven,textvariable=Ciclos,font=("Consolas", 24)).place(x=1135,y=360,width=140,height=50)

##### | Botones | #####
Button(ven,text="1",command=Valor1,font=("Consolas",20),bg="#09799B").place(x=60,y=320,width=60,height=60)
Label(ven,textvariable=Entrada1,font=("Consolas",20)).place(x=60,y=390,width=60,height=30)
Button(ven,text="2",command=Valor2,font=("Consolas",20),bg="#D22668").place(x=150,y=320,width=60,height=60)
Label(ven,textvariable=Entrada2,font=("Consolas",20)).place(x=150,y=390,width=60,height=30)
Button(ven,text="3",command=Valor3,font=("Consolas",20),bg="#13AC53").place(x=240,y=320,width=60,height=60)
Label(ven,textvariable=Entrada3,font=("Consolas",20)).place(x=240,y=390,width=60,height=30)
Button(ven,text="4",command=Valor4,font=("Consolas",20),bg="#F1DA33").place(x=330,y=320,width=60,height=60)
Label(ven,textvariable=Entrada4,font=("Consolas",20)).place(x=330,y=390,width=60,height=30)
Button(ven,text="5",command=Valor5,font=("Consolas",20),bg="#C924E6").place(x=420,y=320,width=60,height=60)
Label(ven,textvariable=Entrada5,font=("Consolas",20)).place(x=420,y=390,width=60,height=30)
Button(ven,text="Click",command=Click,font=("Corbel",16),bg="#03CD72").place(x=600,y=340,width=100,height=60)
Button(ven,text="Reset",command=Reset,font=("Corbel",16),bg="#EA9E1C").place(x=750,y=340,width=100,height=60)
Button(ven,text="Salir",command=Salir,font=("Corbel",16),bg="#EA1C9F").place(x=900,y=340,width=100,height=60)

##### Flecha de Posición Actual
Posición = Label(ven,text="↓",font=("Cambria Math",32))
Posición.place(x=xcoord.get(),y=60,width=90,height=38)

ven.mainloop()
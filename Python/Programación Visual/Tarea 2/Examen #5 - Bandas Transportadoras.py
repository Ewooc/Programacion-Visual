# Examen 5 - Bandas Transportadoras
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

from tkinter import *

ven = Tk()
ven.title("Bandas Transportadoras")
ven.geometry("740x340")

AcumuladorBanda1 = IntVar()
AcumuladorBanda2 = IntVar()
BandaActiva = StringVar()
Pieza = IntVar()

Pieza.set(0)
BandaActiva.set("1")


def Mover_Bandas():
    if BandaActiva.get() == "1":
        AcumuladorBanda1.set( AcumuladorBanda1.get() + Pieza.get() )
        Pieza.set(0)
    elif BandaActiva.get() == "2":
        AcumuladorBanda2.set( AcumuladorBanda2.get() + AcumuladorBanda1.get() )
        AcumuladorBanda1.set(0)

def Activar_Banda1():
    BandaActiva.set("1")
    Flecha1.config(text="→")
    Flecha2.config(text="| |")
    Mover_Bandas()

def Activar_Banda2():
    BandaActiva.set("2")
    Flecha1.config(text="| |")
    Flecha2.config(text="→")
    Mover_Bandas()

def Detener_Proceso():
    BandaActiva.set("Ninguna")
    Flecha1.config(text="| |")
    Flecha2.config(text="| |")

def Generar_Pieza():
    Pieza.set( Pieza.get() + 1 )
    Mover_Bandas()

def Vaciar():
    AcumuladorBanda2.set(0)

def Salir():
    ven.destroy()


################################### | IGU | ###################################

########## Entradas y Diseño #########################
Label(ven,bg="#B48E38").place(x=50,y=-10,width=100,height=40)
Generar = Button(ven,text="Generar Pieza",command=Generar_Pieza,font=("Corbel",12,"bold"),fg="#291D00",bg="#B48E38")
Generar.place(x=40,y=20,width=120,height=60)
Label(ven,bg="#291D00").place(x=38,y=18,width=124,height=4)
#Banda1
Label(ven,text="Banda 1",font=("Corbel",14)).place(x=40,y=190,width=280,height=30)
Label(ven,text="•",font=("Corbel",74),fg="#666666").place(x=15,y=152.5,height=40)
Label(ven,text="•",font=("Corbel",74),fg="#666666").place(x=295,y=152.5,height=40)
Label(ven,bg="#666666").place(x=40,y=160,width=280,height=30)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=32,y=161.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=99.5,y=161.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=167,y=161.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=234.5,y=161.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=302,y=161.5,width=25,height=23)
Flecha1 = Label(ven,text="→",font=("Corbel",32))
Flecha1.place(x=200,y=90,width=90,height=60)
#Banda2
Label(ven,text="Banda 2",font=("Corbel",14)).place(x=320,y=250,width=280,height=30)
Label(ven,text="•",font=("Corbel",74),fg="#666666").place(x=295,y=212.5,height=40)
Label(ven,text="•",font=("Corbel",74),fg="#666666").place(x=575,y=212.5,height=40)
Label(ven,bg="#666666").place(x=320,y=220,width=280,height=30)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=312,y=221.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=379.5,y=221.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=447,y=221.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=514.5,y=221.5,width=25,height=23)
Label(ven,text="•",font=("Corbel",50),fg="#3D3D3D",bg="#666666").place(x=582,y=221.5,width=25,height=23)
Flecha2 = Label(ven,text="| |",font=("Corbel",32))
Flecha2.place(x=475.5,y=151.5,width=60,height=60)


########## Salidas ###################################
Label(ven,bg="#B48E38").place(x=610,y=290,width=100,height=60)
Label(ven,text="Final",font=("Corbel",12,"bold"),fg="#291D00",bg="#B48E38").place(x=600,y=280,width=120,height=40)
Label(ven,bg="#291D00").place(x=598,y=318,width=124,height=4)
Label(ven,textvariable=Pieza,bg="#C4C4C4",font=("Cambria Math",12)).place(x=70,y=90,width=60,height=60)
Label(ven,textvariable=AcumuladorBanda1,bg="#C4C4C4",font=("Cambria Math",12)).place(x=345.5,y=151.5,width=60,height=60)
Label(ven,textvariable=AcumuladorBanda2,bg="#C4C4C4",font=("Cambria Math",12)).place(x=630,y=210,width=60,height=60)


########## Botones ###################################
Label(ven,text="Sensor de",font=("Corbel",12)).place(x=330.5,y=40,width=90,height=20)
Label(ven,bg="#FF5050").place(x=374.5,y=70,width=2,height=82)
Button(ven,text="Paso",command=Activar_Banda2,font=("Corbel",12),bg="#BCA4B2").place(x=330.5,y=60,width=90,height=30)

Label(ven,text="Sensor de",font=("Corbel",12)).place(x=615.5,y=98.5,width=90,height=20)
Label(ven,bg="#FF5050").place(x=659.5,y=128.5,width=2,height=82)
Button(ven,text="Fin",command=Activar_Banda1,font=("Corbel",12),bg="#BCA4B2").place(x=615.5,y=118.5,width=90,height=30)

Button(ven,text="Vaciar",command=Vaciar,font=("Corbel",12),bg="#AFE958").place(x=510,y=285,width=80,height=30)

Button(ven,text="Detener",command=Detener_Proceso,font=("Corbel",12),bg="#58BDE9").place(x=60,y=240,width=140,height=30)
Button(ven,text="Salir",command=Salir,font=("Corbel",12),bg="#F7864A").place(x=60,y=290,width=140,height=30)


ven.mainloop()

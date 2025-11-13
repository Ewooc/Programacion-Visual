from tkinter import *

ven = Tk()
ven.title("Divisor de Voltaje")
ven.geometry("720x530")

VDD = StringVar()
RG1 = StringVar()
RG2 = StringVar()
RD = StringVar()
RS = StringVar()
IDSS = StringVar()
VP = StringVar()

VGSQ = DoubleVar()
IDQ = DoubleVar()
prefIDQ = StringVar()
prefVGSQ = StringVar()

def Calcular():
    Vdd = float(VDD.get().replace("K","e3").replace("M","e6").replace("m","e-3"))
    R1 = float(RG1.get().replace("K","e3").replace("M","e6").replace("m","e-3"))
    R2 = float(RG2.get().replace("K","e3").replace("M","e6").replace("m","e-3"))
    Rd = float(RD.get().replace("K","e3").replace("M","e6").replace("m","e-3"))
    # En realidad no se ocupa calcular Rd porque no se requiere en las fórmulas
    Rs = float(RS.get().replace("K","e3").replace("M","e6").replace("m","e-3"))
    Idss = float(IDSS.get().replace("K","e3").replace("M","e6").replace("m","e-3"))
    Vp = float(VP.get().replace("K","e3").replace("M","e6").replace("m","e-3"))

    l = Vp**2 / ( 2 * Rs * Idss )
    m = 2 * ( ( R2 / (R1 + R2 ) ) * Vdd - Vp )
    V = Vp - l + ( l**2 + l * m )**(1/2)
    signoV = 1
    signoI = 1
    if V < 0:
        signoV = -1
    I = (Idss * ( 1 - (V/Vp) )**2)
    if I < 0:
        signoI = -1

    I, pref1 = Determinar_Prefijo(abs(I))
    V, pref2 = Determinar_Prefijo(abs(V))

    IDQ.set( round(I*signoI,4) )
    VGSQ.set( round(V*signoV,4) )
    prefIDQ.set( f"{pref1}A" )
    prefVGSQ.set( f"{pref2}V" )

def Determinar_Prefijo(valor):
    if valor < 1e-1: ##### Menor a 1m
        Req = valor * 1e3
        pref = "m"
    elif valor < 1e3: ### Entre 1m y 1K
        Req = valor
        pref = ""
    else: ############ Mayor a 1K
        Req = valor / 1e3
        pref = "K"
    return Req, pref

def Salir():
    ven.destroy()

############################# | IGU | #############################

########## Diseño del Circuito
Label(ven,text="◦",font=("Corbel",36,"bold"),fg="#644574").place(x=160,y=70,width=20,height=28)
Label(ven,bg="#644574").place(x=168,y=94,width=3,height=20)

Label(ven,bg="#000000").place(x=90,y=114,width=150,height=3)

Label(ven,text="•",font=("Corbel",26)).place(x=82,y=275,width=20,height=20)
Label(ven,text="▶",font=("Corbel",26)).place(x=198,y=271,width=26,height=26)

Label(ven,bg="#000000").place(x=90,y=114,width=3,height=60) # R1
Label(ven,bg="#000000").place(x=90,y=224,width=3,height=60)
Label(ven,bg="#744545").place(x=84,y=174,width=16,height=3)
Label(ven,bg="#744545").place(x=84,y=224,width=16,height=3)
Label(ven,bg="#744545").place(x=84,y=174,width=3,height=50)
Label(ven,bg="#744545").place(x=97,y=174,width=3,height=50)

Label(ven,bg="#000000").place(x=90,y=284,width=3,height=60) # R2
Label(ven,bg="#000000").place(x=90,y=394,width=3,height=60)
Label(ven,bg="#744545").place(x=84,y=344,width=16,height=3)
Label(ven,bg="#744545").place(x=84,y=394,width=16,height=3)
Label(ven,bg="#744545").place(x=84,y=344,width=3,height=50)
Label(ven,bg="#744545").place(x=97,y=344,width=3,height=50)

Label(ven,bg="#000000").place(x=90,y=284,width=130,height=3) # Q1
Label(ven,bg="#000000").place(x=220,y=254,width=3,height=60)
Label(ven,bg="#000000").place(x=220,y=261,width=20,height=3)
Label(ven,bg="#000000").place(x=220,y=304,width=20,height=3)
Label(ven,text="Q1",font=("Corbel",14)).place(x=240,y=254,width=30,height=60)

Label(ven,bg="#000000").place(x=240,y=114,width=3,height=60) # RD
Label(ven,bg="#000000").place(x=240,y=224,width=3,height=40)
Label(ven,bg="#744545").place(x=234,y=174,width=16,height=3)
Label(ven,bg="#744545").place(x=234,y=224,width=16,height=3)
Label(ven,bg="#744545").place(x=234,y=174,width=3,height=50)
Label(ven,bg="#744545").place(x=247,y=174,width=3,height=50)

Label(ven,bg="#000000").place(x=240,y=304,width=3,height=40) # RS
Label(ven,bg="#000000").place(x=240,y=394,width=3,height=60)
Label(ven,bg="#744545").place(x=234,y=344,width=16,height=3)
Label(ven,bg="#744545").place(x=234,y=394,width=16,height=3)
Label(ven,bg="#744545").place(x=234,y=344,width=3,height=50)
Label(ven,bg="#744545").place(x=247,y=344,width=3,height=50)

Label(ven,bg="#000000").place(x=90,y=454,width=153,height=3)
Label(ven,bg="#000000").place(x=168,y=454,width=3,height=24)
Label(ven,bg="#000000").place(x=144,y=478,width=50,height=3)
Label(ven,bg="#000000").place(x=152,y=488,width=35,height=3)
Label(ven,bg="#000000").place(x=160,y=498,width=20,height=3)

########## Entradas
Label(ven,text="VDD",font=("Corbel",14)).place(x=140,y=10,width=60,height=30)
Entry(ven,textvariable=VDD,font=("Cambria Math",12),justify="center").place(x=140,y=40,width=60,height=30)

Label(ven,text="R1",font=("Corbel",14)).place(x=100,y=170,width=30,height=30)
Entry(ven,textvariable=RG1,font=("Cambria Math",12),justify="center").place(x=105,y=198,width=60,height=30)

Label(ven,text="R2",font=("Corbel",14)).place(x=100,y=340,width=30,height=30)
Entry(ven,textvariable=RG2,font=("Cambria Math",12),justify="center").place(x=105,y=368,width=60,height=30)

Label(ven,text="RD",font=("Corbel",14)).place(x=250,y=170,width=30,height=30)
Entry(ven,textvariable=RD,font=("Cambria Math",12),justify="center").place(x=255,y=198,width=60,height=30)

Label(ven,text="RS",font=("Corbel",14)).place(x=250,y=340,width=30,height=30)
Entry(ven,textvariable=RS,font=("Cambria Math",12),justify="center").place(x=255,y=368,width=60,height=30)

Label(ven,text="IDSS",font=("Corbel",14)).place(x=260,y=40,width=60,height=30)
Entry(ven,textvariable=IDSS,font=("Cambria Math",12),justify="center").place(x=320,y=40,width=60,height=30)

Label(ven,text="VP",font=("Corbel",14)).place(x=260,y=90,width=60,height=30)
Entry(ven,textvariable=VP,font=("Cambria Math",12),justify="center").place(x=320,y=90,width=60,height=30)

########## Salidas
Label(ven,text="IDQ = ",font=("Corbel",14),anchor="e",bg="#9172A0").place(x=360,y=240,width=80,height=30)
Label(ven,textvariable=IDQ,font=("Cambria Math",14),bg="#B299BF").place(x=440,y=240,width=160,height=30)
Label(ven,textvariable=prefIDQ,font=("Cambria Math",14),bg="#C3ADCF").place(x=600,y=240,width=40,height=30)

Label(ven,text="VGSQ = ",font=("Corbel",14),anchor="e",bg="#9172A0").place(x=360,y=300,width=80,height=30)
Label(ven,textvariable=VGSQ,font=("Cambria Math",14),bg="#B299BF").place(x=440,y=300,width=160,height=30)
Label(ven,textvariable=prefVGSQ,font=("Cambria Math",14),bg="#C3ADCF").place(x=600,y=300,width=40,height=30)

########## Botones
Button(ven,text="Calcular",command=Calcular,font=("Corbel",14),bg="#38A6EA").place(x=370,y=150,width=110,height=50)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#EAA938").place(x=520,y=150,width=110,height=50)

ven.mainloop()
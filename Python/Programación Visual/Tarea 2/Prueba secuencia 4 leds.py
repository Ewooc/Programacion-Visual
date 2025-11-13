from tkinter import *
from tkinter import messagebox
import threading # Para realizar funciones independientes
import random # Para una función aleatoria dedicada

ven=Tk()
ven.title("Secuencia Leds Simulada")
ven.geometry("700x650")


##### Variables Instrucciones
Instrucción1 = StringVar()
Tiempo1 = StringVar()
Instrucción2 = StringVar()
Tiempo2 = StringVar()
Instrucción3 = StringVar()
Tiempo3 = StringVar()
Instrucción4 = StringVar()
Tiempo4 = StringVar()
Instrucción5 = StringVar()
Tiempo5 = StringVar()
Instrucción6 = StringVar()
Tiempo6 = StringVar()
Instrucción7 = StringVar()
Tiempo7 = StringVar()
Instrucción8 = StringVar()
Tiempo8 = StringVar()
Instrucción9 = StringVar()
Tiempo9 = StringVar()
Instrucción10 = StringVar()
Tiempo10 = StringVar()
Instrucción11 = StringVar()
Tiempo11 = StringVar()
Instrucción12 = StringVar()
Tiempo12 = StringVar()
Instrucción13 = StringVar()
Tiempo13 = StringVar()
Instrucción14 = StringVar()
Tiempo14 = StringVar()
Instrucción15 = StringVar()
Tiempo15 = StringVar()
Instrucción16 = StringVar()
Tiempo16 = StringVar()
valoresinstrucción={"0","1"}
time = DoubleVar()


##### Entradas (definirlas ahora para poder manipularlas en una lista)
I1 = Entry(ven,textvariable=Instrucción1,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I1.place(x=40,y=80,width=85,height=30)
T1 = Entry(ven,textvariable=Tiempo1,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T1.place(x=130,y=80,width=80,height=30)

I2 = Entry(ven,textvariable=Instrucción2,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I2.place(x=40,y=115,width=85,height=30)
T2 = Entry(ven,textvariable=Tiempo2,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T2.place(x=130,y=115,width=80,height=30)

I3 = Entry(ven,textvariable=Instrucción3,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I3.place(x=40,y=150,width=85,height=30)
T3 = Entry(ven,textvariable=Tiempo3,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T3.place(x=130,y=150,width=80,height=30)

I4 = Entry(ven,textvariable=Instrucción4,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I4.place(x=40,y=185,width=85,height=30)
T4 = Entry(ven,textvariable=Tiempo4,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T4.place(x=130,y=185,width=80,height=30)

I5 = Entry(ven,textvariable=Instrucción5,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I5.place(x=40,y=220,width=85,height=30)
T5 = Entry(ven,textvariable=Tiempo5,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T5.place(x=130,y=220,width=80,height=30)

I6 = Entry(ven,textvariable=Instrucción6,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I6.place(x=40,y=255,width=85,height=30)
T6 = Entry(ven,textvariable=Tiempo6,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T6.place(x=130,y=255,width=80,height=30)

I7 = Entry(ven,textvariable=Instrucción7,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I7.place(x=40,y=290,width=85,height=30)
T7 = Entry(ven,textvariable=Tiempo7,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T7.place(x=130,y=290,width=80,height=30)

I8 = Entry(ven,textvariable=Instrucción8,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I8.place(x=40,y=325,width=85,height=30)
T8 = Entry(ven,textvariable=Tiempo8,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T8.place(x=130,y=325,width=80,height=30)

I9 = Entry(ven,textvariable=Instrucción9,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I9.place(x=40,y=360,width=85,height=30)
T9 = Entry(ven,textvariable=Tiempo9,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T9.place(x=130,y=360,width=80,height=30)

I10 = Entry(ven,textvariable=Instrucción10,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I10.place(x=40,y=395,width=85,height=30)
T10 = Entry(ven,textvariable=Tiempo10,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T10.place(x=130,y=395,width=80,height=30)

I11 = Entry(ven,textvariable=Instrucción11,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I11.place(x=40,y=430,width=85,height=30)
T11 = Entry(ven,textvariable=Tiempo11,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T11.place(x=130,y=430,width=80,height=30)

I12 = Entry(ven,textvariable=Instrucción12,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I12.place(x=40,y=465,width=85,height=30)
T12 = Entry(ven,textvariable=Tiempo12,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T12.place(x=130,y=465,width=80,height=30)

I13 = Entry(ven,textvariable=Instrucción13,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I13.place(x=40,y=500,width=85,height=30)
T13 = Entry(ven,textvariable=Tiempo13,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T13.place(x=130,y=500,width=80,height=30)

I14 = Entry(ven,textvariable=Instrucción14,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I14.place(x=40,y=535,width=85,height=30)
T14 = Entry(ven,textvariable=Tiempo14,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T14.place(x=130,y=535,width=80,height=30)

I15 = Entry(ven,textvariable=Instrucción15,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I15.place(x=40,y=570,width=85,height=30)
T15 = Entry(ven,textvariable=Tiempo15,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T15.place(x=130,y=570,width=80,height=30)

I16 = Entry(ven,textvariable=Instrucción16,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
I16.place(x=40,y=605,width=85,height=30)
T16 = Entry(ven,textvariable=Tiempo16,font=("Cambria Math",14),bg="#DCBDDF",state="normal",justify="center")
T16.place(x=130,y=605,width=80,height=30)


# Generar un temporizador globar para acceder a él desde cualquier función
global temporizador
temporizador: threading.Timer | None = None


# Para poder acceder a las instrucciones y los tiempos establecidos
instrucciones = [
    {"bits": Instrucción1, "tiempo": Tiempo1, "entradaI": I1, "entradaT": T1},  
    {"bits": Instrucción2, "tiempo": Tiempo2, "entradaI": I2, "entradaT": T2},  
    {"bits": Instrucción3, "tiempo": Tiempo3, "entradaI": I3, "entradaT": T3},  
    {"bits": Instrucción4, "tiempo": Tiempo4, "entradaI": I4, "entradaT": T4},  
    {"bits": Instrucción5, "tiempo": Tiempo5, "entradaI": I5, "entradaT": T5},  
    {"bits": Instrucción6, "tiempo": Tiempo6, "entradaI": I6, "entradaT": T6},  
    {"bits": Instrucción7, "tiempo": Tiempo7, "entradaI": I7, "entradaT": T7},  
    {"bits": Instrucción8, "tiempo": Tiempo8, "entradaI": I8, "entradaT": T8},  
    {"bits": Instrucción9, "tiempo": Tiempo9, "entradaI": I9, "entradaT": T9},  
    {"bits": Instrucción10, "tiempo": Tiempo10, "entradaI": I10, "entradaT": T10},  
    {"bits": Instrucción11, "tiempo": Tiempo11, "entradaI": I11, "entradaT": T11},
    {"bits": Instrucción12, "tiempo": Tiempo12, "entradaI": I12, "entradaT": T12},
    {"bits": Instrucción13, "tiempo": Tiempo13, "entradaI": I13, "entradaT": T13},
    {"bits": Instrucción14, "tiempo": Tiempo14, "entradaI": I14, "entradaT": T14},
    {"bits": Instrucción15, "tiempo": Tiempo15, "entradaI": I15, "entradaT": T15},
    {"bits": Instrucción16, "tiempo": Tiempo16, "entradaI": I16, "entradaT": T16},
]


def Verificar_Datos(): # Verificación de Datos
    pos = 0
    while pos < 16:
        item = instrucciones[pos]
        instrucciónactual = set(item["bits"].get())
        if not instrucciónactual.issubset(valoresinstrucción):
            messagebox.showerror("Error",f"La instrucción #{pos+1} es inválida\n"
                                 f"Solo permite '0' (apagado) y '1' (encendido)")
            return
        if len(item["bits"].get()) != 4:
            messagebox.showerror("Error",f"La instrucción #{pos+1} debe ser de 4 caracteres\n"
                                 f"Se ingresó '{item["bits"].get()}', de {len(item["bits"].get())} "
                                 f"caracter{"es" if len(item["bits"].get()) != 1 else ""}")
            return
        try:
            tiempoactual = float(item["tiempo"].get())
        except:
            messagebox.showerror("Error",f"El tiempo en la instrucción #{pos+1} no es un número\n"
                                 f"En su lugar, se ingresó '{item["tiempo"].get()}'")
            return
        if tiempoactual < 0 or tiempoactual > 5:
            messagebox.showerror("Error",f"El tiempo en la instrucción #{pos+1} es inválido\n"
                                 f"Solo se permiten tiempos de 0 a 5 segundos")
            return
        pos += 1
    ##### Si cumple, desactivar la entrada de datos antes de iniciar la secuencia
    pos = 0
    while pos < 16:
        item = instrucciones[pos]
        item["entradaI"].config( state="disabled" )
        item["entradaT"].config( state="disabled" )
        pos += 1
    BotónIniciar.place_forget()
    BotónDetener.place(x=235,y=510,width=205,height=50)
    Iniciar_Secuencia(0, Instrucción1.get(), float(Tiempo1.get()) if time.get() == 0 else time.get())


def Iniciar_Secuencia(num: int, instrucción: str, espera: float, ycoord=80): # Inicia la secuencia de instrucciones
    Flecha.place(y=ycoord)
    FocoA.config(fg="#ab9812" if instrucción[0] == "1" else "#555555")
    FocoB.config(fg="#ab9812" if instrucción[1] == "1" else "#555555")
    FocoC.config(fg="#ab9812" if instrucción[2] == "1" else "#555555")
    FocoD.config(fg="#ab9812" if instrucción[3] == "1" else "#555555")
    global temporizador
    if num < 0 or num+1 >= len(instrucciones): # Si es la última fila
        temporizador = threading.Timer(espera, Detener_Secuencia)
    else: # Seguir con la siguiente fila
        valorsiguiente = instrucciones[num + 1]["bits"].get()
        esperasiguiente = float(instrucciones[num + 1]["tiempo"].get() if time.get() == 0 else time.get())
        temporizador = threading.Timer(espera, Iniciar_Secuencia,
                                       args=(num + 1, valorsiguiente, esperasiguiente, ycoord + 35))
    temporizador.start()


def Detener_Secuencia(): # Detiene la secuencia de instrucciones
    global temporizador
    if temporizador:
        temporizador.cancel()
    BotónDetener.place_forget()
    BotónIniciar.place(x=235,y=510,width=205,height=50)
    # Volver a habilitar la entrada de datos
    pos = 0
    while pos < 16:
        item = instrucciones[pos]
        item["entradaI"].config( state="normal" )
        item["entradaT"].config( state="normal" )
        pos += 1
    # Reiniciar los Focos
    Flecha.place(y=45)
    FocoA.config(fg="#555555")
    FocoB.config(fg="#555555")
    FocoC.config(fg="#555555")
    FocoD.config(fg="#555555")


def Vaciar(): # Deja todo en 0
    Detener_Secuencia()
    pos = 0
    while pos < 16:
        item = instrucciones[pos]
        item["bits"].set( "0000" )
        item["tiempo"].set( "1.0" )
        pos += 1


def Aleatorio(): # Genera valores al azar
    Detener_Secuencia()
    pos = 0
    while pos < 16:
        item = instrucciones[pos]
        bit1 = str(random.randint(0,1))
        bit2 = str(random.randint(0,1))
        bit3 = str(random.randint(0,1))
        bit4 = str(random.randint(0,1))
        item["bits"].set( bit1 + bit2 + bit3 + bit4 )
        item["tiempo"].set( str(random.randrange(10,50,5)/10) )
        pos += 1


def Salir(): # Cierra la ventana
    ven.destroy()


############################################# | IGU | #############################################

##### Recuadro
Label(ven,bg="#000000").place(x=5,y=5,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=40,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=75,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=110,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=145,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=180,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=215,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=250,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=285,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=320,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=355,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=390,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=425,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=460,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=495,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=530,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=565,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=600,width=210,height=5)
Label(ven,bg="#000000").place(x=5,y=635,width=210,height=5)

Label(ven,bg="#000000").place(x=5,y=5,width=5,height=635)
Label(ven,bg="#000000").place(x=35,y=40,width=5,height=600)
Label(ven,bg="#000000").place(x=125,y=40,width=5,height=600)
Label(ven,bg="#000000").place(x=210,y=5,width=5,height=635)

Label(ven,text="Serie de Comandos",font=("Corbel",14,"bold"),bg="#8A5B90").place(x=10,y=10,width=200,height=30)
Label(ven,text="#",font=("Corbel",14,"bold"),bg="#AD7FB3").place(x=10,y=45,width=25,height=30)
Label(ven,text="Instrucción",font=("Corbel",12,"bold"),bg="#AD7FB3").place(x=40,y=45,width=85,height=30)
Label(ven,text="Tiempo (s)",font=("Corbel",12,"bold"),bg="#AD7FB3").place(x=130,y=45,width=80,height=30)

Label(ven,text="1",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=80,width=25,height=30)
Label(ven,text="2",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=115,width=25,height=30)
Label(ven,text="3",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=150,width=25,height=30)
Label(ven,text="4",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=185,width=25,height=30)
Label(ven,text="5",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=220,width=25,height=30)
Label(ven,text="6",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=255,width=25,height=30)
Label(ven,text="7",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=290,width=25,height=30)
Label(ven,text="8",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=325,width=25,height=30)
Label(ven,text="9",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=360,width=25,height=30)
Label(ven,text="10",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=395,width=25,height=30)
Label(ven,text="11",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=430,width=25,height=30)
Label(ven,text="12",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=465,width=25,height=30)
Label(ven,text="13",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=500,width=25,height=30)
Label(ven,text="14",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=535,width=25,height=30)
Label(ven,text="15",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=570,width=25,height=30)
Label(ven,text="16",font=("Cambria Math",14),bg="#C297C7",justify="right").place(x=10,y=605,width=25,height=30)


##### Salidas
FocoA = Label(ven,text="•",font=("Corbel", 180),fg="#555555",anchor="center")
FocoA.place(x=230,y=95,width=100,height=100)
Label(ven,text="A",font=("Corbel", 36)).place(x=230,y=200,width=100,height=50)

FocoB = Label(ven,text="•",font=("Corbel", 180),fg="#555555",anchor="center")
FocoB.place(x=350,y=95,width=100,height=100)
Label(ven,text="B",font=("Corbel", 36)).place(x=350,y=200,width=100,height=50)

FocoC = Label(ven,text="•",font=("Corbel", 180),fg="#555555",anchor="center")
FocoC.place(x=470,y=95,width=100,height=100)
Label(ven,text="C",font=("Corbel", 36)).place(x=470,y=200,width=100,height=50)

FocoD = Label(ven,text="•",font=("Corbel", 180),fg="#555555",anchor="center")
FocoD.place(x=590,y=95,width=100,height=100)
Label(ven,text="D",font=("Corbel", 36)).place(x=590,y=200,width=100,height=50)

Flecha = Label(ven,text="<",font=("Corbel",12,"bold"))
Flecha.place(x=215,y=45,width=16,height=30)


##### Botones
Label(ven,text="Tiempo de Espera",font=("Corbel", 14)).place(x=240,y=300)
Radiobutton(ven,text="Libre",font=("Corbel", 12),variable=time,value=0).place(x=250,y=330)
Radiobutton(ven,text="0.5 segundos",font=("Corbel", 12),variable=time,value=0.5).place(x=250,y=355)
Radiobutton(ven,text="1 segundo",font=("Corbel", 12),variable=time,value=1).place(x=250,y=380)
Radiobutton(ven,text="2 segundos",font=("Corbel", 12),variable=time,value=2).place(x=250,y=405)
Radiobutton(ven,text="3 segundos",font=("Corbel", 12),variable=time,value=3).place(x=250,y=430)
Radiobutton(ven,text="4 segundos",font=("Corbel", 12),variable=time,value=4).place(x=250,y=455)

BotónIniciar = Button(ven,text="Iniciar",command=Verificar_Datos,font=("Corbel", 14),bg="#48D84A")
BotónDetener = Button(ven,text="Detener",command=Detener_Secuencia,font=("Corbel", 14),bg="#48D890")

Button(ven,text="Aleatorio",command=Aleatorio,font=("Corbel", 14),bg="#4882D8").place(x=470,y=510,width=205,height=50)
Button(ven,text="Vaciar",command=Vaciar,font=("Corbel", 14),bg="#D8D648").place(x=235,y=580,width=205,height=50)
Button(ven,text="Salir",command=Salir,font=("Corbel", 14),bg="#D84D48").place(x=470,y=580,width=205,height=50)

time.set(0)
Vaciar() # Ejecutar la función al iniciar el programa

ven.mainloop()

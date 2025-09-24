from tkinter import *
ventana = Tk()
ventana.title("IGU aproximada a imagen")
ventana.geometry("500x200")

##### Definir Variables #####
F = DoubleVar()
C = DoubleVar()
L = DoubleVar()
R = DoubleVar()

##### Ventana Principal #####
Label(ventana,text="impedance of the RLC circuit in series",fg="dark cyan",bg="white").place(x="5",y="5",width="490",height="30")

##### Widgets #####
Label(ventana,text="Frequency f:").place(x="5",y="45",width="75",height="30") ### Frecuencia #############
Entry(ventana,textvariable=F,bg="white").place(x="85",y="45",width="390",height="30")
Label(ventana,text="Hz").place(x="475",y="45",width="20",height="30")

Label(ventana,text="Capacity C:").place(x="5",y="85",width="75",height="30") ### Capacitancia ############
Entry(ventana,textvariable=C,bg="white").place(x="85",y="85",width="390",height="30")
Label(ventana,text="F").place(x="475",y="85",width="20",height="30")

Label(ventana,text="Inductance L:").place(x="5",y="125",width="75",height="30") ### Inductancia ##########
Entry(ventana,textvariable=L,bg="white").place(x="85",y="125",width="390",height="30")
Label(ventana,text="H").place(x="475",y="125",width="20",height="30")

Label(ventana,text="Resistance R:").place(x="5",y="165",width="75",height="30") ### Resistencia ##########
Entry(ventana,textvariable=R,bg="white").place(x="85",y="165",width="390",height="30")
Label(ventana,text="Ω").place(x="475",y="165",width="20",height="30")

ventana.mainloop() ### Bucle


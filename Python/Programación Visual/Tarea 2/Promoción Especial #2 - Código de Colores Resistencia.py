from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Código de Colores - Resistencias")
ventana.geometry("660x460")

A = IntVar()
B = IntVar()
C = IntVar()
R = DoubleVar()
Prefijo = StringVar()

def Banda_A(): ##### Para colorear banda A en la resistencia
    if A.get() == 0:
        Label(ventana,bg="Black").place(x=500,y=60,width=20,height=40)
    elif A.get() == 1:
        Label(ventana,bg="Maroon").place(x=500,y=60,width=20,height=40)
    elif A.get() == 2:
        Label(ventana,bg="Red").place(x=500,y=60,width=20,height=40)
    elif A.get() == 3:
        Label(ventana,bg="Orange").place(x=500,y=60,width=20,height=40)
    elif A.get() == 4:
        Label(ventana,bg="Yellow").place(x=500,y=60,width=20,height=40)
    elif A.get() == 5:
        Label(ventana,bg="Green").place(x=500,y=60,width=20,height=40)
    elif A.get() == 6:
        Label(ventana,bg="Blue").place(x=500,y=60,width=20,height=40)
    elif A.get() == 7:
        Label(ventana,bg="Purple").place(x=500,y=60,width=20,height=40)
    elif A.get() == 8:
        Label(ventana,bg="Gray").place(x=500,y=60,width=20,height=40)
    elif A.get() == 9:
        Label(ventana,bg="White").place(x=500,y=60,width=20,height=40)
    Calcular_Y_Notación()
    

def Banda_B(): ##### Para colorear banda B en la resistencia
    if B.get() == 0:
        Label(ventana,bg="Black").place(x=530,y=60,width=20,height=40)
    elif B.get() == 1:
        Label(ventana,bg="Maroon").place(x=530,y=60,width=20,height=40)
    elif B.get() == 2:
        Label(ventana,bg="Red").place(x=530,y=60,width=20,height=40)
    elif B.get() == 3:
        Label(ventana,bg="Orange").place(x=530,y=60,width=20,height=40)
    elif B.get() == 4:
        Label(ventana,bg="Yellow").place(x=530,y=60,width=20,height=40)
    elif B.get() == 5:
        Label(ventana,bg="Green").place(x=530,y=60,width=20,height=40)
    elif B.get() == 6:
        Label(ventana,bg="Blue").place(x=530,y=60,width=20,height=40)
    elif B.get() == 7:
        Label(ventana,bg="Purple").place(x=530,y=60,width=20,height=40)
    elif B.get() == 8:
        Label(ventana,bg="Gray").place(x=530,y=60,width=20,height=40)
    elif B.get() == 9:
        Label(ventana,bg="White").place(x=530,y=60,width=20,height=40)
    Calcular_Y_Notación()


def Banda_C(): ##### Para colorear banda C en la resistencia
    if C.get() == 0:
        Label(ventana,bg="Black").place(x=560,y=60,width=20,height=40)
    elif C.get() == 1:
        Label(ventana,bg="Maroon").place(x=560,y=60,width=20,height=40)
    elif C.get() == 2:
        Label(ventana,bg="Red").place(x=560,y=60,width=20,height=40)
    elif C.get() == 3:
        Label(ventana,bg="Orange").place(x=560,y=60,width=20,height=40)
    elif C.get() == 4:
        Label(ventana,bg="Yellow").place(x=560,y=60,width=20,height=40)
    elif C.get() == 5:
        Label(ventana,bg="Green").place(x=560,y=60,width=20,height=40)
    elif C.get() == 6:
        Label(ventana,bg="Blue").place(x=560,y=60,width=20,height=40)
    elif C.get() == 7:
        Label(ventana,bg="Purple").place(x=560,y=60,width=20,height=40)
    elif C.get() == 8:
        Label(ventana,bg="Gray").place(x=560,y=60,width=20,height=40)
    elif C.get() == 9:
        Label(ventana,bg="White").place(x=560,y=60,width=20,height=40)
    Calcular_Y_Notación()


def Calcular_Y_Notación(): ##### Obtiene valor de la resistencia y su unidad
    Resistencia = ( A.get() * 10 + B.get() ) * (10 ** C.get())
    if Resistencia < 1e3: # Entre 0 a 1K
        NuevaRes = Resistencia
        Prefijo.set("Ω")
    elif Resistencia < 1e6: # Entre 1K a 1M
        NuevaRes = Resistencia / 1e3
        Prefijo.set("KΩ")
    else: # Mayor a 1M
        NuevaRes = Resistencia / 1e6
        Prefijo.set("MΩ")
    R.set( round(NuevaRes,2) )


def Salir(): ##### Cierra la ventana
    salir = messagebox.askquestion("Saliendo . . .","Salir?")
    if salir == "yes":
        ventana.destroy()


############### Entradas
### Colores
Label(ventana,text="Colores",font=("Corbel",14),bg="#24D09D").place(x=10,y=10,width=80,height=30)
Label(ventana,text="Negro",font=("Corbel",12),bg="Black",fg="White").place(x=10,y=50,width=80,height=30)
Label(ventana,text="Café",font=("Corbel",12),bg="Maroon",fg="White").place(x=10,y=90,width=80,height=30)
Label(ventana,text="Rojo",font=("Corbel",12),bg="Red",fg="Black").place(x=10,y=130,width=80,height=30)
Label(ventana,text="Naranja",font=("Corbel",12),bg="Orange",fg="Black").place(x=10,y=170,width=80,height=30)
Label(ventana,text="Amarillo",font=("Corbel",12),bg="Yellow",fg="Black").place(x=10,y=210,width=80,height=30)
Label(ventana,text="Verde",font=("Corbel",12),bg="Green",fg="White").place(x=10,y=250,width=80,height=30)
Label(ventana,text="Azul",font=("Corbel",12),bg="Blue",fg="White").place(x=10,y=290,width=80,height=30)
Label(ventana,text="Violeta",font=("Corbel",12),bg="Purple",fg="White").place(x=10,y=330,width=80,height=30)
Label(ventana,text="Gris",font=("Corbel",12),bg="Gray",fg="Black").place(x=10,y=370,width=80,height=30)
Label(ventana,text="Blanco",font=("Corbel",12),bg="White",fg="Black").place(x=10,y=410,width=80,height=30)

### Primera Banda
Label(ventana,text="1° Banda",font=("Corbel",14),bg="#24D09D").place(x=100,y=10,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=0,bg="#808080").place(x=100,y=50,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=1,bg="#BF6060").place(x=100,y=90,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=2,bg="#FF8080").place(x=100,y=130,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=3,bg="#FFD280").place(x=100,y=170,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=4,bg="#FFFF80").place(x=100,y=210,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=5,bg="#60BF60").place(x=100,y=250,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=6,bg="#8080FF").place(x=100,y=290,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=7,bg="#BF60BF").place(x=100,y=330,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=8,bg="#BFBFBF").place(x=100,y=370,width=100,height=30)
Radiobutton(ventana,variable=A,command=Banda_A,value=9,bg="#DEDEDE").place(x=100,y=410,width=100,height=30)

### Segunda Banda
Label(ventana,text="2° Banda",font=("Corbel",14),bg="#24D09D").place(x=210,y=10,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=0,bg="#808080").place(x=210,y=50,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=1,bg="#BF6060").place(x=210,y=90,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=2,bg="#FF8080").place(x=210,y=130,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=3,bg="#FFD280").place(x=210,y=170,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=4,bg="#FFFF80").place(x=210,y=210,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=5,bg="#60BF60").place(x=210,y=250,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=6,bg="#8080FF").place(x=210,y=290,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=7,bg="#BF60BF").place(x=210,y=330,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=8,bg="#BFBFBF").place(x=210,y=370,width=100,height=30)
Radiobutton(ventana,variable=B,command=Banda_B,value=9,bg="#DEDEDE").place(x=210,y=410,width=100,height=30)

### Tercera Banda
Label(ventana,text="3° Banda",font=("Corbel",14),bg="#24D09D").place(x=320,y=10,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=0,bg="#808080").place(x=320,y=50,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=1,bg="#BF6060").place(x=320,y=90,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=2,bg="#FF8080").place(x=320,y=130,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=3,bg="#FFD280").place(x=320,y=170,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=4,bg="#FFFF80").place(x=320,y=210,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=5,bg="#60BF60").place(x=320,y=250,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=6,bg="#8080FF").place(x=320,y=290,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=7,bg="#BF60BF").place(x=320,y=330,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=8,bg="#BFBFBF").place(x=320,y=370,width=100,height=30)
Radiobutton(ventana,variable=C,command=Banda_C,value=9,bg="#DEDEDE").place(x=320,y=410,width=100,height=30)

### Resistencia
Label(ventana,text="Dibujo Resistencia",font=("Corbel",14),bg="#24D09D").place(x=460,y=10,width=160,height=30)
Label(ventana,bg="#4A4A4A").place(x=470,y=75,width=140,height=10)
Label(ventana,bg="#D8B477").place(x=490,y=60,width=100,height=40)
Label(ventana,bg="#000000").place(x=500,y=60,width=20,height=40)
Label(ventana,bg="#000000").place(x=530,y=60,width=20,height=40)
Label(ventana,bg="#000000").place(x=560,y=60,width=20,height=40)

############### Salidas
Label(ventana,text="Valor Resistencia",font=("Corbel",14),bg="#24D09D").place(x=460,y=120,width=160,height=30)
Label(ventana,textvariable=R,font=("Cambria Math",14),bg="#FFFFFF").place(x=460,y=160,width=110,height=30)
Label(ventana,textvariable=Prefijo,font=("Cambria Math",14),bg="#FFFFFF").place(x=580,y=160,width=40,height=30)

############### Comandos
Button(ventana,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=520,y=410,width=100,height=30)


R.set(0)
Prefijo.set("Ω")

messagebox.showinfo("Te damos la bienvenida!","Gracias por utilizar la calculadora")
ventana.mainloop()


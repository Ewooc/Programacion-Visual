from tkinter import *

ventana = Tk()
ventana.title("Código de Colores - Resistencias")
ventana.geometry("600x600")

A = IntVar()
B = IntVar()
C = IntVar()

def Banda_A():
    if A.get() == 0:
        Label(ventana,bg="Black").place(x=50,y=460,width=20,height=40)
    elif A.get() == 1:
        Label(ventana,bg="Maroon").place(x=50,y=460,width=20,height=40)
    elif A.get() == 2:
        Label(ventana,bg="Red").place(x=50,y=460,width=20,height=40)
    elif A.get() == 3:
        Label(ventana,bg="Orange").place(x=50,y=460,width=20,height=40)
    elif A.get() == 4:
        Label(ventana,bg="Yellow").place(x=50,y=460,width=20,height=40)
    elif A.get() == 5:
        Label(ventana,bg="Green").place(x=50,y=460,width=20,height=40)
    elif A.get() == 6:
        Label(ventana,bg="Blue").place(x=50,y=460,width=20,height=40)
    elif A.get() == 7:
        Label(ventana,bg="Purple").place(x=50,y=460,width=20,height=40)
    elif A.get() == 8:
        Label(ventana,bg="Gray").place(x=50,y=460,width=20,height=40)
    elif A.get() == 9:
        Label(ventana,bg="White").place(x=50,y=460,width=20,height=40)
    

def Banda_B():
    if B.get() == 0:
        Label(ventana,bg="Black").place(x=80,y=460,width=20,height=40)
    elif B.get() == 1:
        Label(ventana,bg="Maroon").place(x=80,y=460,width=20,height=40)
    elif B.get() == 2:
        Label(ventana,bg="Red").place(x=80,y=460,width=20,height=40)
    elif B.get() == 3:
        Label(ventana,bg="Orange").place(x=80,y=460,width=20,height=40)
    elif B.get() == 4:
        Label(ventana,bg="Yellow").place(x=80,y=460,width=20,height=40)
    elif B.get() == 5:
        Label(ventana,bg="Green").place(x=80,y=460,width=20,height=40)
    elif B.get() == 6:
        Label(ventana,bg="Blue").place(x=80,y=460,width=20,height=40)
    elif B.get() == 7:
        Label(ventana,bg="Purple").place(x=80,y=460,width=20,height=40)
    elif B.get() == 8:
        Label(ventana,bg="Gray").place(x=80,y=460,width=20,height=40)
    elif B.get() == 9:
        Label(ventana,bg="White").place(x=80,y=460,width=20,height=40)


def Banda_C():
    if C.get() == 0:
        Label(ventana,bg="Black").place(x=110,y=460,width=20,height=40)
    elif C.get() == 1:
        Label(ventana,bg="Maroon").place(x=110,y=460,width=20,height=40)
    elif C.get() == 2:
        Label(ventana,bg="Red").place(x=110,y=460,width=20,height=40)
    elif C.get() == 3:
        Label(ventana,bg="Orange").place(x=110,y=460,width=20,height=40)
    elif C.get() == 4:
        Label(ventana,bg="Yellow").place(x=110,y=460,width=20,height=40)
    elif C.get() == 5:
        Label(ventana,bg="Green").place(x=110,y=460,width=20,height=40)
    elif C.get() == 6:
        Label(ventana,bg="Blue").place(x=110,y=460,width=20,height=40)
    elif C.get() == 7:
        Label(ventana,bg="Purple").place(x=110,y=460,width=20,height=40)
    elif C.get() == 8:
        Label(ventana,bg="Gray").place(x=110,y=460,width=20,height=40)
    elif C.get() == 9:
        Label(ventana,bg="White").place(x=110,y=460,width=20,height=40)


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
Label(ventana,bg="#4A4A4A").place(x=20,y=475,width=140,height=10)
Label(ventana,bg="#D8B477").place(x=40,y=460,width=100,height=40)
Label(ventana,bg="#000000").place(x=50,y=460,width=20,height=40)
Label(ventana,bg="#000000").place(x=80,y=460,width=20,height=40)
Label(ventana,bg="#000000").place(x=110,y=460,width=20,height=40)

ventana.mainloop()
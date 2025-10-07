# Promoción Especial #4
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

from tkinter import *
from tkinter import messagebox

ven = Tk()
ven.title("Ubicación de las Zonas de Memoria")
ven.geometry("520x400")

### Entradas
tamañoROM = StringVar()
tamañoLibre = StringVar()
tamañoRAM = StringVar()
mROM = IntVar()
mLibre = IntVar()
mRAM = IntVar()

### Salidas
inicioROM = StringVar()
finROM = StringVar()
inicioLibre = StringVar()
finLibre = StringVar()
inicioRAM = StringVar()
finRAM = StringVar()


def Verificar_Datos(): ##### Primero verifica la entrada de datos
    
    ValoresPermitidos = ["256", "512", "1k", "2k", "4k", "8k", "16k", "32k", "64k"]
    
    ##### Si no se ingresó un valor
    if tamañoROM.get() == "":
        messagebox.showerror("No se ingresó ROM","Ingrese un tamaño para la ROM")
        return
    if tamañoLibre.get() == "":
        messagebox.showerror("No se ingresó Espacio Libre","Ingrese un tamaño para el Espacio Libre")
        return
    if tamañoRAM.get() == "":
        messagebox.showerror("No se ingresó RAM","Ingrese un tamaño para la RAM")
        return

    ##### Conversión de datos
    valorROM = tamañoROM.get()
    valorLibre = tamañoLibre.get()
    valorRAM = tamañoRAM.get()
    
    ##### Si los valores ingresados no son potencia de 2
    if valorROM not in ValoresPermitidos:
        messagebox.showerror("ROM Inválida", "El valor de ROM tiene que ser una potencia de 2")
        return
    if valorLibre not in ValoresPermitidos:
        messagebox.showerror("Espacio Libre Inválido", "El valor del Espacio Libre tiene que ser una potencia de 2")
        return
    if valorRAM not in ValoresPermitidos:
        messagebox.showerror("RAM Inválida", "El valor de RAM tiene que ser una potencia de 2")
        return

    ##### Multiplica el valor de k (1024)
    númeroROM = int( valorROM.replace("k", "") ) * mROM.get()
    númeroLibre = int( tamañoLibre.get().replace("k", "") ) * mLibre.get()
    númeroRAM = int( tamañoRAM.get().replace("k", "") ) * mRAM.get()
    if valorROM[ len(valorROM)-1 ] == "k":
        númeroROM = númeroROM * 1024 
    if valorLibre[ len(valorLibre)-1 ] == "k":
        númeroLibre = númeroLibre * 1024
    if valorRAM[ len(valorRAM)-1 ] == "k":
        númeroRAM = númeroRAM * 1024

    ##### Si los valores ingresados son menores a 256
    if númeroROM < 256:
        messagebox.showerror("ROM Insuficiente","El tamaño mínimo de la ROM es de 256")
        return
    if númeroLibre < 256:
        messagebox.showerror("Espacio Libre Insuficiente","El tamaño mínimo del Espacio Libre es de 256")
        return
    if númeroRAM < 256:
        messagebox.showerror("RAM Insuficiente","El tamaño mínimo de la RAM es de 256")
        return
    
    ##### Si la suma total es mayor a 64k
    if númeroROM + númeroLibre + númeroRAM > 65536:
        messagebox.showerror("Máximo Superado","El tamaño máximo del Mapa de Memoria es de 64k")
        return
    
    ##### Si todo está correcto, pasar a calcular
    Calcular_Ubicaciones(númeroROM,númeroLibre,númeroRAM)


def Calcular_Ubicaciones(ROM,Libre,RAM): ##### Después de hacer las verificaciones

    inicioROM.set("0000")
    finROM.set( hex(ROM-1)[2:].upper() )

    inicioLibre.set( hex(ROM)[2:].upper() )
    finLibre.set( hex(ROM+Libre-1)[2:].upper() )

    inicioRAM.set( hex(ROM+Libre)[2:].upper() )
    finRAM.set( hex(ROM+Libre+RAM-1)[2:].upper() )


def Salir():
    ven.destroy()


##### Entradas
Label(ven,text="Memoria ROM",bg="#B9CC9F").place(x=10,y=10,width=100,height=30)
Entry(ven,textvariable=tamañoROM,bg="#FFFFFF",justify="center").place(x=120,y=10,width=60,height=30)
Label(ven,text="Múltiplo",bg="#B9CC9F").place(x=190,y=10,width=60,height=30)
Radiobutton(ven,text="1",variable=mROM,value=1).place(x=260,y=10,height=30)
Radiobutton(ven,text="3",variable=mROM,value=3).place(x=300,y=10,height=30)
Radiobutton(ven,text="5",variable=mROM,value=5).place(x=340,y=10,height=30)
Radiobutton(ven,text="6",variable=mROM,value=6).place(x=380,y=10,height=30)
Radiobutton(ven,text="7",variable=mROM,value=7).place(x=420,y=10,height=30)
Radiobutton(ven,text="9",variable=mROM,value=9).place(x=460,y=10,height=30)

Label(ven,text="Espacio Libre",bg="#9FCCC9").place(x=10,y=50,width=100,height=30)
Entry(ven,textvariable=tamañoLibre,bg="#FFFFFF",justify="center").place(x=120,y=50,width=60,height=30)
Label(ven,text="Múltiplo",bg="#9FCCC9").place(x=190,y=50,width=60,height=30)
Radiobutton(ven,text="1",variable=mLibre,value=1).place(x=260,y=50,height=30)
Radiobutton(ven,text="3",variable=mLibre,value=3).place(x=300,y=50,height=30)
Radiobutton(ven,text="5",variable=mLibre,value=5).place(x=340,y=50,height=30)
Radiobutton(ven,text="6",variable=mLibre,value=6).place(x=380,y=50,height=30)
Radiobutton(ven,text="7",variable=mLibre,value=7).place(x=420,y=50,height=30)
Radiobutton(ven,text="9",variable=mLibre,value=9).place(x=460,y=50,height=30)

Label(ven,text="Memoria RAM",bg="#A39FCC").place(x=10,y=90,width=100,height=30)
Entry(ven,textvariable=tamañoRAM,bg="#FFFFFF",justify="center").place(x=120,y=90,width=60,height=30)
Label(ven,text="Múltiplo",bg="#A39FCC").place(x=190,y=90,width=60,height=30)
Radiobutton(ven,text="1",variable=mRAM,value=1).place(x=260,y=90,height=30)
Radiobutton(ven,text="3",variable=mRAM,value=3).place(x=300,y=90,height=30)
Radiobutton(ven,text="5",variable=mRAM,value=5).place(x=340,y=90,height=30)
Radiobutton(ven,text="6",variable=mRAM,value=6).place(x=380,y=90,height=30)
Radiobutton(ven,text="7",variable=mRAM,value=7).place(x=420,y=90,height=30)
Radiobutton(ven,text="9",variable=mRAM,value=9).place(x=460,y=90,height=30)

##### Salidas
Label(ven,text="Zona ROM",bg="#B9CC9F").place(x=20,y=140,width=120,height=80)
Label(ven,textvariable=inicioROM,bg="#C6D6AF").place(x=140,y=140,width=60,height=20)
Label(ven,text="inicio").place(x=200,y=140,height=20)
Label(ven,textvariable=finROM,bg="#C6D6AF").place(x=140,y=200,width=60,height=20)
Label(ven,text="fin").place(x=200,y=200,height=20)

Label(ven,text="Zona Libre",bg="#9FCCC9").place(x=20,y=220,width=120,height=80)
Label(ven,textvariable=inicioLibre,bg="#B8DDDA").place(x=140,y=220,width=60,height=20)
Label(ven,text="inicio").place(x=200,y=220,height=20)
Label(ven,textvariable=finLibre,bg="#B8DDDA").place(x=140,y=280,width=60,height=20)
Label(ven,text="fin").place(x=200,y=280,height=20)

Label(ven,text="Zona RAM",bg="#A39FCC").place(x=20,y=300,width=120,height=80)
Label(ven,textvariable=inicioRAM,bg="#B4B0D8").place(x=140,y=300,width=60,height=20)
Label(ven,text="inicio").place(x=200,y=300,height=20)
Label(ven,textvariable=finRAM,bg="#B4B0D8").place(x=140,y=360,width=60,height=20)
Label(ven,text="fin").place(x=200,y=360,height=20)

##### Botones
Button(ven,text="Calcular",command=Verificar_Datos,bg="#F9B62F").place(x=260,y=140,width=100,height=40)
Button(ven,text="Salir",command=Salir,bg="#D0235D").place(x=380,y=140,width=100,height=40)

mROM.set(1)
mLibre.set(1)
mRAM.set(1)

ven.mainloop()
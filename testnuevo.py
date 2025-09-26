from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Simulador")
ventana.geometry("520x280")

Voltaje = DoubleVar()
Material = IntVar()
CantidadFocos = IntVar()
ResistenciaFocos = IntVar()
TipoConexión = IntVar()
CorrienteI = DoubleVar()
Prefijo = StringVar()


def VerificarValor(): ##### Limita el voltaje de 0 a 400
    if Voltaje.get() <= 0:
        messagebox.showerror("No hay voltaje o es negativo","El voltaje debe ser mayor a 0")
    elif Voltaje.get() > 400:
        messagebox.showerror("Demasiado Voltaje","Voltaje máximo de 400V")
    else:
        Conexión_Y_Corriente()


def Conexión_Y_Corriente(): ##### Realiza todas las verificaciones de datos y calcula la corriente
    ### Para el Material
    if Material.get() == 1: # Cobre
        ResistenciaMaterial = 1.678e-8
    elif Material.get() == 2: # Plata
        ResistenciaMaterial = 1.586e-8
    elif Material.get() == 3: # Acero
        ResistenciaMaterial = 1.7e-7
    else:
        messagebox.showerror("Material?","No hay material seleccionado")
        return # Solo para que no siga con el proceso
    
    ### Para la Cantidad de Focos
    if CantidadFocos.get() == 0:
        messagebox.showerror("Cantidad?","Selecciona una cantidad de focos")
        return # Solo para que no siga con el proceso

    ### Para el Valor de Resistencia de los Focos
    if ResistenciaFocos.get() == 0:
        messagebox.showerror("Valor?","Selecciona valor de resistencia para los focos")
        return # Solo para que no siga con el proceso

    ### Para el Tipo de Conexión
    if TipoConexión.get() == 1: # Serie
        Req = (ResistenciaFocos.get() * CantidadFocos.get()) + ResistenciaMaterial
        multiplicador = 1 * CantidadFocos.get()
    elif TipoConexión.get() == 2: # Paralelo
        Req = (ResistenciaFocos.get() / CantidadFocos.get()) + ResistenciaMaterial
        multiplicador = 1 * CantidadFocos.get()
    else:
        messagebox.showerror("Tipo?","No hay tipo de conexión seleccionado")
        return # Solo para que no siga con el proceso
    
    ### Calcular Corriente
    Corriente = Voltaje.get() / Req
    
    ### Para Comprobar Potencia
    Pfocos = (Corriente ** 2) * (Req - ResistenciaMaterial)
    if ResistenciaFocos.get() == 144:
        Pnominal = 100 * multiplicador
    elif ResistenciaFocos.get() == 360:
        Pnominal = 40 * multiplicador
    elif ResistenciaFocos.get() == 720:
        Pnominal = 20 * multiplicador
    
    if Pnominal < Pfocos:
        messagebox.showwarning("Advertencia","La potencia es demasiada para los focos")
        CorrienteI.set(0)
        Prefijo.set("-")
    else:
        Determinar_Prefijo(Corriente)


def Determinar_Prefijo(Valor): ##### Hace la conversión a notación de ingeniería
    if Valor < 1e-5: # Menor a 1μ
        NuevoValor = Valor * 1e6
        Prefijo.set("μA")
    elif Valor < 1e-2: # Entre 1μ a 1m
        NuevoValor = Valor * 1e3
        Prefijo.set("mA")
    elif Valor < 1e3: # Entre 1m a 1K
        NuevoValor = Valor
        Prefijo.set("A")
    elif Valor < 1e6: # Entre 1K a 1M
        NuevoValor = Valor / 1e3
        Prefijo.set("KA")
    else: # Mayor a 1M
        NuevoValor = Valor / 1e6
        Prefijo.set("MA")
    CorrienteI.set( round(NuevoValor,2) )


def Salir(): ##### Cierra la ventana
    salir = messagebox.askquestion("Saliendo . . .","Salir?")
    if salir == "yes":
        ventana.destroy()


############### Entradas
Label(ventana,text="Material",font=("Corbel",16),bg="#A6E454").place(x=10,y=10,width=90,height=30)
Label(ventana,bg="#D4FAA3").place(x=10,y=40,width=90,height=100)
Radiobutton(ventana,text="Cobre",variable=Material,value=1,font=("Corbel",12),bg="#C68346").place(x=15,y=50,width=80,height=20) # Cobre = 1
Radiobutton(ventana,text="Plata",variable=Material,value=2,font=("Corbel",12),bg="#C4C4C4").place(x=15,y=80,width=80,height=20) # Plata = 2
Radiobutton(ventana,text="Acero",variable=Material,value=3,font=("Corbel",12),bg="#7B9AC9").place(x=15,y=110,width=80,height=20) # Acero = 3

Label(ventana,text="# de Focos",font=("Corbel",16),bg="#54E4AD").place(x=120,y=10,width=140,height=30)
Label(ventana,bg="#B8EED9").place(x=120,y=40,width=140,height=40)
Radiobutton(ventana,text="1",variable=CantidadFocos,value=1,font=("Cambria Math",12),bg="#6EEDBC").place(x=125,y=45,width=40,height=30)
Radiobutton(ventana,text="2",variable=CantidadFocos,value=2,font=("Cambria Math",12),bg="#6EEDBC").place(x=170,y=45,width=40,height=30)
Radiobutton(ventana,text="3",variable=CantidadFocos,value=3,font=("Cambria Math",12),bg="#6EEDBC").place(x=215,y=45,width=40,height=30)

Label(ventana,text="Resistencia de los Focos",font=("Corbel",16),bg="#BB54E4").place(x=280,y=10,width=230,height=30)
Label(ventana,bg="#D09BE5").place(x=280,y=40,width=230,height=40)
Radiobutton(ventana,text="100W",variable=ResistenciaFocos,value=144,font=("Cambria Math",12),bg="#CA6CEF").place(x=285,y=45,width=70,height=30)
Label(ventana,text="144Ω",font=("Cambria Math",8)).place(x=285,y=80,width=70,height=10)
Radiobutton(ventana,text="40W",variable=ResistenciaFocos,value=360,font=("Cambria Math",12),bg="#CA6CEF").place(x=360,y=45,width=70,height=30)
Label(ventana,text="360Ω",font=("Cambria Math",8)).place(x=360,y=80,width=70,height=10)
Radiobutton(ventana,text="20W",variable=ResistenciaFocos,value=720,font=("Cambria Math",12),bg="#CA6CEF").place(x=435,y=45,width=70,height=30)
Label(ventana,text="720Ω",font=("Cambria Math",8)).place(x=435,y=80,width=70,height=10)

Label(ventana,text="Tipo de Conexión:",font=("Corbel",16),bg="#DD637E").place(x=120,y=100,width=180,height=40)
Label(ventana,bg="#E39DAD").place(x=300,y=100,width=210,height=40)
Radiobutton(ventana,text="Serie",variable=TipoConexión,value=1,font=("Corbel",12),bg="#EA7C94").place(x=316,y=108,width=71,height=24) # Serie = 1
Radiobutton(ventana,text="Paralelo",variable=TipoConexión,value=2,font=("Corbel",12),bg="#EA7C94").place(x=403,y=108,width=91,height=24) # Paralelo = 2

Label(ventana,text="Voltaje (V)",font=("Corbel",16),bg="#6392DD").place(x=10,y=160,width=110,height=30)
Scale(ventana,variable=Voltaje,from_=0,to=400,orient=HORIZONTAL).place(x=130,y=152,width=160,height=60) ### Cambio de Entry a Scale

############### Salidas
Label(ventana,text="Corriente (I)",font=("Corbel",16),bg="#FFEF3E").place(x=10,y=210,width=110,height=30)
Label(ventana,textvariable=CorrienteI,font=("Cambria Math",12),bg="#FFFFFF").place(x=130,y=210,width=160,height=30)
Label(ventana,text="valor",font=("Corbel", 10)).place(x=130,y=240,width=160,height=20)
Label(ventana,textvariable=Prefijo,font=("Cambria Math",12),bg="#FFFFFF").place(x=300,y=210,width=30,height=30)
Label(ventana,text="unidad",font=("Corbel", 10)).place(x=291,y=240,width=50,height=20)

############### Comandos
Button(ventana,text="Calcular",command=VerificarValor,font=("Corbel",14),bg="#F9B62F").place(x=305,y=160,width=90,height=30)
Button(ventana,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=410,y=160,width=90,height=30)

Prefijo.set("-") # Para indicar el espacio destinado al elemento
CantidadFocos.set(0) # Para la verificación de datos
ResistenciaFocos.set(0) # Para la verificación de datos

#messagebox.showinfo("Te damos la bienvenida!","Gracias por utilizar la calculadora")
ventana.mainloop()

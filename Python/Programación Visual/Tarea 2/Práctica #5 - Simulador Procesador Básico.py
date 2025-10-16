#IGU practica operacion de un procesador basico
from tkinter import *
from tkinter import messagebox
import random as rng

win=Tk()
win.geometry("1920x1080")
win.title("IGU")
win.configure(bg="#F3F3F3")

binario={" ","0","1"}
Memoria_Principal=["","","","","","","",""]
Instruccion=StringVar()
Instruccion0 = StringVar()
Instruccion1 = StringVar()
Instruccion2 = StringVar()
Instruccion3 = StringVar()
Instruccion4 = StringVar()
Instruccion5 = StringVar()
Instruccion6 = StringVar()
Instruccion7 = StringVar()
Instruccion8 = StringVar()
PC=StringVar()
ACC=StringVar()
B=StringVar()
RI=StringVar()
Contador_Instruccion=IntVar()
i=IntVar()
k=IntVar()
i.set(0)
k.set(0)

PC.set(f"{bin(rng.randint(0,255))[2:].zfill(8)}")
ACC.set(f"{bin(rng.randint(0,255))[2:].zfill(8)}")
B.set(f"{bin(rng.randint(0,255))[2:].zfill(8)}")
RI.set(f"{bin(rng.randint(0,255))[2:].zfill(8)}")

def Cargar():
    dato=str(Instruccion.get())
    Digitos=set(dato)
    if Digitos.issubset(binario):
        if len(Instruccion.get())==8:
            if i.get()<8:
                Memoria_Principal[i.get()]=Instruccion.get()
                globals()[f"Instruccion{i.get()}"].set(Memoria_Principal[i.get()])
                i.set(i.get()+1)
                Contador_Instruccion.set(i.get())
                if Contador_Instruccion.get()==8:
                    Contador_Instruccion.set(0)
                    i.set(0)              
        else:
            messagebox.showerror("Error","Instruccion Invalida")
    else:
        messagebox.showerror("Error","No es binario")
        
def Reset_Memoria():
    i.set(0)
    Contador_Instruccion.set(0)
    j=0
    while j<len(Memoria_Principal):
        globals()[f"Instruccion{j}"].set("")
        Memoria_Principal[j]=""
        j+=1
def Reset_CPU():
    ACC.set("00000000")
    B.set("00000000")
    RI.set("00000000")
    PC.set("00000000")
    k.set(0)
def Salir():
    win.destroy()

def run():
    if k.get() == 8:
        k.set(0)
    PC.set(bin(k.get())[2:].zfill(8))
    RI.set(Memoria_Principal[k.get()])
    Operacion=RI.get()[:-6]
    if Operacion=="01":
        ACC.set(RI.get()[2:].zfill(8))
    elif Operacion=="10":
        if ACC.get()=="":
            B.set("00000000")
        else:
            B.set(ACC.get().zfill(8))
    elif Operacion=="11":
        acc=int(ACC.get(),2)
        b=int(B.get(),2)
        ACC.set(bin(acc+b)[2:].zfill(8))
    k.set(k.get()+1)
    print(PC.get())
    print(k.get())

#-----Entradas
#Memoria
#Labels memoria de arriba a abajo
Label(win,textvariable=Instruccion0,bg="#D67861",font="Bahnschrift 20").place(x=853,y=43,width=300,height=75)   #1 - rojo claro
Label(win,textvariable=Instruccion1,bg="#E09B5E",font="Bahnschrift 20").place(x=853,y=118,width=300,height=75)  #2 - naranja claro
Label(win,textvariable=Instruccion2,bg="#EAC05B",font="Bahnschrift 20").place(x=853,y=193,width=300,height=75)  #3 - amarillo dorado claro
Label(win,textvariable=Instruccion3,bg="#D7D35A",font="Bahnschrift 20").place(x=853,y=268,width=300,height=75)  #4 - amarillo verdoso claro
Label(win,textvariable=Instruccion4,bg="#9CCC66",font="Bahnschrift 20").place(x=853,y=343,width=300,height=75)  #5 - verde claro
Label(win,textvariable=Instruccion5,bg="#4CB289",font="Bahnschrift 20").place(x=853,y=418,width=300,height=75)  #6 - verde azulado claro
Label(win,textvariable=Instruccion6,bg="#4CA6B2",font="Bahnschrift 20").place(x=853,y=493,width=300,height=75)  #7 - cian claro
Label(win,textvariable=Instruccion7,bg="#4C79B2",font="Bahnschrift 20").place(x=853,y=568,width=300,height=75)  #8 - azul claro

#Cuadricula Tabla Memoria
Label(win,bg="#000000").place(x=1150,y=40,width=3,height=600) #Borde Lateral Derecho
Label(win,bg="#000000").place(x=850,y=40,width=3,height=600) #Borde Lateral Izquierdo
Label(win,bg="#000000").place(x=850,y=40,width=300,height=3) #Borde 1 (Superior)
Label(win,bg="#000000").place(x=850,y=115,width=300,height=3) #Borde 2
Label(win,bg="#000000").place(x=850,y=190,width=300,height=3) #Borde 3
Label(win,bg="#000000").place(x=850,y=265,width=300,height=3) #Borde 4
Label(win,bg="#000000").place(x=850,y=340,width=300,height=3) #Borde 5
Label(win,bg="#000000").place(x=850,y=415,width=300,height=3) #Borde 6
Label(win,bg="#000000").place(x=850,y=490,width=300,height=3) #Borde 7
Label(win,bg="#000000").place(x=850,y=565,width=300,height=3) #Borde 8
Label(win,bg="#000000").place(x=850,y=640,width=303,height=3) #Borde 9 (Inferior)

Entry(win,textvariable=Instruccion).place(x=880,y=650,width=270,height=30)
Label(win,textvariable=Contador_Instruccion).place(x=850,y=650,width=30,height=30)
#CPU
#Cuadro CPU
Label(win,text="CPU",bg="#F3F3F3",font=("Bahnschrift",30)).place(x=145,y=68,width=605,height=50)  
Label(win,bg="#000000").place(x=145,y=118,width=605,height=525)  
Label(win,bg="#4CA6B2").place(x=150,y=123,width=595,height=515)
Label(win,bg="#000000").place(x=158,y=131,width=579,height=269)    
Label(win,bg="#AEB8C5").place(x=160,y=133,width=575,height=265)  

Label(win,text="⟷",bg="#F3F3F3",font=("Bahnschrift", 60, "bold")).place(x=750,y=548,width=100,height=80)
Label(win,bg="#000000").place(x=598,y=546,width=139,height=84)
Label(win,text="Unidad \n de control",bg="#ABB6AB",font=("Bahnschrift", 20)).place(x=600,y=548,width=135,height=80)
Label(win,text="⟷",bg="#4CA6B2",font=("Bahnschrift", 60, "bold")).place(x=500,y=548,width=98,height=80)

Label(win,text="↑",bg="#4CA6B2",font=("Bahnschrift",60)).place(x=440,y=408,width=60,height=80)
Label(win,text="↑",bg="#4CA6B2",font=("Bahnschrift",60)).place(x=175,y=408,width=60,height=80)
Label(win,bg="#000000").place(x=173,y=486,width=329,height=144)
Label(win,bg="#4CA6B2").place(x=237,y=486,width=201,height=60)

Label(win,bg="#BB2E59").place(x=175,y=488,width=60,height=100)
Label(win,bg="#BB2E59").place(x=440,y=488,width=60,height=100)
Label(win,text="Unidad Logica Aritmetica\n(ALU)",bg="#BB2E59",font=("Bahnschrift",20)).place(x=175,y=548,width=325,height=80)

#-----Botones
Button(win,text="RESET",bg="#DD7D5B",command=Reset_Memoria).place(x=850,y=700,width=145,height=50)  #Boton Memoria
Button(win,text="CARGAR",bg="#70C257",command=Cargar).place(x=1005,y=700,width=145,height=50)       #Boton Memoria
Button(win, text="RUN", bg="#70C257", font="Bahnschrift 12", command=run).place(x=540, y=670, width=150, height=60)             #Boton CPU
Button(win, text="RESET", bg="#DD7D5B", font="Bahnschrift 12", command=Reset_CPU).place(x=372.5, y=670, width=150, height=60)   #Boton CPU
Button(win, text="SALIR", bg="#6DA9D6", font="Bahnschrift 12", command=Salir).place(x=205, y=670, width=150, height=60)         #Boton CPU

#-----Salidas
#Cuadro de Registros
Label(win,text="Registros",bg="#AEB8C5",font=("Bahnschrift",30)).place(x=170,y=143,width=230,height=50)
Label(win,bg="#A1A363").place(x=170,y=213,width=230,height=50)                                              #Registro PC
Label(win,text="PC",bg="#A1A363",font=("Bahnschrift",20)).place(x=185,y=218,width=30,height=40)
Label(win,textvariable=PC,bg="#C8CA7C",font=("Bahnschrift",20)).place(x=240,y=218,width=150,height=40)

Label(win,bg="#70B14B").place(x=170,y=323,width=230,height=50)                                              #Registro ACC
Label(win,text="ACC",bg="#70B14B",font=("Bahnschrift",20)).place(x=175,y=328,width=51,height=40)
Label(win,textvariable=ACC,bg="#93CE71",font=("Bahnschrift",20)).place(x=240,y=328,width=150,height=40)

Label(win,bg="#5980A7").place(x=495,y=213,width=230,height=50)                                              #Registro Ri
Label(win,text="RI",bg="#5980A7",font=("Bahnschrift",20)).place(x=500,y=218,width=30,height=40)
Label(win,textvariable=RI,bg="#7D9CBB",font=("Bahnschrift",20)).place(x=565,y=218,width=150,height=40)

Label(win,bg="#9254B6").place(x=495,y=323,width=230,height=50)                                              #Registro B
Label(win,text="B",bg="#9254B6",font=("Bahnschrift",20)).place(x=500,y=328,width=30,height=40)
Label(win,textvariable=B,bg="#AA84C0",font=("Bahnschrift",20)).place(x=565,y=328,width=150,height=40)
win.mainloop()

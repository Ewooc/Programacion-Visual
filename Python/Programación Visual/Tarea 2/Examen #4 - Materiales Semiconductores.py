# Examen 4 - Materiales Semiconductores
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

from tkinter import *
from tkinter import messagebox

ven = Tk()
ven.title("Materiales Semiconductores")
ven.geometry("370x380")

Material = StringVar()
Símbolo = StringVar()
Z = StringVar()
Tipo = StringVar()
Valencia = StringVar()
Aplicaciones = StringVar()

# Generar Diccionario para almacenar la información de los materiales
InfoMateriales = {
    "silicio": {
        "Símbolo": "Si",
        "Z": "14",
        "Tipo": "Metaloide",
        "Valencia": "4",
        "Aplicaciones": "Microelectrónica, Obleas CMOS, Celdas solares"
    },
    "germanio": {
        "Símbolo": "Ge",
        "Z": "32",
        "Tipo": "Metaloide",
        "Valencia": "4",
        "Aplicaciones": "Fotónica infrarroja, Detectores"
    },
    "fósforo": {
        "Símbolo": "P",
        "Z": "15",
        "Tipo": "No Metal",
        "Valencia": "5",
        "Aplicaciones": "Dopante donador en Si"
    },
    "antimonio": {
        "Símbolo": "Sb",
        "Z": "51",
        "Tipo": "Metaloide",
        "Valencia": "5",
        "Aplicaciones": "Dopante tipo n, Compuestos semiconductores"
    },
    "selenio": {
        "Símbolo": "Se",
        "Z": "34",
        "Tipo": "No Metal",
        "Valencia": "6",
        "Aplicaciones": "Fotodetección, Rectificadores fotoeléctricos"
    },
    "arsénico": {
        "Símbolo": "As",
        "Z": "33",
        "Tipo": "Metaloide",
        "Valencia": "5",
        "Aplicaciones": "Dopante tipo n, Componente en GaAs & InAs"
    },
    "cadmio": {
        "Símbolo": "Cd",
        "Z": "48",
        "Tipo": "Metal",
        "Valencia": "2",
        "Aplicaciones": "Compuestos (CdTe, CdSe) para PV y fotónica"
    },
    "carbono": {
        "Símbolo": "C",
        "Z": "6",
        "Tipo": "No Metal",
        "Valencia": "4",
        "Aplicaciones": "Grafeno: alta movilidad, Diamante: sensores"
    },
    "telurio": {
        "Símbolo": "Te",
        "Z": "52",
        "Tipo": "No Metal",
        "Valencia": "6",
        "Aplicaciones": "Compuestos fotovoltaicos (CdTe)"
    },
    "boro": {
        "Símbolo": "B",
        "Z": "5",
        "Tipo": "Metaloide",
        "Valencia": "3",
        "Aplicaciones": "Dopante tipo p esencial en Si"
    },
    "indio": {
        "Símbolo": "In",
        "Z": "49",
        "Tipo": "Metal",
        "Valencia": "3",
        "Aplicaciones": "Óxidos conductores transparentes"
    },
    "azufre": {
        "Símbolo": "S",
        "Z": "16",
        "Tipo": "No Metal",
        "Valencia": "6",
        "Aplicaciones": "Fotoelectrónica y fotocatálisis"
    },
    "arseniuro de galio": {
        "Símbolo": "GaAs",
        "Z": "N/A",
        "Tipo": "III-V compuesto",
        "Valencia": "8",
        "Aplicaciones": "RF / microondas, Láseres y fotodetectores"
    },
    "carburo de silicio": {
        "Símbolo": "SiC",
        "Z": "N/A",
        "Tipo": "Compuesto covalente de banda ancha",
        "Valencia": "8",
        "Aplicaciones": "Electrónica de potencia, Alta T, Sustratos"
    },
    "seleniuro de cadmio": {
        "Símbolo": "CdSe",
        "Z": "N/A",
        "Tipo": "II-VI compuesto",
        "Valencia": "8",
        "Aplicaciones": "Quantum dots, Fotodetectores, Displays"
    },
    "óxido de zinc": {
        "Símbolo": "ZnO",
        "Z": "N/A",
        "Tipo": "Óxido semiconductor",
        "Valencia": "8",
        "Aplicaciones": "LEDs UV, Sensores de gas, Fotocatálisis"
    },
    "arseniuro de indio": {
        "Símbolo": "InAs",
        "Z": "N/A",
        "Tipo": "III-V compuesto",
        "Valencia": "8",
        "Aplicaciones": "Detectores IR, Alta movilidad, Heteroestructuras"
    },
    "fosfuro de indio": {
        "Símbolo": "InP",
        "Z": "N/A",
        "Tipo": "III-V compuesto",
        "Valencia": "8",
        "Aplicaciones": "Láseres y moduladores para telecomunicaciones"
    },
    "fosfuro de galio": {
        "Símbolo": "GaP",
        "Z": "N/A",
        "Tipo": "III-V compuesto",
        "Valencia": "8",
        "Aplicaciones": "LEDs visibles, Fotónica, Sustratos"
    },
}


def MostrarInfo(): # Verifica y muestra la información del material ingresado
    if Material.get() == "":
        messagebox.showerror("Error","No se ingresó material")
        return
    MaterialSeleccionado = Material.get().lower()
    info = InfoMateriales.get(MaterialSeleccionado, None)
    if not info:
        messagebox.showerror("Error","Material Inválido")
        return
    Símbolo.set( info["Símbolo"] )
    Z.set( info["Z"] )
    Tipo.set( info["Tipo"] )
    Valencia.set( info["Valencia"] )
    Aplicaciones.set( info["Aplicaciones"] )


def MostrarMateriales(): # Muestra una lista de los materiales disponibles
    messagebox.showinfo("Materiales Disponibles",
                        "Silicio, Germanio, Fósforo,\n" \
                        "Antimonio, Selenio, Arsénico,\n" \
                        "Cadmio, Carbono, Telurio,\n" \
                        "Boro, Indio, Azufre,\n" \
                        "Arseniuro de galio,\n" \
                        "Carburo de silicio,\n" \
                        "Seleniuro de cadmio,\n" \
                        "Óxido de zinc,\n" \
                        "Arseniuro de indio,\n" \
                        "Fosfuro de indio,\n" \
                        "Fosfuro de galio")


def Salir(): # Cierra la ventana
    ven.destroy()


############ Entradas
Label(ven,text="Material",font=("Corbel",14),bg="#A6E454").place(x=10,y=10,width=100,height=40)
Entry(ven,textvariable=Material,font=("Cambria Math",14),bg="#C8E7A0").place(x=120,y=10,width=200,height=40)

############ Salidas
Label(ven,text="Símbolo",font=("Corbel",14),bg="#E454B6").place(x=10,y=110,width=120,height=30)
Label(ven,textvariable=Símbolo,font=("Cambria Math",20),bg="#E197C9").place(x=10,y=140,width=120,height=70)

Label(ven,text="Z",font=("Corbel",14),bg="#8B54E4").place(x=140,y=110,width=90,height=30)
Label(ven,textvariable=Z,font=("Cambria Math",20),bg="#A37AE6").place(x=140,y=140,width=90,height=70)

Label(ven,text="e⁻ Valencia",font=("Corbel",14),bg="#D6E454").place(x=240,y=110,width=120,height=30)
Label(ven,textvariable=Valencia,font=("Cambria Math",20),bg="#DDE68C").place(x=240,y=140,width=120,height=70)

Label(ven,text="Tipo:",font=("Corbel",14),bg="#54E4AA").place(x=10,y=220,width=350,height=30)
Label(ven,textvariable=Tipo,font=("Cambria Math",12),bg="#A7E4CC").place(x=10,y=250,width=350,height=40)

Label(ven,text="Aplicaciones",font=("Corbel",14),bg="#91BFCE").place(x=10,y=300,width=350,height=30)
Label(ven,textvariable=Aplicaciones,font=("Cambria Math",12),bg="#BADBE6").place(x=10,y=330,width=350,height=40)

############ Botones
Button(ven,text="i",command=MostrarMateriales,font=("Cambria Math",12),bg="#1BA2CF").place(x=330,y=10,width=24,height=24)
Button(ven,text="Ingresar",command=MostrarInfo,font=("Corbel",14),bg="#F9B62F").place(x=30,y=60,width=140,height=36)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=200,y=60,width=140,height=36)

# Inicia el programa marcando los espacios para la información
Símbolo.set("-")
Z.set("-")
Tipo.set("-")
Valencia.set("-")
Aplicaciones.set("-")

ven.mainloop()

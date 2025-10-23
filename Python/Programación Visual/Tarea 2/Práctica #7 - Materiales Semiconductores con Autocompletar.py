# Práctica 7 - Materiales Semiconductores con Autocompletar
# Woolfolk Cerecer Evan, 24331167
# Programación Visual, Grupo O3A

from tkinter import *
from tkinter import messagebox
from unidecode import unidecode # Librería para eliminar acentos en el texto
# Para importar, usar " pip install Unidecode "

ven = Tk()
ven.title("Materiales Semiconductores")
ven.geometry("740x400")

Material = StringVar()
MaterialMostrado = StringVar()
Símbolo = StringVar()
Z = StringVar()
Tipo = StringVar()
Valencia = StringVar()
Aplicaciones = StringVar()

MaterialesPosibles = StringVar() # No se muestran en pantalla
PrimerMaterial = StringVar()
SinCoincidencias = IntVar()

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


def MostrarMateriales(n, i, m): # Autocompleta de la lista de materiales disponibles
    MaterialABuscar = unidecode(Material.get().strip().lower())
    MaterialesFiltrados = [material for material in InfoMateriales
                           if unidecode(material.strip().lower()).startswith(MaterialABuscar)]
    MaterialesFiltrados.sort()
    if len(MaterialesFiltrados) > 0:
        SinCoincidencias.set(0)
        PrimerMaterial.set(MaterialesFiltrados[0])
        MaterialesPosibles.set("\n".join(MaterialesFiltrados))
    else:
        SinCoincidencias.set(1)
        MaterialesPosibles.set("[Sin Coincidencias]\n\n"
                            f"Quizá quisiste decir:\n{PrimerMaterial.get()}")


def MostrarInfo(): # Muestra la información del material ingresado o del anterior válido
    if Material.get() == "":
        messagebox.showwarning("Advertencia", f"No se Ingresó material, mostrando '{PrimerMaterial.get()}'")
    
    if SinCoincidencias.get() == 1:
        messagebox.showwarning("Advertencia",f"'{Material.get()}' no forma parte de la lista\n"
                               f"Mostrando en su lugar '{PrimerMaterial.get()}'")

    info = InfoMateriales.get(PrimerMaterial.get(), InfoMateriales["silicio"])
    MaterialMostrado.set( PrimerMaterial.get() )
    Símbolo.set( info["Símbolo"] )
    Z.set( info["Z"] )
    Tipo.set( info["Tipo"] )
    Valencia.set( info["Valencia"] )
    Aplicaciones.set( info["Aplicaciones"] )


def Salir(): # Cierra la ventana
    ven.destroy()


############ Entradas
Label(ven,text="Material",font=("Corbel",14),bg="#A6E454").place(x=10,y=10,width=100,height=40)
Entry(ven,textvariable=Material,font=("Cambria Math",14),bg="#C8E7A0").place(x=120,y=10,width=240,height=40)


############ Salidas
Label(ven,bg="#000000").place(x=370,y=10,width=1,height=380)
Label(ven,text="Coincidencias",font=("Corbel",14),bg="#54E4C7").place(x=10,y=60,width=350,height=30)
Label(ven,textvariable=MaterialesPosibles,font=("Corbel",10),bg="#97F4E1",anchor="n").place(x=10,y=90,width=350,height=300)

Label(ven,text="Material",font=("Corbel",14),bg="#A6E454").place(x=380,y=60,width=350,height=30)
Label(ven,textvariable=MaterialMostrado,font=("Cambria Math",14),bg="#C8E7A0").place(x=380,y=90,width=350,height=30)

Label(ven,text="Símbolo",font=("Corbel",14),bg="#E454B6").place(x=380,y=130,width=120,height=30)
Label(ven,textvariable=Símbolo,font=("Cambria Math",20),bg="#E197C9").place(x=380,y=160,width=120,height=70)

Label(ven,text="Z",font=("Corbel",14),bg="#8B54E4").place(x=510,y=130,width=90,height=30)
Label(ven,textvariable=Z,font=("Cambria Math",20),bg="#A37AE6").place(x=510,y=160,width=90,height=70)

Label(ven,text="e⁻ Valencia",font=("Corbel",14),bg="#D6E454").place(x=610,y=130,width=120,height=30)
Label(ven,textvariable=Valencia,font=("Cambria Math",20),bg="#DDE68C").place(x=610,y=160,width=120,height=70)

Label(ven,text="Tipo:",font=("Corbel",14),bg="#54E4AA").place(x=380,y=240,width=350,height=30)
Label(ven,textvariable=Tipo,font=("Cambria Math",12),bg="#A7E4CC").place(x=380,y=270,width=350,height=40)

Label(ven,text="Aplicaciones",font=("Corbel",14),bg="#91BFCE").place(x=380,y=320,width=350,height=30)
Label(ven,textvariable=Aplicaciones,font=("Cambria Math",12),bg="#BADBE6").place(x=380,y=350,width=350,height=40)


############ Botones
Button(ven,text="Ingresar",command=MostrarInfo,font=("Corbel",14),bg="#F9B62F").place(x=380,y=10,width=170,height=40)
Button(ven,text="Salir",command=Salir,font=("Corbel",14),bg="#D0235D").place(x=560,y=10,width=170,height=40)


# Inicia el programa marcando los espacios para la información
PrimerMaterial.set("silicio")
MaterialMostrado.set("-")
Símbolo.set("-")
Z.set("-")
Tipo.set("-")
Valencia.set("-")
Aplicaciones.set("-")

# Va mostrando las coincidencias activamente según se escribe el material
Material.trace_add("write", MostrarMateriales)

ven.mainloop()

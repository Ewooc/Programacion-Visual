from tkinter import *
from tkinter import messagebox
from unidecode import unidecode

ven = Tk()
ven.title("Test_New")
ven.geometry("440x220")

CosaABuscar = StringVar()
CosasPosibles = StringVar()
Cosa1 = StringVar()

Cosas = {
    "Amarillo",
    "Libro",
    "Papel",
    "Pluma",
    "Arcoiris",
    "Galleta",
    "leona",
    "leo la terraria wiki",
    "Gato",
    "Perro",
    "Espada",
    "Erizo",
    "Mapache",
    "Cuervo",
    "Hamster",
    "Computadora",
    "Mesa",
    "Casa",
    "Azul",
    "Rojo",
    "Refresco",
    "León",
    "Bola",
    "Dado",
    "Fantasma",
    "Gas",
    "Disruptor de partículas 3-X",
    "Tanque",
    "Bazuca",
    "Rastrillo",
    "Trapo",
    "Borrador",
    "Avión",
    "Barco",
    "Columpio",
    "Parque",
    "Castillo",
    "Mochila",
    "Lombriz",
    "Impresora",
    "Iridio",
    "Holograma",
    "Tungsteno",
    "Imán",
    "Carta",
    "Ladrillo",
    "Piedra",
    "Verde",
    "Luz",
    "Nieve",
    "Nota"
}

Caosas = {
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


def obtener_filtro(filtro: str):
    #if filtro == "":
    #    return Cosas
    
    # "aplanar" el texto de busqueda
    filtro = unidecode(filtro.strip().lower())
    Cosas_filtradas = [Cosa for Cosa in Cosas
                       # "aplanamos" los valores disponibles y revisamos si es válido
                       if unidecode(Cosa.strip().lower()).startswith(filtro)]
    Cosas_filtradas.sort()
    
    if len(Cosas_filtradas) > 0:
        PrimeraCosa = Cosas_filtradas[0]
        Cosa1.set(PrimeraCosa)

    ### Agregar sugerencia de último valor válido, como: quiza quisiste decir arcoiris cuando escribes arco iris
    return Cosas_filtradas


def revisar_valor(n, i, m):
    # esta funcion se activa cuando el valor de Cosaabuscar cambia
    valor_actual = CosaABuscar.get()
    lista_de_busqueda = obtener_filtro(valor_actual)

    if lista_de_busqueda==[]:
        print("[Sin Coincidencias]")
        CosasPosibles.set("[Sin Coincidencias]\n"
                          "Mostrando resultado para:\n" \
                          +Cosa1.get())
        #messagebox.showwarning("Advertencia","Sin Coincidencias")
    else:
        print("\n".join(lista_de_busqueda))
        CosasPosibles.set("\n".join(lista_de_busqueda))
    print("#####################################")


Entry(ven,textvariable=CosaABuscar,bg="#B2DEC1").place(x=10,y=10,width=160,height=30)
Label(ven,textvariable=CosasPosibles,bg="#52CE7B").place(x=10,y=50,width=160)
Label(ven,textvariable=Cosa1).place(x=200,y=10,width=160)

CosaABuscar.trace_add("write", revisar_valor)
# Entry.onInput(filtrados)


ven.mainloop()
# import tkinter

# root = tkinter.Tk()  # Create main window

# root.title("Font Example in Tkinter")
# root.geometry("400x240")

# txt = tkinter.Text(root, height=10, font=("Verdana", 18, "italic"))
# txt.pack()
# root.mainloop()


Materiales = {
    "Silicio": {
        "simbolo": "Si",
        "z": "14",
        "tipo": "Metaloide",
        "e": "4",
        "aplicaciones": "Se utiliza en aleaciones, en la decantación de las "
            "siliconas, en la industria de la cerámica técnica y, "
            "debido a que es un material semiconductor muy abundante, "
            "tiene un interés especial en la industria electrónica y "
            "microelectrónica como material básico para la creación de "
            "obleas o chips que se pueden implantar en transistores, "
            "pilas solares y una gran variedad de circuitos electrónicos."
    },
    "Metal2": {
        "simbolo": "Si",
        "z": "14",
        "tipo": "Metaloide",
        "e": "4",
        "aplicaciones": "Se utiliza en aleaciones, en la decantación de las "
            "siliconas, en la industria de la cerámica técnica y, "
            "debido a que es un material semiconductor muy abundante, "
            "tiene un interés especial en la industria electrónica y "
            "microelectrónica como material básico para la creación de "
            "obleas o chips que se pueden implantar en transistores, "
            "pilas solares y una gran variedad de circuitos electrónicos."
    },
}

#print(Materiales)

for material in Materiales:
    print(material + ">>")
    for propiedad in Materiales[material]:
        print("\t" + propiedad + ": " + str(Materiales[material][propiedad]))
    print()
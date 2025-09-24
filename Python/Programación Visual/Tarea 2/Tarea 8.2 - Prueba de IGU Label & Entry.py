# Prueba - Tarea 8

from tkinter import * # Importar todas las funciones de Tkinter
ventana = Tk()        # Generar ventana de nombre "ventana"
ventana.title("Test") # Asignar título "Test" a "ventana"
ventana.geometry("360x160") # Determinar resolución a "ventana"
#/// Widgets
R = IntVar()
Label(ventana,text="Resistencia:").place(x=10,y=24,width=120,height=60)
Entry(ventana,textvariable=R,bg="white").place(x=140,y=24,width=180,height=60)
#///
ventana.mainloop() # Permite repetir todo en "ventana", esencial al final del código


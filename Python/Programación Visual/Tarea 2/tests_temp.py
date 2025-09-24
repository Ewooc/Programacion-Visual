import tkinter

root = tkinter.Tk()  # Create main window

root.title("Font Example in Tkinter")
root.geometry("400x240")

txt = tkinter.Text(root, height=10, font=("Verdana", 18, "italic"))
txt.pack()
root.mainloop()
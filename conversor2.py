from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.title = "Conversor"

mainframe = ttk.Frame(ventana, padding = "8")
mainframe.grid(column = 0, row = 0, sticky=(W, N, E, S))

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

monto = StringVar()
montoIngreso = ttk.Entry(mainframe, width = 12, textvariable = monto)
montoIngreso.grid(column = 2, row = 1, sticky = (W, E))

dolares = ttk.Label(mainframe, text = "0")
dolares.grid(column = 2, row = 2)

euros = ttk.Label(mainframe, text = "0")
euros.grid(column = 2, row = 3)

reales = ttk.Label(mainframe, text = "0")
reales.grid(column = 2, row = 4)

ttk.Label(mainframe, text = "Pesos: ").grid(column = 1, row = 1, sticky = E)
ttk.Label(mainframe, text = "Dolares: ").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "Euros: ").grid(column = 1, row = 3, sticky = E)
ttk.Label(mainframe, text = "Reales: ").grid(column = 1, row = 4, sticky = E)

def ejecucion():
    pesos = int(montoIngreso.get())
    
    dolares.configure(text = str(round((pesos / 150), 2)))
    euros.configure(text = str(round((pesos / 183), 2)))
    reales.configure(text = str(round((pesos / 16.57), 2)))

ttk.Button(mainframe, text = "Convertir", command = ejecucion).grid(column = 3, row = 4, sticky = W)

menu = Menu(ventana)
menu.add_command(label = "Salir", command = ventana.destroy)
ventana.config(menu = menu)

ventana.mainloop()
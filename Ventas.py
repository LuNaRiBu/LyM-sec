from tkinter import*
from tkinter import messagebox
from tkinter import font


app = Tk()

producto_text = StringVar()
producto_Label = Label(app, text = "Producto", font = ("blod", 12))
producto_Label.grid(row = 0, column=0, sticky=W)
producto_entry = Entry(app, textvariable= producto_text)
producto_entry.grid(row= 0, column= 1)

cliente_text = StringVar()
cliente_Label = Label(app, text = "Cliente", font = ("blod", 12))
cliente_Label.grid(row = 0, column= 2, sticky=W)
cliente_entry = Entry(app, textvariable= producto_text)
cliente_entry.grid(row= 0, column= 3)

vendedor_text = StringVar()
vendedor_Label = Label(app, text = "Vendedor", font = ("blod", 12))
vendedor_Label.grid(row = 1, column= 0, sticky=W)
vendedor_entry = Entry(app, textvariable= producto_text)
vendedor_entry.grid(row= 1, column= 1)






app.title("Organización Lamia")
app.geometry("700x350")
app.mainloop()
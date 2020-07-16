import parser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title("JSON Parser")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
keylist = parser.findKeys(root.filename)

ttk.Label(mainframe, text= "Choose a key").grid(column=0, row=0, sticky=(W, E))

keyselection = StringVar()
keys = ttk.Combobox(textvariable = keyselection)
keys['values'] = keylist
keys.grid(column = 1, row = 0) 
keys.current() 






root.mainloop()

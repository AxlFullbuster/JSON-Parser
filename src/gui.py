import parser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class parserGUI:
	def __init__(self, master):
		self.master = master
		master.title("JSON Parser")
		
		self.mainframe = ttk.Frame(master, padding="5 5 12 12")
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		
		master.filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
		self.keylist = parser.findKeys(master.filename)
		
		ttk.Label(self.mainframe, text= "Key to search:  ").grid(column = 0 , row = 0, sticky=(N,W))
		self.keysearch = StringVar()
		self.key_search = ttk.Combobox(self.mainframe, textvariable = self.keysearch)
		self.key_search.bind('<<ComboboxSelected>>', self.find)
		self.key_search['values'] = self.keylist
		self.key_search.grid(column = 1, row = 0)
		
		
		ttk.Label(self.mainframe, text= "Key to extract:  ").grid(column = 0, row = 1, sticky=(N,W))
		self.keyextract = StringVar()
		self.key_extract = ttk.Combobox(self.mainframe, textvariable = self.keyextract)
		self.key_extract.bind('<<ComboboxSelected>>', self.find)
		self.key_extract['values'] = self.keylist
		self.key_extract.grid(column = 1, row = 1)
		
		self.search = self.key_search.current(0)
		self.extract = self.key_extract.current(0)
		
		
	
	def find(self, event):
		self.search = self.key_search.get()
		self.extract = self.key_extract.get()
		
		print(self.search)
		print(self.extract)
		
	

root = Tk()
my_gui = parserGUI(root)
root.mainloop()


import os
import tkinter as tk
from parser import FileParser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class ParserGUI:
	def __init__(self, master):
		self.master = master
		master.title("JSON Parser")
		
		self.mainframe = ttk.Frame(master, padding="5 5 12 12")
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		
		self.keylist = list()
		file_button = ttk.Button(self.mainframe, text = "Load New File", command = self.new_file)
		file_button.grid(column = 3, row = 3, sticky = (E))
		
		self.name = ttk.Label(self.mainframe)
		self.name.grid(column = 5, row = 3)
		
		
		ttk.Label(self.mainframe, text= "Key to search:  ").grid(column = 0 , row = 0, sticky=(N,W))
		keysearch = StringVar()
		self.key_search = ttk.Combobox(self.mainframe, textvariable = keysearch)
		self.key_search['values'] = self.keylist
		self.key_search.grid(column = 1, row = 0)
		
		
		ttk.Label(self.mainframe, text= "Key to extract:  ").grid(column = 0, row = 1, sticky=(N,W))
		keyextract = StringVar()
		self.key_extract = ttk.Combobox(self.mainframe, textvariable = keyextract)
		self.key_extract['values'] = self.keylist
		self.key_extract.grid(column = 1, row = 1)
		
		user_input = ttk.Label(self.mainframe, text="Content to look for: ")
		user_input.grid(column = 0, row = 2)
		
		self.user_string = StringVar()
		string_input = ttk.Entry(self.mainframe, textvariable = self.user_string)
		string_input.grid(column = 1, row = 2)
		
		
		search_button = ttk.Button(self.mainframe, text = "Search", command = self.find)
		search_button.grid(column = 0, row = 3, sticky = (W))
		
		self.results = tk.Text(master, height = 5, width = 100)
		self.results.grid(column = 0, row = 4, sticky=(N,S,E,W))
		
		scroll = ttk.Scrollbar(master, command = self.results.yview)
		scroll.grid(column = 1, row = 4, sticky=(N,S,E,W))
		self.results['yscrollcommand'] = scroll.set

		
	def find(self):
		search = self.key_search.get()
		extract = self.key_extract.get()
		uinput = self.user_string.get()
		
		self.content = self.parser.parse(search, extract, uinput)
		
		self.results.delete(1.0, tk.END)
		
		for x in self.content:
			self.results.insert(tk.END, x + '\n')
			
	
	def new_file(self):
		self.master.filename = filedialog.askopenfilename(initialdir = "./json",
														  title = "Select file",
														  filetypes = (("json files","*.json"),
														("all files","*.*")))
		
		self.parser = FileParser(self.master.filename)
		self.keylist = self.parser.findKeys()
		
		self.key_search['values'] = self.keylist
		self.key_extract['values'] = self.keylist
		
		self.key_search.current(0)
		self.key_extract.current(0)
		
		file = os.path.basename(self.master.filename)
		self.name.config(text = "Current File: " + file)
		


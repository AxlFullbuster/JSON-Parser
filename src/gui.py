import os
import tkinter as tk
from parser import FileParser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class ParserGUI:
	
	# Initialize the class by creating a window with various widgets.
	def __init__(self, master):
		self.master = master
		master.title("JSON Parser")
		
		# Create a Frame for the window that holds all the other widgets used below
		mainframe = ttk.Frame(master, padding="5 5 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		
		# Creates an empty list that will eventually hold all the keys found in the JSON File.
		# Then create a Button that will load a JSON file to parse.
		self.keylist = list()
		file_button = ttk.Button(mainframe, text = "Load New File", command = self.new_file)
		file_button.grid(column = 3, row = 3, sticky = (E))
		
		# A Label widget that will display the name of the file currently being parsed
		self.name = ttk.Label(mainframe)
		self.name.grid(column = 5, row = 3)
		self.name.config(text = "No File has Been Loaded")
		
		
		# A Label and Combobox widget that displays the key the user would like to search for
		ttk.Label(mainframe, text= "Key to search:  ").grid(column = 0 , row = 0, sticky=(N,W))
		keysearch = StringVar()
		self.key_search = ttk.Combobox(mainframe, textvariable = keysearch)
		self.key_search['values'] = self.keylist
		self.key_search.grid(column = 1, row = 0)
		
		# A Label and Combobox widget that displays the key the user would like returned to them
		ttk.Label(mainframe, text= "Key to extract:  ").grid(column = 0, row = 1, sticky=(N,W))
		keyextract = StringVar()
		self.key_extract = ttk.Combobox(mainframe, textvariable = keyextract)
		self.key_extract['values'] = self.keylist
		self.key_extract.grid(column = 1, row = 1)
		
		# An optional Label and Entry widget that allows the user to input a string that matches with the key they are searching with.
		user_input = ttk.Label(mainframe, text="Content to look for: ")
		user_input.grid(column = 0, row = 2)
		self.user_string = StringVar()
		string_input = ttk.Entry(mainframe, textvariable = self.user_string)
		string_input.grid(column = 1, row = 2)
		
		# A Button that will start the parsing process 
		search_button = ttk.Button(mainframe, text = "Search", command = self.find)
		search_button.grid(column = 0, row = 3, sticky = (W))
		
		# A Text widget that will display the parsed information 
		self.results = tk.Text(master, height = 10, width = 200)
		self.results.grid(column = 0, row = 4, sticky=(N,S,E,W))
		
		# A Scrollbar widget created to easily move across the text box
		yscroll = ttk.Scrollbar(master, command = self.results.yview)
		yscroll.grid(column = 1, row = 4, sticky=(N,S,E,W))
		self.results['yscrollcommand'] = yscroll.set
		
	# Calls the 'parse' method in FileParser and gives it the search, extract, and uinput parameters
	def find(self):
		search = self.key_search.get()
		extract = self.key_extract.get()
		uinput = self.user_string.get()
		
		self.content = self.parser.parse(search, extract, uinput)
		
		self.results.delete(1.0, tk.END)		# Clears the current text box 
		
		
		# If there was no content found in the file return a specified message
		# Otherwise return the matching data
		if not self.content:
			self.results.insert(tk.END, "No Matchng Results Found.")
		else:
			for x in self.content:
				self.results.insert(tk.END, x + '\n')
			
	
	# Has the user select a file to parse, and sends the name of the file to FileParser
	# Also resets the Comboboxes to the first key found in the JSON File
	# We also set the name label initialized above to the file name found here
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
		


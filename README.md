# Author ID
Name: Thierno Diallo  
Email: Tdial3280@gmail.com  
Date: July 2020

# Project Description
This is a JSON File parser that I initially started working on during my junior year in college. I decided to go back to
it now and add some new features to it. This is a very simple program that uses the Tkinter library in Python to
create a User Interface.

# Features
The Program functions by getting the keys found in a particular JSON file and having the user select what key they would
like to search with, a key that they want information extracted from, and entering in a string of the content they would like
to find.

Consider the following JSON file:
````
{
		"Name": "Debian",
		"Version": "9",
		"Install": "apt",
		"Owner": "SPI",
		"Kernel": "4.9"
	},
````

In this particular example the keys would be filtered into the following list:
````
[Name, Version, Install, Owner, Kernel]
````

Say if the user wanted to search with the key "Name" and wanted to extract information from the key "Install". If they enter
the string "Debian" the program would return "apt" in a text box.

Entering a string is optional in the program so if nothing is entered the first ten elements found in the file will be
displayed in the text box.

# Requirements/Compiling
In order to run the program you will need Python3 and the Tkinter Library installed on your machine.
To Compile the code just enter the following in the root of the repository.

````
python3 src
````

By this point a window will appear and you can tinker around with it. To load a file press the "Load File Button"
found in the window. It will take you to the 'json' folder found in the repository and you can select a json file.
One sample file is provided to get a feel for how the program works. Feel free to use other json files to get the
most out of it. Please note that this program works best with json files that match the format found in the sample
file.

Note that this project was created and tested on a Linux machine so YMMV on other operating systems.

# References
[TkDocs](https://tkdocs.com/index.html) Walks you through installing tiknter and working with the basic widgets. It
was very helpful as I had no experience making a user interface in python prior to this project.

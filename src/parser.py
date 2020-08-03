import json
import difflib

class FileParser:
    
    # Initializes the class with the name of the file selected by the user
    # We specify the file as a JSON File and load it's information into a variable called 'obj'
    def __init__(self, file):
        jsonfile = file
        type(jsonfile)
        
        with open (jsonfile) as myfile:
            data = myfile.read()
            
        self.obj = json.loads(data)
        
        
    # Returns a list of keys found in the JSON File
    def findKeys(self):
        keylist = list()
        
        # Get the keys in the file and put them in a list
        for x in self.obj:
            for i in x.keys():
                keylist.append(i)
                
            break
        
        
        return keylist
    
    # Parses the information in the JSON File and returns a list of contents
    # @param search: the key that we are searching with
    # @param extract: the key that we will extract information from
    # @param uinput: a string that was entered by the user(can be empty)
    def parse(self, search, extract, uinput):
        contents = list()
        
        # If the user had entered a string, create a list that holds information that matches the particular search key and string 
        # Else find the first 10 objects in the file and return those instead
        if uinput:
            matches = difflib.get_close_matches(uinput, [x[search] for x in self.obj]) 
            contents = [x[extract] for x in self.obj if x[search] in matches]
        else:
            for x in self.obj:
                contents.append(x[extract])
                
                if len(contents) >= 10:
                    break
            
        return contents
        
    
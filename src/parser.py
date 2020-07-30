import json
import difflib

class FileParser:
    def __init__(self, file):
        jsonfile = file
        type(jsonfile)
        
        with open (jsonfile) as myfile:
            data = myfile.read()
            
        self.obj = json.loads(data)
        
    def findKeys(self):
        keylist = list()
        
        # get the keys in the file and put them in a list
        for x in self.obj:
            for i in x.keys():
                keylist.append(i)
                
            break
        
        
        return keylist
    
    
    def parse(self, search, extract, uinput):
        matches = difflib.get_close_matches(uinput, [x[search] for x in self.obj])
        contents = list()
        
        if uinput:
            contents = [x[extract] for x in self.obj if x[search] in matches]
        else:
            for x in self.obj:
                contents.append(x[extract])
            
        return contents
        
    
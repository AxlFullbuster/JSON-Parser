import json


def findKeys(file):
    # ask for json file
    jsonfile = file
    type(jsonfile)
    
    
    # open and read json file
    with open (jsonfile) as myfile:
        data = myfile.read()
    
    obj = json.loads(data)
    
    keylist = list()
    
    # get the keys in the file and put them in a list
    for x in obj:
        for i in x.keys():
            keylist.append(i)
            
        break
    
    parse_file = file
    
    return keylist


def parse(file, search, extract, uinput):
    # ask for json file
    jsonfile = file 
    type(jsonfile)
    
    
    # open and read json file
    with open (jsonfile) as myfile:
        data = myfile.read()
    
    obj = json.loads(data)

    contents = list()
    
    if uinput:
        contents = [x[extract] for x in obj if x[search] == uinput]
    else:
        for x in obj:
            contents.append(x[extract])
        
    return contents
    
    
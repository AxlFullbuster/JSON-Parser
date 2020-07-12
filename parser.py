import json

# ask for json file
jsonfile = input("Choose a json file: ")
type(jsonfile)



# open and read json file
with open (jsonfile) as myfile:
    data = myfile.read()

obj = json.loads(data)

# get the keys in the file and put them in a list
for x in obj:
    list = x.keys()
    break

print(list)
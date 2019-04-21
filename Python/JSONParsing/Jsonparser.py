import json

#ask for json file
jsonfile = raw_input("Choose a json file: ")
type(jsonfile)

#name of item your looking for
name = input("Type in the name: ")
type(name)

#open and read json file
with open (jsonfile) as myfile:
    data = myfile.read()

obj = json.loads(data)

#prints out matching parts of json using list comprehension
print([x['Version'] for x in obj if x['Name'] == name])

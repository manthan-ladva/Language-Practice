import json
from pprint import pprint

with open("company1.json","r") as file:
    d = json.loads(str(file.read())) #--------json.loads is used in json for loading file

pprint(d)

import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate (w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff = 0.5))>0:
        yn = input("Did you mean %s? Press Y if Yes nad N if No \n" % get_close_matches(w, data.keys(), cutoff=0.5)[0])
        yn = yn.upper()
        if yn  == "Y":
            return data[get_close_matches(w, data.keys(), cutoff=0.5)[0]]
        elif yn == "N":
            return "Try Again!"
        else:
            return "Didn't understand your input"
    else:
        return "Wrong Input"

x = input("Enter the word: ")
x = x.lower()
b = translate(x)
if type(b) == list:
    for f in b:
        print(f)
else:
    print(b)

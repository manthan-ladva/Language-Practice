#--------------------Importing Libraries
import json
import difflib
from difflib import get_close_matches

#--------------------Opening Json File
data = json.load(open("data.json"))

l = 0
no = input("How many douts?\n")
while l < int(no):           #--------------------Loop which will last long according to input
#--------------------Function for dictionary
    def translate (word):
        if word in data:
            return data[word]
        elif word.title() in data:              #--------------------Title Word
            return data[word.title()]
        elif word.upper() in data:              #--------------------Upper Case Word
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys()))>0:      #Code for wrong input
            yn = input("Did you mean %s ?\nIf Yes press Y if No press N\n"
                 % get_close_matches(word, data.keys())[0])
            yn = yn.upper()
            if yn == "Y":
                return data[get_close_matches(word, data.keys())[0]]
            elif yn == "N":
                return "No such words"
            else:
                return "Wrong choice"
        else:
            return "Please check It Again"

    #--------------------Inputing Word
    x = input("Enter word: ")
    x = x.lower()
    output = translate(x)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    l+=1

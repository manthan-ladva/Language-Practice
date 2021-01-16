import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))

l=0
no = input("How many douts?\n")
while l < int(no):
    def translate(word):
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys()))>0:
            yn = input("Did You mean %s. Press Y if Yes or N for No\n" % get_close_matches(word, data.keys())[0])
            yn = yn.upper()
            if yn == 'Y':
                return data[get_close_matches(word, data.keys())[0]]
            elif yn == 'N':
                return "Try Again"
            else:
                return "Wrong Input"
        else:
            return "Wrong input, Check Twice!"

    enter = input("Enter the word: ")
    enter = enter.lower()
    output = translate(enter)
    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)
    l+=1

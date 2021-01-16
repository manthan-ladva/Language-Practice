import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate (word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if Yes and N for No\n" % get_close_matches(word, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "No other words please check it"
        else:
            return "I can't understang your input"
    else:
        return "Please Double check it"


x= input("Enter word: ")
x= x.lower()
y = translate(x)
if type(y) == list:
    for item in y:
        print(item)
else:
    print(y)

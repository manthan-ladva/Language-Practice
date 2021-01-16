import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")
text = r.text
a = text.count("a")
print(a)

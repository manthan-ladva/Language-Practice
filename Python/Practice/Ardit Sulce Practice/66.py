d = dict(weather = "clima", earth = "terra", rain = "chuva")

def etp(word):
    if word in d:
        print(d[word])
    else:
        print("Wrong Input")

x = input("Enter the word:- ")
etp(x)

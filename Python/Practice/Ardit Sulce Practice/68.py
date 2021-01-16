d = dict(weather = "clima", earth = "terra", rain = "chuva")

def etp(word):
    try:
        print(d[word])
    except:
        print("Wrong Input")

x = input("Enter the word:- ").lower()
etp(x)

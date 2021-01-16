#------------Agrs & Kwargs
def new_string(*args):
    return sum(args) * 10

print(new_string(2,4,6))

def kw(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit is {}" .format(kwargs["fruit"]))
    else:
        print("Sorry")
kw(fruit= "Mango", name = "Manthan")


def square(*args):
    #a = list(args)
    for i in args:
        b = i**2
        print(b)
square(4,10,9,2)

import datetime as dt

age = int(input("Your age:- "))
year = int(dt.datetime.now().year)
year = year - age
print("You were born in %s "%year)

#------------------------------------------------------Another Method
from datetime import datetime as dt
age = int(input("Your age:- "))
year = int(dt.now().strftime("%Y"))
year = year - age
print("You were born in %s "%year)

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy():
    def __init__(self):
        self.items = []
        self.zero = 0

    def addItem(self,object):
        self.object = object

        if self.object == 'tophat':
            self.zero = self.zero + 2
        elif self.object == 'bowtie':
            self.zero = self.zero + 4
        elif self.object == 'monocle':
            self.zero = self.zero+ 5
        else:
            self.zero = self.zero + 0
        self.items.append(self.zero)

    def getClassiness(self):
        if len(self.items) == 0:
            return "0"
        else:
            return self.items[-1]

me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
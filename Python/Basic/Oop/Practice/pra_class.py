
# coding: utf-8

# In[16]:


class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        d = ( ((self.coor2[0] - self.coor1[0]) ** 2) + ((self.coor2[1] - self.coor1[1]) ** 2 ) ) ** (1/2)
        return d
    
    def slope(self):
        s = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return s

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

li.distance()

li.slope()


# In[29]:


class Cylinder:
    pie = 3.14
    def __init__(self, height, radius):
        self.height = height
        self.radius  = radius
    
    def volume(self):
        v = self.pie * self.radius * self.radius * self.height
        return v
    
    def sa(self):
        s = (2 * self.pie * self.radius) * (self.radius + self.height)
        return s

c = Cylinder(2, 3)

c.volume()

c.sa()


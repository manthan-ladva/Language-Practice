
# coding: utf-8

# #-----------Lecture 1-----------
# 
# class Dog():
#     def __init__(self, breed, name, sports):
#         self.bru = breed
#         self.name = name
#         self.spo = sports
# 
# my_set  = Dog(breed = "Pup",name = "Tommy", sports = False)
# 
# my_set.bru
# 
# my_set.spo
# 
# my_set.name

# In[15]:


#-----------Lecture 2-----------

class Circle():
    pie = 3.14
    def __init__(self, radius):
        self.radius = radius
        circum = self.pie * self.radius * 2
        print(circum)
    def area(self):
        a = self.pie * self.radius * self.radius
        print(a)

my_circle = Circle(10)
my_circle.area()


# In[ ]:


#-----------Lecture 3-----------


from math import pi
def vol(h, r=10):
    lvol = ((4*pi*(r**3))/3) - (pi*(h**2)*(3*r-h)/3)
    print(lvol)
vol(float(2))

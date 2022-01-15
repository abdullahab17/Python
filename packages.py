import math


r = 0.4 #value of radius

#c = 2pir
c = 2*math.pi*r
print(c)

#a = pir^2
a = math.pi*r**2
print(a)

print("Circumference: ",c)
print("Area: ",a)
#---------------------------------------------------------------
from math import radians
r = 192500
phi = radians(12)
dist = r *phi
print(dist)
#print(math.radians(12))

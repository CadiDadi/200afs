# The math.py file should ask a user the radius of the circle
# In the math.py file, write a code that calculate area of the circle.

# Method 1

from math import pi
r = float(input ("What is the radius of the circle you wish to create: "))
print ("The area of your circle with a radius of " + str(r) + " is: " + str(pi * r**2))

# Method 2

# PI = 3.14
# radius = float(input("What is the radius of a circle?: "))
# area = PI * radius * radius
# print(" Area Of a Circle = %.2f" %area)
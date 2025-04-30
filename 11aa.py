# Write a python program to find the area of a triangle whose sides are given. 
import math
print("Enter the sides of Triangle") 
x=int(input("x = "))
y=int(input("y = "))
z=int(input("z = "))
s=(x+y+z)/2.0
print("the s of a Triangle is ", s )
a=s*(s-x)*(s-y)*(s-z)
area=math.sqrt(a)

print("the Area of a Triangle is ", area )

# pyhon float valuue control
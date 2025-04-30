# Write a python program to find the roots of a quadratic equation.
import math
print("Finding Roots in Quadratic Equation")
print(" ax^2 + b^x + c")
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))

D=(b*b)-4*a*c

if(D>0):
    sqrt_d=math.sqrt(D)   

    r1=(-b+sqrt_d)/(2*a) 
    r2=(-b-sqrt_d)/(2*a )
    print("Hence the Root of Equation is r1 ",r1 ,"and r2 ",r2)
else:
    print("The Equation Roots are  imaginary Roots")
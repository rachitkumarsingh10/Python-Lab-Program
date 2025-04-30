#  Write a python program to find the largest of two numbers.

try:
    print("Enter two Numbers")
    a=int(input("a ="))
    b=int(input("b ="))
    if a>b:
        print(a,">",b)
    else:
        print(b,">",a)
except:
    print("Invalid Input")
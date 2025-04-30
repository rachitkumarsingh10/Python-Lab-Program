#  Write a python program to find the largest of three numbers.  
print("Enter Three Numbers")
a=int(input("a ="))
b=int(input("b ="))
c=int(input("c ="))

if a>b:
    if a>c:
           print(" A is Largest Number")
elif b>a:
    if b>c:
           print(" B is Largest Number")
elif c>b:
    if c>a:
           print(" C is Largest Number")

# Using Function
# print("Enter Three Numbers")
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))

# largest = max(x, y, z)
# print("The largest number is:", largest)

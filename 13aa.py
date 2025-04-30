#  Write a python program to swap two numbers  without using third variable. 
print("Enter two Value")
a=int(input("a = "))
b=int(input("b = "))
print("\nValues in a is ",a)
print("Values in b is ",b)
print("\nAfter Swap Without Using Third Variable")
b=a+b
a=b-a
b=b-a
print("\nValues in a is ",a)
print("Values in b is ",b)
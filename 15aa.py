#  Write a python program to check whether the given number is even or odd. 
x=int(input("Enter a Number "))
if x%2==0:
    print("Number is Even =",x)
elif x%2==1:
      print("Number is Odd =",x)
else:
    print("Invalid Input")

# Uses try-except to catch invalid inputs (e.g., non-integer inputs like letters or symbols).

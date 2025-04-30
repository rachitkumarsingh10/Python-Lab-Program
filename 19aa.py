#  A company decides to give bonus to all its employees on Diwali. A 5% bonus on 
# salary is given to the male worker and 10% bonus on salary to the female workers.  
# WAP to enter the salary of the employee and gender of the employee. If the salary of the 
# employee is less than Rs. 10,000 then the employee gets an extra 2% bonus on salary. 
# Calculate the bonus that has to be given to the employee and display the salary that the 
# employee will get.


print("Company Diwali Bonous")
sal=float(input("Enter Your Salary = "))
print("Enter Your Gender")
gen=input("Male or Female = ")

if sal<10000:
     if gen=="Male":
          new_sal=sal+(sal*0.05)+(sal*0.02)
     elif gen=="Female":
         new_sal=sal+(sal*0.1)+(sal*0.02)
     else:
        print("Invalid Input")
else:
     if gen=="Male":
          new_sal=sal+(sal*0.05)
     else:
         new_sal=sal+(sal*0.1)

print("The Salary of Employee Including Bonus is ",new_sal,"which has increased by his original salary(",sal,")")

# WAP in python to enter the marks of a student in 4 subjects. Then calculate the total 
# and aggregate and also display the grade obtained by the student. If the student scores an 
# aggregate >= 75%, then the grade is distinction.  
# If aggregate is 60>= and <75, then grade = 1st division  
# If aggregate is 50>= and <60, then grade = 2nd division  
# If aggregate is 40>= and <50, then grade = 3rd division else grade is fail.  


# Program to calculate total, aggregate and grade of a student

print("Enter marks for 4 subjects:")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))

total = sub1 + sub2 + sub3 + sub4
aggregate = (total / 400) * 100  # Assuming each subject is out of 100 marks

print("\nTotal Marks =", total)
print("Aggregate Percentage =", aggregate, "%")

# Determine grade
if aggregate >= 75:
    grade = "Distinction"
elif aggregate >= 60:
    grade = "First Division"
elif aggregate >= 50:
    grade = "Second Division"
elif aggregate >= 40:
    grade = "Third Division"
else:
    grade = "Fail"

print("Grade Obtained:", grade)

"""
Day -2 : Input/Output , print formatting, Comments ,conditional
         statements (if,elif,else), nested id ,ternary operators
"""

# Input

# name = input('Enter your name: ') # Always returns string
# age = int(input('Enter your age: ')) # convert to integer
# price = float(input('Enter your price: ')) # convert to float

# Output

print("Hello World")
print("my name is", "Vinod") # comma added space automatically
print("My name is\nVinod")   # \n = new line
print("My name is\tVinod")   # \t = tab space
print("Hello", end=" ")      # end="" stops the default newline
print("World")               # prints on same line → Hello World
print("Hello Vinod","How are you", sep="," ) # sep = "," : separate strings with comma


##############  string formatting #############

name = "Vinod"
age = 22
company = "Soft Tech"

# f- strings
print(f"my name is {name},age is {age} and I'm working at {company} company.")

# f-string Formatting Tricks

pi = 3.14159265
salary = 1500000
score = 87.5

# Decimal Places
print(f"{pi:.2f}") # print the pi value upto 2 decimal place - 3.14
print(f"{pi:.4f}") # print the pi value upto 4 decimal place - 3.1416

# Zero Padding
print(f"ID : {7:04d}") # ID : 0007
print(f"Id : {6:03d}") # ID : 006

# Percentage

print(f"score : {score/100:.1%}") # score : 87.5% after decimal rounded upto 1 digit
print(f"score : {score/100:.2%}") # score : 87.50% after decimal rounded upto 2 digits

# separators

print(f"salary : ${salary:,}") # salary : $1,500,000
print(f"salary : {salary:,} dollars") # salary : 1,500,000 dollars


##### Comments #####

name = 'sanju' # assigned a value to `name` variable (This is inline comment)

"""
This is a multiline-comment (technically a string)
It is used describe the a function, file and a block of code
comments are ignored by python at the time of execution
"""

######## Conditional Statements ########

# syntax
"""
if statement is a decision-making control structure used 
to execute a block of code based on whether a condition evaluates to True or False.

# Basic structure
if condition:
    # runs if condition is True
elif another_condition:
    # runs if above is False, this is True
else:
    # runs if ALL above are False
 """

# Example 1: if-elif-else
age = 20
has_id = "Yes"
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")

# Example 2 : Nested if
" if statement inside another if statement "

if age >= 18:
    if has_id == "Yes":
        print("Access Granted !!")
    else:
        print("Please bring the Valid Id")
else:
    print("You must be 18+ years to vote")


# Ternary Operator (one-line if-else)
# Syntax: value_if_true  if  condition  else  value_if_false

status = "Major" if age >= 18 else "Minor"
print(status)

Marks = 54
Grade = "Pass" if Marks >= 35 else "Fail"
print(Grade)

# Checking membership (in is membership operator)
color = "red"
if color in ["red", "green", "blue"]:
    print("Primary color")

# check if something is empty

name = input("Enter your name: ")
if not name:
    print("name cannot be empty")
else:
    print(name)
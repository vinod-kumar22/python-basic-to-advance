# declaring the variables
name = 'vinod'
age = 25
company = "Soft Tech"
designation = "Technology Analyst"
salary = 50000
is_permanent_employee = True
lpa = 8.5


# Data types
print(type(name))   # string
print(type(age))    # integer
print(type(lpa))    #  float
print(type(is_permanent_employee)) # boolean

# type conversion
lpa = int(lpa)
print(type(lpa)) # integer

salary = float(salary)
print(type(salary))

age = str(age)
print(type(age))

name = int(name)
print(type(name)) # incase try to convert the string into integer it will give a ValueError

company = int(company)
print(type(company)) # incase try to convert the string into integer it will give a ValueError


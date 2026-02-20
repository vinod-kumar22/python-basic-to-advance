"""
Day 1 - Python Fundamentals
Topics Covered:
- Variables
- Data Types
- Type Conversion
- Operators (Arithmetic, Assignment, Comparison, Logical)
"""

# ----------------------------
# Variables
# ----------------------------

name = "vinod"
age = 25
company = "Soft Tech"
designation = "Technology Analyst"
salary = 50000
is_permanent_employee = True
lpa = 8.5


# ----------------------------
# Data Types
# ----------------------------

print(type(name))                     # str
print(type(age))                      # int
print(type(lpa))                      # float
print(type(is_permanent_employee))    # bool


# ----------------------------
# Type Conversion
# ----------------------------

lpa = int(lpa)
print(type(lpa))                      # int

salary = float(salary)
print(type(salary))                   # float

age = str(age)
print(type(age))                      # str

# Converting non-numeric string to int will raise ValueError
# Example:
# name = int(name)


# ----------------------------
# Arithmetic Operators
# ----------------------------

a = 10
b = 20

print(a + b)     # Addition
print(a - b)     # Subtraction
print(a * b)     # Multiplication
print(a / b)     # Division
print(a % b)     # Modulus
print(a // b)    # Floor Division


# ----------------------------
# Assignment Operators
# ----------------------------

c, d = 10, 20

c += d
print(c)

c -= d
print(c)

c *= d
print(c)

c /= d
print(c)

c %= d
print(c)

c **= d
print(c)

c //= d
print(c)


# ----------------------------
# Comparison Operators
# ----------------------------

e, f = 10, 40

print(e == f)
print(e != f)
print(e > f)
print(e < f)
print(e >= f)
print(e <= f)


# ----------------------------
# Logical Operators
# ----------------------------

print(e == f and e != f)
print(e == f or e != f)
print(not (e == f))

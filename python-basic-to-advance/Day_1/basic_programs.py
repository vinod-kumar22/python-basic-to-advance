"""
Day 1 - Basic Practice Programs
"""
import math
# Calculator
a = 20
b = 30

addition = a + b
subtraction = b - a
multiplication = a * b
division = a / b
print(f'addition : {addition}, subtraction : {subtraction}, multiplication : {multiplication}, division: {division}')

# Temperature converter
celsius = 49.5

fahrenheit = (celsius * 9 / 5) + 32
print(f'temperature in celsius : {celsius}, temperature in fahrenheit : {fahrenheit}')

# Area of circle
radius = 5
area_of_circle = math.pi * radius ** 2
print(f'area of circle : {area_of_circle}')

# Area of rectangle

length = 20
width = 6

area_of_rectangle = length * width
print(f'area of rectangle : {area_of_rectangle}')

# Simple interest

principal = 800000
time = 5
rate = 16

simple_interest = (principal * rate * time) / 100
print(f'simple interest : {simple_interest}')

# Swap two numbers
i = 10
j = 20

print(f'before swapping : {i} and {j}')
i,j = j,i
print(f'after swapping : {i} and {j}')

# Even or Odd checker
num = 40
if num % 2 == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')

# Largest between 2 numbers

x = 30
y = 10

if x > y:
    print(f'{x} is larger number than {y}')
else:
    print(f'{y} is larger number than {x}')


# Square and Cube

number = 10
square = number ** 2
cube = number ** 3

print(f'square of {number} is {square} and cube of {number} is {cube}')


# BMI Calculator

weight = 72
height = 1.6

body_mass_index = weight / (height* height)

print(f'body mass index is {body_mass_index}')
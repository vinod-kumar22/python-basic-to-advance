#### Program 1 — Multiplication Table ####
"""
Take a number as input.
Print its multiplication table from 1 to 10 in format `5 x 1 = 5`.
"""
number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a positive number.")
else:
    print(f"\nMultiplication Table of {number}")
    print("-" * 25)

    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")


#### Program 2 — Sum of N Numbers ####
"""
Take N as input. Calculate sum of all numbers from 1 to N without using any formula.
Use a loop. (Example: N=5 → 1+2+3+4+5 = 15)
"""

N = int(input("Enter N: "))
total_sum = 0
if N < 0:
    print("Please enter a positive integer")
else:
    for i in range(1, N+1):
        total_sum += i

    print(f"The sum of all numbers from 1 to {N} is {total_sum}")


#### Program 3 — Countdown Timer ####
"""
Take a number as input. Count down to 0 and print "Blast Off! 🚀" at the end.
"""
number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a positive number")
else:
    for i in range(number, -1,-1):
        print(f"Count Down : {i}")

    print("Blast Off!")


#### Program 4 — Even and Odd Separator ####
"""
Take start and end as input. Print all even numbers on one line and all odd numbers on another line within that range.
"""

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

if start > end:
    print("Start should be less than or equal to end")

else:
    even_numbers = ""
    odd_numbers = ""
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_numbers += str(i) + " "
        else:
            odd_numbers += str(i) + " "

    print("Even numbers:", even_numbers )
    print("Odd numbers:", odd_numbers)


#### Program 5 — Digit Sum ####
"""
Take a number as input. Add all individual digits using a loop.
(Example: 1234 → 1+2+3+4 = 10). No `sum()` allowed.
"""

number = int(input("Enter a number: "))
if number < 0:
    print("Please enter a positive number")
else:
    sum_of_digits = 0
    while number > 0:
        rem = number % 10
        sum_of_digits += rem
        number //= 10

    print(sum_of_digits)


#### Program 6 — Factorial Calculator ####
"""
Take a number N as input. Calculate N! using a loop. (Example: 5! = 5×4×3×2×1 = 120). Handle 0! = 1.
"""
N = int(input("Enter a number: "))

if N < 0:
    print("Please enter a positive number")
else:
    factorial = 1
    for i in range(1, N+1):
        factorial *= i

    print(f"The factorial of {N} is {factorial}")


### Pattern Programs (7–12) ###
#### Program 7 — Right Triangle ####
"""
Take rows as input. Print:
```
*
* *
* * *
* * * *
* * * * *
```
"""

rows = int(input("Enter number of rows: "))

if rows < 0:
    print("rows cannot be negative")
else:

    for i in range(1,rows+1):
        for j in range(i):
            print(f"*", end=" ")
        print()


#### Program 8 — Inverted Triangle ####
"""
Take rows as input. Print:
```
* * * * *
* * * *
* * *
* *
*
```
"""

rows = int(input("Enter number of rows: "))

if rows < 0:
    print("rows cannot be negative")
else:

    for i in range(rows,0,-1):
        for j in range(i):
            print(f"*", end=" ")
        print()


#### Program 9 — Number Triangle ####
"""
Take rows as input. Print:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
"""
rows = int(input("Enter number of rows: "))

if rows < 0:
    print("rows cannot be negative")
else:

    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(f"{j}", end=" ")
        print()


#### Program 10 — Square Patter ####
"""
Take size as input. Print a hollow square border of stars. (Example size=5):
```
* * * * *
*       *
*       *
*       *
* * * * *
```
"""
rows = int(input("Enter number of rows: "))

if rows < 0:
    print("rows cannot be negative")
else:
    for i in range(rows):
        for j in range(rows):
            if i == 0 or i == rows-1 or j == 0 or j == rows-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


#### Program 11 — Pyramid Pattern ####
"""
Take rows as input. Print a centered pyramid:
```
    *
   * *
  * * *
 * * * *
* * * * *
```
"""
rows = int(input("Enter the number of rows: "))
if rows <= 0:
    print("rows cannot be negative")
else:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)


#### Program 12 — Number Square ####
"""
Take size N as input. Print multiplication grid:
```
1  2  3  4
2  4  6  8
3  6  9  12
4  8  12 16
```
"""

N = int(input("Enter the number of rows: "))
if N <= 0:
    print("N must be greater than 0")
else:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(f"{i * j:4}", end = "")
        print()


#### Program 13 — Guess the Number Game ####
"""
Generate a random number between 1 and 100. Keep asking the user to guess.
Tell them "Too High" or "Too Low" after each guess. Print how many attempts it took when they get it right.
"""

import random
random_number = (random.randint(1, 100))
count = 0

while True:
    user_choice = int(input("Enter a number between 1 and 100: "))
    count += 1

    if user_choice > random_number:
        print("Too High")
    elif user_choice < random_number:
        print("Too Low")
    else:
        print("Correct !!")
        break
print(f"It took {count} attempts to guess the number")


#### ATM with 3 Attempts ####
"""
Use your Day 2 ATM program but now give the user only 3 PIN attempts using a loop. Block the card after 3 wrong tries.
"""

balance = 45000
pin = 3447
max_attempts = 3
for attempt in range(1,max_attempts+1):
    enter_pin = int(input("Enter PIN: "))
    if pin == enter_pin:
        print("You entered the correct PIN")
        amount = int(input("Enter withdrawal amount: "))
        if amount <=0:
            print("Invalid Amount, Please check and try again")
        elif amount > balance :
            print(f'Insufficient balance. Available balance is {balance} , try again.')
        elif amount % 100 != 0:
            print("Amount must be a multiple of 100 , try again")
        else:
            balance = balance - amount
            print(f"Withdrawal amount is {amount}, remaining balance is {balance}")
            print("Thank you! visit again.")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Incorrect PIN, you have {remaining} attempt(s) remaining.")
        else:
            print(f"Card Blocked ! please try again after 24 hours.")



#### Program 15 — Prime Number Checker ####
"""
Take a number as input. Check if it is prime using a loop. (A prime number is divisible only by 1 and itself.)
"""

number = int(input("Enter a number: "))

import math

if number < 2 :
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for n in range(2, int(math.sqrt(number)) + 1):
    # for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


#### Program 16 — Fibonacci Series ####
"""
Take N as input. Print the first N numbers of the Fibonacci series. (0, 1, 1, 2, 3, 5, 8, 13...)
"""
N = int(input("Enter how many terms: "))
a = 0
b = 1
series = []
while a < N:
    series.append(a)
    a, b = b, a+b

print(f"Fibonacci series for first {N} terms: {', '.join(map(str, series))}")


#### Program 17 — Number Reverse ####
"""
Take a number as input. Reverse it using a loop and without converting to string. (Example: 1234 → 4321)
"""

number = int(input("Enter a number: "))
original = number
reverse = 0
while number > 0:
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number //= 10

print(f"Original number : {original}")
print(f'Reversed number : {reverse}')


#### Program 18 — Prime Numbers in a Range ####
"""
Take start and end as input. Print all prime numbers in that range. Count how many primes were found.
"""
start = int(input('Enter start number: '))
end = int(input('Enter end number: '))
count = 0
primes = []

for num in range(start, end+1):
    if num < 2 :
        continue
    is_prime = True
    for i in range (2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        count += 1

print(f"\nPrime numbers between {start} and {end}:")
print(*primes, sep=", ")
print(f"Total primes found: {count}")

#### Program 19 — Pattern Menu ####
"""
Show a menu with 4 pattern choices. User picks one, program prints that pattern.
Use a while loop to keep showing the menu until the user chooses to exit.
"""

while True:
    print("\n===== Pattern Menu =====")
    print("1. Right Triangle")
    print("2. Inverted Triangle")
    print("3. Pyramid")
    print("4. Diamond")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))
    rows = 0

    if choice == 5:
        print("Goodbye!")
        break

    if choice in [1, 2, 3, 4]:
        rows = int(input("Enter number of rows: "))

    if choice == 1:
        print("\n--- Right Triangle ---")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        print("\n--- Inverted Triangle ---")
        for i in range(rows, 0, -1):
            print("*" * i)

    elif choice == 3:
        print("\n--- Pyramid ---")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

    elif choice == 4:
        print("\n--- Diamond ---")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))
        for i in range(rows - 1, 0, -1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

    else:
        print("Invalid choice. Please select 1-5.")


#### Program 20 — Mini Calculator with History ####
"""
Build a calculator that keeps running in a loop. After each calculation, ask if they want to continue.
Keep track of all calculations done in the session and print a history when they exit.
"""

history = []

print("===== Calculator =====")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = num1 / num2
        else:
            print("Invalid operator! Please use +, -, *, /")
            continue

        calculation = f"{num1} {operator} {num2} = {result}"
        history.append(calculation)
        print(f"Result: {calculation}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    again = input("\nDo you want to continue? (yes/no): ").lower()
    if again != "yes":
        break

print("\n===== Calculation History =====")
if history:
    for i, record in enumerate(history, 1):
        print(f"{i}. {record}")
    print(f"\nTotal calculations done: {len(history)}")
else:
    print("No calculations were done.")

print("Thank you for using the calculator. Goodbye!")

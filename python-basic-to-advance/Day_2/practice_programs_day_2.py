
import random

########## Program 1 — Grade Calculator #############
"""
Take marks as input (0–100). Print the grade (A+, A, B, C, D, F) based on standard grading.
Also handle invalid marks like -5 or 150.
"""
marks = int(input("Enter your marks: "))

if marks > 100 or marks < 0 :
    print("Your marks should be between 0 and 100")
elif marks >= 90 :
    print("Grade : A+")
elif marks >= 80 :
    print("Grade : A")
elif marks >= 70 :
    print("Grade : B")
elif marks >= 60 :
    print("Grade : C")
elif marks >= 35 :
    print("Grade : D")
else:
    print("Grade : F")


#### Program 2 — Even or Odd + Sign ####
"""
Take a number as input. Print whether it is Even/Odd AND whether it is Positive/Negative/Zero. Print both results.
"""
number = int(input("Enter a number: "))

if number > 0:
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
else:
    print(f'{number} is equal zero')


if number % 2 == 0:
    print(f"{number} is a even number")
else:
    print(f"{number} is a odd number")


#### Program 3 — Largest of 3 Numbers ####
"""
Take 3 numbers as input. Find and print the largest without using max(). Then verify your answer using max().
"""

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
num_3 = int(input("Enter another number: "))

if num_1 >= num_2 and num_1 >= num_3:
    largest_num = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    largest_num = num_2
else:
    largest_num = num_3
print(f'{largest_num} is the greatest number among {num_1}, {num_2} and {num_3}')

largest_builtin = max(num_1, num_2, num_3) # using in-built max() function
print(f'verified using in-built max function', largest_builtin)

#### Program 4 — Voting Eligibility ####
"""
Take age as input. If 18 or above print eligible, else print how many years are left until eligibility.
"""

age = int(input("Please enter your age: "))

if age < 0 or age > 120:
    print("Invalid age !")
elif age >= 18:
    print("You are eligible to vote")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more year(s) to be eligible to vote")

#### Program 5 — Leap Year Checker ####
"""
Take a year as input. Check if it's a leap year or not.
Remember the 3 rules — divisible by 4, exception for 100, exception to exception for 400.
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")

#### Program 6 — Login Validation ####
"""
Set a hardcoded username and password. 
Take input from user. Print a specific message for: correct login, wrong password only, wrong username only, both wrong.
"""

correct_username = "Anandkumar"
correct_password = "Vinu@041722"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password :
    print("Login Successful")
elif username != correct_username and password != correct_password :
    print("Login Unsuccessful, wrong username and password !! Try Again")
elif username != correct_username :
    print("Login Unsuccessful, incorrect username !! Try Again")
else:
    print("Login Unsuccessful, incorrect password!! Try Again")

#### Program 7 — Triangle Type ####

"""
Take 3 sides as input. First check if it forms a valid triangle.
If valid, classify as Equilateral, Isosceles, or Scalene.
"""

side_1 = int(input("Enter a side 1: "))
side_2 = int(input("Enter a side 2: "))
side_3 = int(input("Enter a side 3: "))

if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
    print("Sides must be positive numbers")

elif side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2:
    print(f"{side_1},{side_2},{side_3} form a triangle")
    if side_1 == side_2 == side_3:
        print(f"It is an equilateral triangle")
    elif side_1 != side_2 and side_2 != side_3 and side_3 != side_1:
        print(f"It is a Scalene triangle")
    else:
        print(f"It is an Isosceles triangle")
else:
    print(f"{side_1},{side_2},{side_3} cannot form a triangle")


#### Program 8 — ATM Machine ####
"""
Set a balance and PIN. Ask user to enter PIN. If correct, ask withdrawal amount.
Handle: wrong PIN, insufficient balance, invalid amount (negative or zero), and amount not in multiples of 100.
"""

balance = 45000
pin = 3447

enter_pin = int(input("Enter PIN: "))

if pin == enter_pin:
    print("You entered the correct PIN")
    amount = int(input("Enter withdrawal amount: "))
    if amount <=0:
        print("Invalid Amount, Please check and try again")
    elif amount > balance :
        print(f'Insufficient balance. Available balance is {balance}.')
    elif amount % 100 != 0:
        print("Amount must be a multiple of 100")
    else:
        balance = balance - amount
        print(f"Withdrawal amount is {amount}, remaining balance is {balance}")
        print("Thank you! visit again.")
else:
    print("Incorrect PIN, Please try again")


#### Program 9 — Electricity Bill ####
"""
Take units consumed as input. Calculate bill using slabs
 — first 100 units at ₹1.5, next 200 units at ₹3, next 200 at ₹5, above 500 at ₹7.
Add 10% tax and print the final bill.
"""
electricity_consumed = int(input("Enter electricity consumed in units: "))

if electricity_consumed < 0:
    print("Units cannot be negative")
else:
    electricity_bill = 0
    if electricity_consumed <= 100:
        electricity_bill = electricity_consumed * 1.5
    elif electricity_consumed <= 300:
        electricity_bill = (100 * 1.5) + ((electricity_consumed - 100) * 3)
    elif electricity_consumed <= 500:
        electricity_bill = (100 * 1.5) + (200 * 3) + ((electricity_consumed - 300) * 5)
    else:
        electricity_bill =  (100 * 1.5) + (200 * 3) + (200 * 5) + ((electricity_consumed - 500) * 7)

    tax = electricity_bill * 0.10
    final_bill = electricity_bill + tax

    print(f"Electricity bill before tax: {electricity_bill:.2f}")
    print(f"Tax (10%): {tax:.2f}")
    print(f"Total electricity bill is {final_bill:.2f}.")

#### Program 10 — Discount Calculator ####
"""
Take purchase amount and membership status (yes/no) as input.
Apply 5% discount above ₹1000, 10% above ₹2000, 20% above ₹5000.
Members get an extra 5% on top. Print original, discount, and final amount.
"""

purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount < 0:
    print("Purchase amount cannot be negative.")
else:
    membership_status = input("Enter membership status: ").lower()
    discount = 0
    if purchase_amount > 5000:
        discount = purchase_amount * 0.20
    elif purchase_amount > 2000:
        discount = purchase_amount * 0.10
    elif purchase_amount > 1000:
        discount = purchase_amount * 0.05
    else:
        discount = 0

    amount_after_discount = purchase_amount - discount

    if membership_status in ["yes","y"]:
        extra_discount = amount_after_discount * 0.05
        amount_after_discount = amount_after_discount - extra_discount
    else:
        extra_discount = 0


    print(f"Original purchase amount : {purchase_amount:.2f}")
    print(f"Base discount : {discount:.2f}")
    print(f"Membership Discount: ₹{extra_discount:.2f}")
    print(f"Final Payable Amount: ₹{amount_after_discount:.2f}")

#### Program 11 — Season Finder ####
"""
Take a month number (1–12) as input.
Print the season — Winter, Spring, Summer, or Autumn. Handle invalid month numbers.
"""

month = int(input("Enter a month number (1-12): "))
if not 1 <= month <= 12:
    print("Invalid month number")
elif month in [12,1,2]:
    print("Winter")
elif month in [3,4,5]:
    print("Spring")
elif month in [6,7,8]:
    print("Summer")
else:
    print("Autumn")

#### Program 12 — Number Classifier ####
"""
Take any number as input.
Classify it as: Positive/Negative/Zero, Even/Odd (only if it's a whole number), and Single/Double/Triple digit.
"""

number = int(input("Enter a number: "))

if number > 0:
    print(f'{number} is a positive number')
elif number < 0:
    print(f'{number} is a negative number')
else:
    print(f'{number} is equal to zero')

if number % 2 == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')
abs_number = abs(number)
digit = len(str(abs_number))

if digit == 1:
    print(f'{number} is a single digit')
elif digit == 2:
    print(f'{number} is a double digit')
elif digit == 3:
    print(f'{number} is a triple digit')
else:
    print(f"{number} has more than three digits")


#### Program 13 — Insurance Premium Calculator ####

"""
Take age, smoker status (yes/no), and BMI as input.
Start with a base premium of ₹5000. Add charges based on age group, smoking habit, and BMI range.
Print annual and monthly premium.
"""
base_premium = 5000

age = int(input("Enter your age: "))
smoking_habit = input("Do you smoke? (yes/no): ").lower().strip()
bmi = float(input("Enter your BMI: "))

premium = base_premium

# Age adjustment
if age < 18:
    print("Insurance not available below 18 years")
else:
    if 18 <= age <= 30:
        premium += premium * 0.05
    elif 31 <= age <= 45:
        premium += premium * 0.10
    elif 46 <= age <= 60:
        premium += premium * 0.20
    elif age > 60:
        premium += premium * 0.30

    # BMI adjustment
    if bmi < 18.5:
        premium += premium * 0.05
    elif 25 <= bmi <= 29.9:
        premium += premium * 0.10
    elif bmi >= 30:
        premium += premium * 0.20
    # Normal BMI (18.5–24.9) → no extra charge

    # Smoking adjustment
    if smoking_habit in ["yes", "y"]:
        premium += premium * 0.25

    annual_premium = premium
    monthly_premium = annual_premium / 12

    print(f"Annual Premium: ₹{annual_premium:.2f}")
    print(f"Monthly Premium: ₹{monthly_premium:.2f}")

#### Program 14 — Rock Paper Scissors ####

player_choice = input("choose one : rock, paper, scissors : ").lower()
computer_choice = ["rock", "paper", "scissors"]
rand = random.choice(computer_choice).lower()
print(f"computer choice is {rand}")

if player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice")
elif player_choice == rand:
    print("It's a draw")
elif player_choice == "rock" and rand == "scissors":
    print("User wins")
elif player_choice == "scissors" and rand == "paper":
    print("User wins")
elif player_choice == "paper" and rand == "rock":
    print("User wins")
else:
    print("Computer wins")


#### Program 15 — Mini Shopping Cart ####
"""
Take 3 item prices as input. Calculate total.
Apply rules: if total > ₹500 apply 10% discount, if customer pays cash apply extra 2% discount (ask payment method). 
Print itemized bill with final total.
"""
book   = float(input("Enter price of item 1: ₹"))
pen    = float(input("Enter price of item 2: ₹"))
charts = float(input("Enter price of item 3: ₹"))

total = book + pen + charts
print(f" Total before discount: {total:.2f}")

if total > 500:
    discount = total * 0.1
else:
    discount = 0

amount_after_discount = total - discount

payment_method = input("Enter Payment Method (Cash/Online) : ").lower().strip()

if payment_method == "cash":
    cash_discount = amount_after_discount * 0.02
else:
    cash_discount = 0

final_bill = amount_after_discount - cash_discount

print("\n----- Itemized Bill -----")
print(f"Book: ₹{book:.2f}")
print(f"Pen: ₹{pen:.2f}")
print(f"Charts: ₹{charts:.2f}")
print(f"Discount (10%): ₹{discount:.2f}")
print(f"Cash Discount (2%): ₹{cash_discount:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")


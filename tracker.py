# Project: Expense Tracker - Installment 3
# Author: Kian Calvin Candol
# Description: Tracks two expenses, calculates subtotal, average, tax, grand total, and budget status.

print("""========================================
            EXPENSE TRACKER
       Know where your money goes.
========================================

MAIN MENU
  [1] Add an expense         (coming soon)
  [2] View all expenses      (coming soon)
  [3] Show total spent       (coming soon)
  [4] Exit                   (coming soon)
""")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("\n----------------------------------------")
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("""
----------------------------------------
Made by: Kian Calvin Candol  |  Installment 3
========================================
""")
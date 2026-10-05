# Project: Expense Tracker - Installment 2
# Author: Kian Calvin Candol
# Description: Displays the landing page and main menu for an expense tracker.

print("""========================================
            EXPENSE TRACKER
        Know where your money goes.
========================================

Welcome! This is your personal expense tracker.

MAIN MENU
  [1] Add an expense            (coming soon)
  [2] View all expenses         (coming soon)
  [3] Show total spent          (coming soon)
  [4] Exit                      (coming soon)
""")

name = input("What's your name? ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input(f"Enter the amount for {item1}: "))

item2 = input("Second expense? ")
amount2 = float(input(f"Enter the amount for {item2}: "))

total = amount1 + amount2
average = total / 2

print("\n------------------------------------------")
print("                 SUMMARY                  ")
print("------------------------------------------")
print(f"{item1:<25} ${amount1:>10.2f}")
print(f"{item2:<25} ${amount2:>10.2f}")
print(f"{'Total Spent:':<25} ${total:>10.2f}")
print(f"{'Average:':<25} ${average:>10.2f}")
print("""
----------------------------------------
Made by: Kian Calvin Candol  |  Installment 2
========================================
""")
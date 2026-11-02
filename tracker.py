# Project: Expense Tracker - Installment 4
# Author: Kian Calvin Candol
# Description: Tracks two expenses, calculates subtotal, average, tax, 
#              grand total, and provides conditional feedback and budget verdicts.

print("""========================================
EXPENSE TRACKER
Know where your money goes.
========================================
MAIN MENU
 [1] Add an expense (coming soon)
 [2] View all expenses (coming soon)
 [3] Show total spent (coming soon)
 [4] Exit (coming soon)
""")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

# --- First Expense ---
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# --- Second Expense ---
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

average = subtotal / 2
tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
budget = float(input("Your budget? "))

over_budget = total > budget 

print("\n----------------------------------------")
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")


if over_budget:
   
    print(f"Over budget by ${total - budget}!")
elif total > 0.9 * budget:
    print(f"Careful: only ${budget - total} left.")
else:
    print(f"Within budget. ${budget - total} left.")

print("""----------------------------------------
Made by: Kian Calvin Candol | Installment 4
========================================
""")

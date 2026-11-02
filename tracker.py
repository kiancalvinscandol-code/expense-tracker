# Project: Expense Tracker - Installment 5
# Author: Kian Calvin Candol
# Description: Tracks expenses continuously via an interactive menu interface
#              with dynamic budget limits, tax calculations, and status alerts.

print("""========================================
EXPENSE TRACKER
Know where your money goes.
========================================
Installment 5
""")

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

while True:

    print("""
MAIN MENU
 [1] Add an expense
 [2] View all expenses (coming soon)
 [3] Show total spent
 [4] Exit""")
    
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("Huge expense - are you sure?")
        elif amount > 100:
            print("Big expense.")
        elif amount > 50:
            print("Moderate expense.")
        else:
            print("Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax
        
        print("\n----------------------------------------")
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal:.2f}")
        print(f"Tax ({tax_percent}%):\t${tax:.2f}")
        print(f"Grand total:\t${grand_total:.2f}")
        
        # Verdict calculations matching exact messages
        if grand_total > budget:
            print(f"Over budget by ${grand_total - budget:.2f}!")
        elif grand_total > 0.9 * budget:
            print(f"Careful: only ${budget - grand_total:.2f} left.")
        else:
            print(f"Within budget. ${budget - grand_total:.2f} left.")
        print("----------------------------------------")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("""----------------------------------------
Made by: Kian Calvin Candol | Installment 5
========================================
""")
        break

    else:
        print("Please choose 1, 2, 3 or 4.")

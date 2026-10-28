# Expense-Tracker Installment 5
# Author: Shan Ezekiel R. Dawal
# A personal expense tracker landing page

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print()

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
running = True

while running:
    print("MAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses\t\t(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit\n")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        amount = float(input("Amount? "))
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
        subtotal += amount
        count += 1
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        average = subtotal / count if count > 0 else 0
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = bool(total > budget)
        
        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")
        
        if over_budget:
            print(f"Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${budget - total} left.")
        else:
            print(f"Within budget. ${budget - total} left.")
        print("-" * 40)
    elif choice == "4":
        print(f"Goodbye, {name}!")
        running = False
    else:
        print("Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Shan Ezekiel R. Dawal  |  Installment 5")
print("=" * 40)
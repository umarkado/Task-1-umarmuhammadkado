# Welcome to Python IDE! If you like it, please leave a review.
# Project 2: Expense Tracker - DecodeLabs

print("=== DecodeLabs Expense Tracker ===")
print("Enter your expenses one by one")
print("Type 'done' when you are finished")
print("----------------------------------")

total = 0
count = 0

while True:
    expense = input("Enter expense amount (or type done): ")

    if expense.lower() == "done":
        break

    # Convert to number and add to total
    expense = float(expense)
    total = total + expense
    count = count + 1

    print(f"Added: {expense} | Current Total: {total}")
    print("----------------------------------")

print("\n=== Final Report ===")
print(f"Total number of expenses: {count}")
print(f"Total Spent: {total}")
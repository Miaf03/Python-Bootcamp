# Tip Calculator:

# - Ask for the total bill
# - Ask what percentage tip the user would like to give: 10, 12 or 15%
# - Ask how many people will split the bill
# - Show how much each person should pay

print("\nWelcome to the Tip Calculator!\n")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

amount_per_person = bill * (tip / 100 + 1) / people
print(f"Each person should pay: ${amount_per_person:.2f}")
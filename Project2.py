# Tip Calculator

print("Welcome to the tip Calculator.")
bill_amt = float(input("What was the bill amount? ₹"))
tip_percent = float(input("What percentage tip would you like to give? "))
total_people = int(input("How many People to split the bill? "))

total_payable_amt = bill_amt + ((tip_percent/100)*bill_amt)

bill_split = round(total_payable_amt / total_people, 2)

print(f"Each Person should pay: ₹{bill_split}")
print("Welcome to tip calculator")
total_bill = float(input("Enter total bill: "))
tip = int(input("How much tip would you like to give? 10, 12,or 15 - please do not add any % sign "))
people_split = int(input("How many people to split the bill? "))


bill_with_tip = tip/100 * total_bill + total_bill
print(f"Bill with tip: {bill_with_tip}")
bill_per_person = round(bill_with_tip/people_split,2)
print(f"Bill per person: {bill_per_person}")
print(f"Each person should pay ${bill_per_person}.")
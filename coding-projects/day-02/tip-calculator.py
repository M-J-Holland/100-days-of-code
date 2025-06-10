print("Welcome to the tip calculator!")

bill = float(input("What was the total for the bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people_to_split = int(input("How many people will be splitting the bill? "))

tip_as_percent = (tip / 100)
bill_with_tip = (tip_as_percent * bill) + bill

print(f"Each person will pay {round(bill_with_tip / people_to_split, 2)}")
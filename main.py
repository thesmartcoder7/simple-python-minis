# Tip Calculator
print("\n-------Welcome to the tip calculator-------\n")
total_bill = float(input("What is the total bill coming to? $"))
percentage_tip = float(input("What percentage tip would you like to give? "))
people_paying = float(input("How many people are splitting the bill? $"))

tip = (percentage_tip/100) * total_bill
bill_w_tip = total_bill + tip
bill_per_person = bill_w_tip/people_paying
bill_per_person = round(bill_per_person, 2)

if people_paying > 1:
    print(f"\nEach person should pay: ${bill_per_person}")
else:   
    print(f"\nYou should pay: ${bill_per_person}")
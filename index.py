
print("Welcome to your tip calculator")
bill = float(input("How much did your meal cost? "))
tip = int(input("How much would you like to tip? 10 20 30: "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_cost = bill * tip_as_percent
total_bill_cost = bill + total_tip_cost
total_per_person = total_bill_cost / people
final_amount = round(total_per_person, 2)
print(f"Your total amount is: {total_bill_cost} Each person should pay {final_amount}")



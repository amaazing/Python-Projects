"""Day 2 tip calulator - Beginner"""
'''
Author - Maaz Ali
Project that takes in inputs of cost, tip percentage, and bill split.
Outputs the amount to pay.
'''

print("Hello and welcome to to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much do you want to tip (no percentage sign)? "))
tip = (tip/100)*total_bill #Conversion and multiplication to find tip.
people = int(input("How many people are splitting the bill? "))
individual_bill = "{:.2f}".format(round((tip + total_bill)/people, 2)) #Formats the bill to 2 decimal places.
print(f"Your bill comes to ${individual_bill}.")

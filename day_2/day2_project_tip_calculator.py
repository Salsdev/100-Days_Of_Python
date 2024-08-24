#!/usr/bin/python3

# Welcome greeting
print("Welcome to the tip calculator")
# Ask for total bill
total_bill = float(input("What is the total bill? $"))
# Ask for how much user would like to tip
user_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# Ask for how many people to split the bill with
split_bill = int(input("How many people to split the bill?"))
# Calculate percentage 
tip_amount = (user_tip / 100) *  total_bill
# Get the total amount
total_amount = total_bill + tip_amount
# Split the bill per person
amount_per_person = round(total_amount / split_bill, 2)
# Print each person's bill
print(f"Each person should pay: ${amount_per_person}")

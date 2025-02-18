#!/usr/bin/python3

# Display a welcome message to the user
print("Welcome to python pizza delivery")

# Ask the user for the size of the pizza and store their input
size = input("What size of pizza do you want? S, M or L: ")

# Ask if the user wants pepperoni on their pizza and store their input
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# Ask if the user wants extra cheese and store their input
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Initialize the bill amount
bill = 0

# Determine the base price based on the pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid input.")  # If the size is invalid, print an error message

# Add the price of pepperoni if the user wants it
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Small pizza with pepperoni costs an extra $2
    else:
        bill += 3  # Medium or Large pizza with pepperoni costs an extra $3

# Add the price for extra cheese if the user wants it
if extra_cheese == "Y":
    bill += 1  # Extra cheese costs an additional $1

# Output the final bill to the user
print(f"Your final bill is ${bill}")


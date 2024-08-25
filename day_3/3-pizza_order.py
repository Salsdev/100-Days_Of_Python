#!/usr/bin/python3

print("Welcom to python Pizza Delivery!")
size = input("What size do you want? S, M or L: ")
#pepperoni = input("DO you want pepperoni on your pizza? Y or N: ")
#extra_cheese = input("Do you want extra cheese? Y or N: ")
peppe_s = 2
peppe_l_m = 3
cheese_bill = 1
bill = 0
if size == "S":
    bill = 15
    print("Your bill is $15")
elif size == "M":
    bill = 20
    print("Your bill is $20")
elif size == "L":
    bill = 25
    print("Your bill is $25")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
total = 0
if pepperoni == "Y":
    if size == "S" and pepperoni == "Y":
        total = bill + peppe_s
        print(f"you bill is {total}")
    elif size == "M" or size == "L" and pepperoni == "Y":
        total = bill + peppe_l_m
        print(f"your bill is {total}")
    else:
        print(f"Your total bill is {bill}")

extra_cheese = input("Do you want extra chees? Y or N: ")
if extra_cheese == "Y":
    total += 1
    print(f"Your final bill is {total}")
elif extra_cheese == "N":
    print(f"your final bill is {total}")
else:
    print("Invalid size")

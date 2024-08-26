#!/usr/bin/python3

print("Welcome to rollacoaster!")
user_height = int(input("What is your height in cm? "))
bill = 3

if user_height > 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket $5")
    elif age == 12 or age == 18:
        bill = 7
        print("Youth ticket $7")
    elif age > 18:
        bill = 12
        print("Adult ticket $12")
    elif 45 <= age <= 55:
        print("Have a free ride")

    wants_photo = input("DO you want to have a photo taken? Type y for yes and n for No. "
                        )
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry you are too short! ")

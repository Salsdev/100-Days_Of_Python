#!/bin/usr/python3

# This line of code will ask for input and print input using variable name
name = input("What is your name? ")
print("Hello " + name)

# This line of code will print the lenght of string
print(len(name))

# This line of code will ask user for their gender and print the lenght of string using a single line
print(len(input("Gender? ")))

# This line of code will ask for input and store it in 'institution'
# print the lenght of string
institution = input("What is the name of your institution? ")
lenght = len(institution)
print(lenght)

# Main Task

glass1 = "Juice"
glass2 = "Milk"

# Write 3 lines of code to switch the contents of the variables using variables.

temp = glass1
glass1 = glass2
glass2 = temp
print(f"{glass1} {glass2}") 


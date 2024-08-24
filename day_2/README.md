# Day 2: Understanding Data Types

### Personal Reflections
Today was an enriching exploration of Python data types, with practical applications that provided both challenge and deep learning opportunities. I tackled problems that not only tested my understanding of syntax but also demanded thoughtful problem-solving.

### Goals for Day 2

- **Python Primitive Data Types**: Deepened my understanding of Python's basic data types.
- **Exercises and Projects**: Applied the day’s lessons in three coding exercises:
  - **Two-Digit Addition**
  - **BMI Calculator**
  - **Tip Calculator**

### Example Code Snippets and Outputs


#### BMI Calculator
**Instructions:** Calculate the Body Mass Index (BMI) from a user's weight and height.
- **Example Input:** `weight = 80`, `height = 1.75`
- **Example Output:** `26`

```python
# BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = int(weight / (height ** 2))
print(f"Your BMI is {bmi}")
```
**Output:**
```
Your BMI is 26
```

#### Tip Calculator
**Instructions:** Calculate how much each person should pay including tip.
- **Example Input:** `What was the total bill? $124.56`
- **Example Output:** `Each person should pay: $19.93`

```python
# Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (total_bill / people) * (1 + tip_percent / 100)
print(f"Each person should pay: ${bill_per_person:.2f}")
```
**Output:**
```
Each person should pay: $19.93
```

### Challenges and Learnings
The initial challenge was understanding and implementing type conversions correctly, especially in the BMI calculator where precision was crucial. Debugging was key in enhancing my problem-solving skills.

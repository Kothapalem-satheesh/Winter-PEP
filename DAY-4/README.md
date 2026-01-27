# The Complete Guide to Conditional Statements and Loops
## From Beginner to Advanced - A Story-Driven Journey

---

## Table of Contents
1. [Introduction](#introduction)
2. [Conditional Statements](#conditional-statements)
3. [Loops](#loops)
4. [Advanced Concepts](#advanced-concepts)
5. [Real-World Applications](#real-world-applications)
6. [Best Practices](#best-practices)

---

## Introduction

### The Story Begins... 🚀

Imagine you're a guardian at the gates of a magical kingdom. Your job is simple: allow people in based on certain rules. If someone is a citizen, let them in. If they're a visitor with a valid passport, let them in. If they're neither, turn them away.

This is exactly what **conditional statements** do in programming! They help your code make decisions.

Now, imagine you need to check every visitor coming to the gate, one by one, for the entire day. You can't possibly check each person individually in your code. You need to **repeat** the checking process over and over. This is where **loops** come in!

These two concepts - **decision making (conditionals)** and **repetition (loops)** - are the superpowers that make programs truly intelligent and efficient.

---

## Conditional Statements

### What is a Conditional Statement?

A conditional statement is a piece of code that performs different actions based on different conditions. Think of it as a fork in the road: depending on the situation, you take a different path.

### Level 1: The Simple If Statement (Beginner)

#### The Story

Imagine you have a breakfast experience. If the temperature outside is cold, you decide to wear a warm jacket.

```python
temperature = 5
if temperature < 10:
    print("It's cold outside! Wear a warm jacket.")
```

**Output:** `It's cold outside! Wear a warm jacket.`

#### How It Works

```
if [condition is True]:
    [do this action]
```

The `if` statement checks your condition. If it's `True`, the code inside executes. If it's `False`, the code is skipped.

#### Real Example

```python
age = 15
if age >= 18:
    print("You can vote in the elections!")
```

**Output:** Nothing happens because `age >= 18` is False.

---

### Level 2: The If-Else Statement (Beginner)

#### The Story

Now, our breakfast decision becomes more complete. If it's cold, wear a jacket. If it's NOT cold, wear light clothes.

```python
temperature = 25
if temperature < 10:
    print("It's cold! Wear a warm jacket.")
else:
    print("It's warm! Wear light clothes.")
```

**Output:** `It's warm! Wear light clothes.`

#### How It Works

```
if [condition is True]:
    [do this action]
else:
    [do this other action if condition is False]
```

The `else` block executes when the `if` condition is `False`.

#### Real Example

```python
score = 45
if score >= 50:
    print("You passed the exam!")
else:
    print("You failed the exam. Try again!")
```

**Output:** `You failed the exam. Try again!`

---

### Level 3: Multiple Conditions with If-Elif-Else (Intermediate)

#### The Story

Let's make breakfast decisions more detailed. If it's very cold, wear a heavy jacket. If it's cold but not too cold, wear a light jacket. If it's warm, wear light clothes.

```python
temperature = 12
if temperature < 0:
    print("Wear a heavy winter coat!")
elif temperature < 15:
    print("Wear a light jacket!")
else:
    print("Wear light clothes!")
```

**Output:** `Wear a light jacket!`

#### How It Works

```
if [condition 1 is True]:
    [do action 1]
elif [condition 2 is True]:
    [do action 2]
elif [condition 3 is True]:
    [do action 3]
else:
    [do default action]
```

Python checks conditions from top to bottom. The moment it finds a `True` condition, it executes that block and skips the rest.

#### Real Example: Grades System

```python
marks = 78
if marks >= 90:
    print("Grade: A (Excellent!)")
elif marks >= 80:
    print("Grade: B (Good!)")
elif marks >= 70:
    print("Grade: C (Average!)")
elif marks >= 60:
    print("Grade: D (Pass!)")
else:
    print("Grade: F (Fail!)")
```

**Output:** `Grade: C (Average!)`

---

### Level 4: Logical Operators (Intermediate)

#### The Story

Imagine your morning decision becomes more complex. You want to go to the park IF it's sunny AND it's not too hot.

```python
is_sunny = True
temperature = 22
if is_sunny and temperature < 28:
    print("Perfect weather to go to the park!")
```

**Output:** `Perfect weather to go to the park!`

#### The Three Logical Operators

**1. AND (`and`)**

Both conditions must be True.

```python
username = "admin"
password = "secure123"
if username == "admin" and password == "secure123":
    print("Login successful!")
else:
    print("Invalid credentials!")
```

**Output:** `Login successful!`

**2. OR (`or`)**

At least one condition must be True.

```python
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend! Time to relax.")
else:
    print("It's a weekday. Time for work.")
```

**Output:** `It's the weekend! Time to relax.`

**3. NOT (`not`)**

Reverses the condition. If True becomes False, and False becomes True.

```python
is_raining = False
if not is_raining:
    print("Let's go outside!")
```

**Output:** `Let's go outside!`

#### Combining Multiple Logical Operators

```python
age = 25
has_license = True
is_sober = True

if (age >= 18) and (has_license) and (is_sober):
    print("You can drive safely!")
else:
    print("You cannot drive.")
```

**Output:** `You can drive safely!`

---

### Level 5: Nested Conditionals (Intermediate to Advanced)

#### The Story

Now let's say: First, check if you want to go out. If yes, then check the weather. If weather is good, check if you have money. Only if all are true, go out.

```python
want_to_go_out = True
weather_good = True
have_money = True

if want_to_go_out:
    print("I want to go out!")
    if weather_good:
        print("Weather is nice!")
        if have_money:
            print("I have money!")
            print("Let's go shopping!")
```

**Output:**
```
I want to go out!
Weather is nice!
I have money!
Let's go shopping!
```

#### Why Use Nested Conditionals?

They help when you have dependent conditions - one condition depends on another being true.

#### Real Example: Bank ATM

```python
has_card = True
pin_correct = True
has_balance = True

if has_card:
    if pin_correct:
        if has_balance:
            print("Transaction successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Incorrect PIN! Card blocked after 3 attempts.")
else:
    print("Please insert your card!")
```

---

### Level 6: Ternary Operator (Advanced)

#### The Story

Sometimes, a simple conditional is overkill. You just want to assign a value based on a condition. The ternary operator is a shortcut.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

**Output:** `Adult`

#### Syntax

```
value_if_true if condition else value_if_false
```

#### More Examples

```python
# Example 1: Determining price discount
purchase_amount = 150
discount = 20 if purchase_amount >= 100 else 0
print(f"Your discount: ${discount}")
```

**Output:** `Your discount: $20`

```python
# Example 2: Simple yes/no based on number
number = 5
result = "Odd" if number % 2 != 0 else "Even"
print(result)
```

**Output:** `Odd`

---

## Loops

### What is a Loop?

A loop is a structure that repeats a block of code multiple times. Instead of writing the same code 100 times, you write it once and tell the computer to repeat it 100 times.

### Level 1: The While Loop (Beginner)

#### The Story

Imagine you're counting down to a rocket launch. You start from 10 and count down to 1, and then say "Blast off!"

```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("Blast off! 🚀")
```

**Output:**
```
10
9
8
7
6
5
4
3
2
1
Blast off! 🚀
```

#### How It Works

```
while [condition is True]:
    [execute this code block]
    [eventually change the condition]
```

The loop keeps running as long as the condition is `True`. The moment it becomes `False`, the loop stops.

#### Real Example: User Input Validation

```python
password = ""
while password != "secret123":
    password = input("Enter the password: ")
    if password != "secret123":
        print("Wrong password! Try again.")
print("Welcome! Access granted.")
```

⚠️ **Important:** Be careful with while loops! If you don't change the condition, you'll create an **infinite loop** that never stops.

```python
# ❌ INFINITE LOOP - DON'T RUN THIS!
while True:
    print("This will run forever!")
```

---

### Level 2: The For Loop (Beginner)

#### The Story

Imagine you have a shopping list and you want to buy each item one by one.

```python
shopping_list = ["apples", "milk", "bread", "eggs"]
for item in shopping_list:
    print(f"I need to buy {item}")
```

**Output:**
```
I need to buy apples
I need to buy milk
I need to buy bread
I need to buy eggs
```

#### How It Works

```
for [variable] in [sequence]:
    [execute this code for each item]
```

The for loop goes through each item in a sequence (like a list) one by one.

#### Using `range()` - The Number Loop

When you want to repeat something a certain number of times:

```python
for i in range(5):
    print(f"This is iteration {i}")
```

**Output:**
```
This is iteration 0
This is iteration 1
This is iteration 2
This is iteration 3
This is iteration 4
```

#### Real Example: Multiplication Table

```python
number = 7
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
```

**Output:**
```
Multiplication table of 7:
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70
```

---

### Level 3: For Loop with Lists and Dictionaries (Intermediate)

#### Looping Through Lists

```python
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}s")
```

**Output:**
```
I like apples
I like bananas
I like oranges
I like grapes
```

#### Getting Index and Value

Sometimes you need to know the position of each item:

```python
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Position {index}: {fruit}")
```

**Output:**
```
Position 0: apple
Position 1: banana
Position 2: orange
```

#### Looping Through Dictionaries

```python
student_ages = {"Alice": 20, "Bob": 21, "Charlie": 19}
for name, age in student_ages.items():
    print(f"{name} is {age} years old")
```

**Output:**
```
Alice is 20 years old
Bob is 21 years old
Charlie is 19 years old
```

---

### Level 4: Break and Continue (Intermediate)

#### The Story

Imagine you're in a store, buying items from a list. If you find that an item is sold out, you skip it (`continue`). If you run out of money, you leave the store (`break`).

#### Break Statement

Stops the loop immediately when a condition is met:

```python
for number in range(1, 11):
    if number == 5:
        print("Found 5! Stopping loop.")
        break
    print(number)
```

**Output:**
```
1
2
3
4
Found 5! Stopping loop.
```

#### Continue Statement

Skips the current iteration and moves to the next:

```python
for number in range(1, 6):
    if number == 3:
        print("Skipping 3...")
        continue
    print(number)
```

**Output:**
```
1
2
Skipping 3...
4
5
```

#### Real Example: Finding a Student

```python
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = "Charlie"

for student in students:
    if student == target:
        print(f"Found {target}!")
        break
    print(f"Checking {student}...")
```

**Output:**
```
Checking Alice...
Checking Bob...
Found Charlie!
```

---

### Level 5: Nested Loops (Intermediate to Advanced)

#### The Story

You have multiple lists and need to compare each item in the first list with each item in the second list.

```python
colors = ["red", "blue"]
sizes = ["small", "large"]

for color in colors:
    for size in sizes:
        print(f"{color} {size} shirt")
```

**Output:**
```
red small shirt
red large shirt
blue small shirt
blue large shirt
```

#### Real Example: Times Table

```python
print("Times Table from 1 to 3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="  ")
    print()  # New line after each row
```

**Output:**
```
Times Table from 1 to 3:
1 × 1 = 1  1 × 2 = 2  1 × 3 = 3
2 × 1 = 2  2 × 2 = 4  2 × 3 = 6
3 × 1 = 3  3 × 2 = 6  3 × 3 = 9
```

#### Real Example: 2D Grid Pattern

```python
rows = 3
cols = 3
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
```

**Output:**
```
* * *
* * *
* * *
```

---

### Level 6: List Comprehension (Advanced)

#### The Story

List comprehension is a Python superpower that lets you create lists in a super concise way using a loop inside a single line.

#### Traditional Way vs List Comprehension

**Traditional:**
```python
numbers = []
for i in range(5):
    numbers.append(i * 2)
print(numbers)
```

**List Comprehension:**
```python
numbers = [i * 2 for i in range(5)]
print(numbers)
```

Both output: `[0, 2, 4, 6, 8]`

#### With Conditions

```python
# Get only even numbers from 1 to 10
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)
```

**Output:** `[2, 4, 6, 8, 10]`

#### Real Examples

```python
# Square each number
squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]

# Convert list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)
# Output: ['APPLE', 'BANANA', 'CHERRY']

# Filter students with high marks
marks = {"Alice": 90, "Bob": 65, "Charlie": 85}
high_scorers = [name for name, mark in marks.items() if mark >= 80]
print(high_scorers)
# Output: ['Alice', 'Charlie']
```

---

### Level 7: Dictionary and Set Comprehension (Advanced)

#### Dictionary Comprehension

Create dictionaries in a concise way:

```python
# Create a dictionary with numbers as keys and their squares as values
squares_dict = {x: x**2 for x in range(1, 5)}
print(squares_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16}
```

#### Set Comprehension

Create sets in a concise way:

```python
# Get unique squares from a list of numbers
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)
# Output: {1, 4, 9, 16}
```

---

## Advanced Concepts

### Combining Conditionals and Loops

This is where the real power comes in! Let's see some advanced patterns.

#### Example 1: Search and Filter

```python
# Find all numbers greater than 5
numbers = [3, 7, 2, 9, 1, 8, 4, 6]
filtered = [num for num in numbers if num > 5]
print(f"Numbers greater than 5: {filtered}")
# Output: Numbers greater than 5: [7, 9, 8, 6]
```

#### Example 2: Data Processing

```python
# Calculate total spending by category
shopping_data = [
    {"item": "apple", "price": 1.50, "category": "fruit"},
    {"item": "carrot", "price": 0.75, "category": "vegetable"},
    {"item": "banana", "price": 0.50, "category": "fruit"},
    {"item": "lettuce", "price": 2.00, "category": "vegetable"}
]

total_fruit = sum(item["price"] for item in shopping_data if item["category"] == "fruit")
print(f"Total spent on fruits: ${total_fruit}")
# Output: Total spent on fruits: $2.0
```

#### Example 3: Number Pattern Recognition

```python
# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find all prime numbers up to 20
primes = [num for num in range(2, 20) if is_prime(num)]
print(f"Primes up to 20: {primes}")
# Output: Primes up to 20: [2, 3, 5, 7, 11, 13, 17, 19]
```

#### Example 4: String Manipulation

```python
# Convert list of words to a sentence with conditionals
words = ["hello", "world", "from", "python"]
sentence = ""
for i, word in enumerate(words):
    if i < len(words) - 1:
        sentence += word + " "
    else:
        sentence += word  # No space at the end

print(sentence)
# Output: hello world from python
```

---

## Real-World Applications

### Application 1: Grade Management System

```python
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Processing student grades
students = {
    "Alice": 92,
    "Bob": 78,
    "Charlie": 88,
    "Diana": 55,
    "Eve": 95
}

print("Student Grade Report:")
for name, marks in students.items():
    grade = calculate_grade(marks)
    status = "Pass" if marks >= 60 else "Fail"
    print(f"{name}: {marks} marks → Grade {grade} ({status})")
```

**Output:**
```
Student Grade Report:
Alice: 92 marks → Grade A (Pass)
Bob: 78 marks → Grade B (Pass)
Charlie: 88 marks → Grade C (Pass)
Diana: 55 marks → Grade F (Fail)
Eve: 95 marks → Grade A (Pass)
```

### Application 2: ATM Withdrawal System

```python
def withdraw_money(balance, amount):
    if amount <= 0:
        return "Amount must be positive!"
    elif amount > balance:
        return "Insufficient balance!"
    elif amount % 100 != 0:
        return "Amount must be in multiples of 100!"
    else:
        return f"Withdrawal successful! Remaining balance: ${balance - amount}"

# Test the system
balance = 5000
withdrawals = [500, 6000, 250, 1000]

for amount in withdrawals:
    result = withdraw_money(balance, amount)
    print(f"Withdrawing ${amount}: {result}")
    if "successful" in result.lower():
        balance -= amount
```

### Application 3: Temperature Monitoring System

```python
temperatures = [28, 35, 40, 32, 38, 45, 29]
alert_threshold = 40

print("Daily Temperature Report:")
for day, temp in enumerate(temperatures, 1):
    if temp >= alert_threshold:
        status = "🔴 ALERT - Very Hot!"
    elif temp >= 35:
        status = "🟡 WARNING - Hot"
    elif temp >= 30:
        status = "🟢 Normal"
    else:
        status = "🟢 Cool"
    
    print(f"Day {day}: {temp}°C - {status}")
```

### Application 4: Inventory Management

```python
inventory = {
    "laptop": 5,
    "mouse": 20,
    "keyboard": 15,
    "monitor": 8
}

def check_stock(item):
    if item in inventory:
        quantity = inventory[item]
        if quantity == 0:
            return f"{item.capitalize()} is OUT OF STOCK!"
        elif quantity <= 5:
            return f"{item.capitalize()} has LOW STOCK ({quantity} left)"
        else:
            return f"{item.capitalize()} has sufficient stock ({quantity} available)"
    else:
        return "Item not found in inventory"

# Check all items
for item in inventory:
    print(check_stock(item))
```

### Application 5: Gaming Score System

```python
# Simple number guessing game
import random

secret_number = random.randint(1, 100)
attempts = 0
guessed = False

while not guessed and attempts < 7:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts!")
        guessed = True
    elif guess < secret_number:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")
    
    remaining = 7 - attempts
    if remaining > 0:
        print(f"Attempts remaining: {remaining}\n")

if not guessed:
    print(f"Game Over! The number was {secret_number}")
```

---

## Best Practices

### 1. Keep Conditionals Simple

❌ **Bad:**
```python
if not (not condition1 and (condition2 or not condition3)):
    pass
```

✅ **Good:**
```python
if condition1 or (not condition2 and condition3):
    pass
```

### 2. Use Meaningful Variable Names

❌ **Bad:**
```python
if x > 18 and y:
    pass
```

✅ **Good:**
```python
if user_age > 18 and has_driver_license:
    pass
```

### 3. Avoid Deep Nesting

❌ **Bad:**
```python
if condition1:
    if condition2:
        if condition3:
            if condition4:
                # This is hard to read!
                pass
```

✅ **Good:**
```python
if not (condition1 and condition2 and condition3 and condition4):
    return

# Continue with code
```

### 4. Use Early Returns

❌ **Bad:**
```python
def check_user(user):
    if user is not None:
        if user.age > 18:
            if user.verified:
                return True
    return False
```

✅ **Good:**
```python
def check_user(user):
    if user is None:
        return False
    if user.age <= 18:
        return False
    if not user.verified:
        return False
    return True
```

### 5. Choose the Right Loop

- Use **`for` loops** when you know how many times to iterate
- Use **`while` loops** when you need to iterate until a condition is met
- Use **list comprehensions** for simple transformations

### 6. Always Have Loop Exit Conditions

❌ **Bad - Infinite Loop:**
```python
while True:
    x = input("Enter something: ")
    # No break condition!
```

✅ **Good:**
```python
while True:
    x = input("Enter something (or 'quit' to exit): ")
    if x.lower() == "quit":
        break
```

### 7. Use Built-in Functions

Instead of loops:

```python
# Instead of:
total = 0
for num in numbers:
    total += num

# Use:
total = sum(numbers)
```

### 8. Document Complex Logic

```python
# Check if user is eligible for senior citizen discount
# Criteria: Age > 60 OR has government ID
is_senior = age > 60 or has_govt_id

if is_senior:
    discount = 0.20  # 20% discount
```

---

## Quick Reference Cheat Sheet

### Conditionals Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| **if** | `if condition:` | Single decision |
| **if-else** | `if condition: else:` | Two-way decision |
| **if-elif-else** | `if c1: elif c2: else:` | Multiple decisions |
| **and** | `condition1 and condition2` | Both must be true |
| **or** | `condition1 or condition2` | At least one true |
| **not** | `not condition` | Reverse the condition |
| **Ternary** | `value_if_true if condition else value_if_false` | Simple assignment |

### Loops Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| **for** | `for item in sequence:` | Iterate through items |
| **while** | `while condition:` | Repeat until condition false |
| **range()** | `range(start, end, step)` | Loop a specific number of times |
| **break** | `break` | Exit loop immediately |
| **continue** | `continue` | Skip to next iteration |
| **List Comp.** | `[expr for item in seq if condition]` | Create list concisely |

---

## Conclusion

Conditional statements and loops are the foundation of programming. They allow your code to:
- **Make decisions** based on different scenarios
- **Repeat actions** efficiently without code duplication
- **Process data** at scale
- **Solve real-world problems** systematically

The journey from understanding basic `if` statements to mastering list comprehensions and nested loops is one of gradual progression. Start simple, practice consistently, and gradually tackle more complex scenarios.

Remember: Every professional programmer started exactly where you are now. The key is practice and understanding the "why" behind each concept, not just memorizing syntax.

**Keep coding, keep learning! 🚀**

---

## Practice Exercises

### Easy
1. Write a program that takes a number and prints whether it's positive, negative, or zero.
2. Create a loop that prints numbers from 1 to 10.
3. Write a program that finds the largest number in a list.

### Medium
4. Create a program that checks if a number is prime.
5. Write a program that reverses a list without using built-in reverse functions.
6. Create a grading system with proper conditionals.

### Hard
7. Write a program that finds all prime numbers up to 100 using loops and conditionals.
8. Create a program that calculates the factorial of a number.
9. Write a program that finds all Fibonacci numbers up to 1000.

---

**Happy Learning! If you have questions, revisit the relevant section and practice with real examples.** 📚

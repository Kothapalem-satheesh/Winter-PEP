# A string is a sequence of characters enclosed in quotes.


# creating the strings
name = "Satheesh"
city = 'Hyderabad'
message = "Hello, World!"


# Triple quotes are mainly used for multi-line strings:
text = """
This is
a multi-line
string
"""

"""
strings are Immutable 
Immutable means → once created, you cannot change it.

❌ Not allowed:
s = "Python"
s[0] = "J"   # ERROR

✅ Correct way:
s = "Python"
s = "J" + s[1:]
print(s)     # Jython


"""

s="kothapalem satheesh"
print("j"+s[1:])
print(len(s))





x = 4
x = "GFG"
x += "Hello"
print(x)


# Concatenation (joining)
first_name = "kothapalem"
last_name = "satheesh"
full_name = first_name + " " + last_name
print(full_name)  # Output: kothapalem satheesh

# Repetition
laugh = "Ha" * 3
print(laugh)  # Output: HaHaHa

# String length
text = "Python"
length = len(text)
print(f"Length: {length}")  # Output: Length: 6 as of now



text = "  Hello Python World  "

# Case conversion
print(text.upper())        # Output: "  HELLO PYTHON WORLD  "
print(text.lower())        # Output: "  hello python world  "
print(text.capitalize())   # Output: "  hello python world  " (only first letter)
print(text.title())        # Output: "  Hello Python World  " (title case)

# Whitespace removal
print(text.strip())        # Output: "Hello Python World" (removes leading/trailing)
print(text.lstrip())       # Output: "Hello Python World  " (removes left side)
print(text.rstrip())       # Output: "  Hello Python World" (removes right side)

# Finding and replacing
greeting = "Hello World"
print(greeting.find("World"))      # Output: 6 (position of "World")
print(greeting.replace("World", "Python"))  # Output: "Hello Python"
print(greeting.count("l"))         # Output: 3 (count of "l")

# Checking content
print(greeting.startswith("Hello"))  # Output: True
print(greeting.endswith("World"))    # Output: True
print(greeting.isalpha())            # Output: False (contains space)


# String Formatting (Important!)
# Method 1: f-strings (modern, recommended)
name = "Alice"
age = 25
print(f"{name} is {age} years old")  # Output: Alice is 25 years old

# Method 2: format() method
print("{} is {} years old".format(name, age))  # Output: Alice is 25 years old

# Method 3: % operator (older style)
print("%s is %d years old" % (name, age))  # Output: Alice is 25 years old

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # Output: Price: $19.99
print(f"Percentage: {0.85*100:.1f}%")  # Output: Percentage: 85.0%
# A dictionary stores data in key-value pairs. Like a real dictionary 
# you look up a word (key) to get its definition (value).

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "gpa": 3.8
}

print(type(student))  # Output: <class 'dict'>




student = {"name": "Alice", "age": 20, "grade": "A"}
# Access by key
print(student["name"])      # Output: "Alice"
print(student["age"])       # Output: 20

# Safe access with get()
print(student.get("name"))  # Output: "Alice"
print(student.get("city"))  # Output: None (key doesn't exist)
print(student.get("city", "Unknown"))  # Output: "Unknown" (default value)





student = {"name": "Alice", "age": 20}
# Adding/updating items
student["grade"] = "A"      # Add new key-value pair
student["age"] = 21         # Update existing value

print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

# Removing items
del student["grade"]        # Delete a key-value pair
student.pop("age")          # Remove and return value
student.clear()             # Remove all items

# Dictionary methods
student = {"name": "Alice", "age": 20, "grade": "A"}

keys = student.keys()           # Get all keys
values = student.values()       # Get all values
items = student.items()         # Get key-value pairs

print(list(keys))    # Output: ['name', 'age', 'grade']
print(list(values))  # Output: ['Alice', 20, 'A']
print(list(items))   # Output: [('name', 'Alice'), ('age', 20), ('grade', 'A')]

# Check existence
print("name" in student)    # Output: True
print("city" in student)    # Output: False



# Dictionary Comprehension
# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With conditions
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}



# Iterating Through Dictionaries
student = {"name": "Alice", "age": 20, "grade": "A"}

# Iterate over keys
for key in student:
    print(key)  # Output: name, age, grade

# Iterate over values
for value in student.values():
    print(value)  # Output: Alice, 20, A

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
    # Output: name: Alice
    #         age: 20
    #         grade: A
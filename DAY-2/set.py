"""Set (set)
What is a Set?
A set is an unordered collection of unique items. No duplicates allowed. Useful for removing duplicates and checking membership.
"""
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4, 5}

print(type(colors))  # Output: <class 'set'>
print(len(colors))   # Output: 3

# Set Operations
# Creating a set
unique_numbers = {1, 2, 2, 3, 3, 3}
print(unique_numbers)  # Output: {1, 2, 3} (duplicates removed!)

# Adding and removing
colors = {"red", "green"}
colors.add("blue")          # Add one item
colors.update(["yellow"])   # Add multiple items
colors.remove("red")        # Remove (error if not found)
colors.discard("red")       # Remove (no error if not found)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2              # {1, 2, 3, 4, 5, 6} (all items)
intersection = set1 & set2       # {3, 4} (common items)
difference = set1 - set2         # {1, 2} (in set1 but not set2)
symmetric_difference = set1 ^ set2  # {1, 2, 5, 6} (in either but not both)

print(union)
print(intersection)
print(difference)
# Set Comprehension
# Create a set of unique squares
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}




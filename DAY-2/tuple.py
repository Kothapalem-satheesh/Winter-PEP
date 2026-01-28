"""A tuple is similar to a list, but immutable - you cannot change, add, 
or remove items after creation. Enclosed in parentheses ()."""

colors = ("red", "green", "blue")
coordinates = (10, 20)
single_item = (42,)  # Note the comma! Without it, it's just the number 42

print(type(colors))  # Output: <class 'tuple'>



# Accessing Tuple Elements
colors = ("red", "green", "blue", "yellow")

# Same indexing as lists
print(colors[0])      # Output: "red"
print(colors[-1])     # Output: "yellow"
print(len(colors))    # Output: 4




# Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 2
print(repeated)  # Output: (1, 2, 3, 1, 2, 3)

# Unpacking
red, green, blue = ("red", "green", "blue")
print(red)    # Output: "red"
print(green)  # Output: "green"

# Methods (limited compared to lists)
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))     # Output: 3 (count of 2s)
print(numbers.index(3))     # Output: 2 (position of first 3)

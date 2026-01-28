fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Lists can contain different types!

print(type(fruits))  # Output: <class 'list'
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# By index (position) - remember, Python starts counting from 0!
print(fruits[0])      # Output: "apple"
print(fruits[1])      # Output: "banana"
print(fruits[-1])     # Output: "elderberry" (last item)
print(fruits[-2])     # Output: "date" (second-to-last)

# Index visualization:
# Index:    0       1        2       3      4
# Value:  apple  banana   cherry  date  elderberry
# Negative: -5    -4       -3     -2    -1





# List Methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Adding elements
numbers.append(5)           # Add to end: [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers.insert(0, 10)       # Insert at position 0: [10, 3, 1, 4, ...]
numbers.extend([7, 8])      # Add multiple items: [..., 6, 5, 7, 8]

# Removing elements
numbers.remove(3)           # Remove first occurrence of 3
numbers.pop()               # Remove and return last item
numbers.pop(0)              # Remove and return item at index 0
numbers.clear()             # Remove all items

# Finding and counting
original = [3, 1, 4, 1, 5, 9, 2, 6]
index = original.index(4)   # Output: 2 (position of 4)
count = original.count(1)   # Output: 2 (how many 1s)

# Sorting and reversing
numbers = [3, 1, 4, 1, 5]
numbers.sort()              # Sort in place: [1, 1, 3, 4, 5]
numbers.reverse()           # Reverse in place: [5, 4, 3, 1, 1]

# Creating new sorted/reversed lists
numbers = [3, 1, 4, 1, 5]
sorted_list = sorted(numbers)      # [1, 1, 3, 4, 5] (new list)
reversed_list = list(reversed(numbers))  # [5, 1, 4, 1, 3] (new list)

# List Comprehension
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# With conditions - only even numbers
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]



# Negative indexing makes it easy to get items without needing to know the exact length of the list.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements starting from index -2
# to end of list
b = a[-2:]
print(b)
# Get elements starting from index 0 
# to index -3 (excluding 3th last index)
c = a[:-3]
print(c)
# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)
# Get every 2nd elements from index -8
text = "Hello World"
#      0123456789(10)
# Indices: H=0, e=1, l=2, l=3, o=4, space=5, W=6, ...

# Get character at position
print(text[0])      # Output: "H"
print(text[6])      # Output: "W"

# Slice from start to position (not including position)
print(text[0:5])    # Output: "Hello"
print(text[6:11])   # Output: "World"

# Slice from position to end
print(text[6:])     # Output: "World"

# Slice from start to position
print(text[:5])     # Output: "Hello"

# Slice entire string
print(text[:])      # Output: "Hello World"





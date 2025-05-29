#############################################
# 🐍 Python Iteration & Indexing Cheatsheet #
#############################################

----------------------
📦 LISTS
----------------------
fruits = ['apple', 'banana', 'cherry']

# Iterate over elements
for fruit in fruits:
    print(fruit)

# Iterate with index
for i in range(len(fruits)):
    print(i, fruits[i])

# Best practice with enumerate
for i, fruit in enumerate(fruits):
    print(i, fruit)


----------------------
🔤 STRINGS
----------------------
word = "hello"

# Iterate characters
for char in word:
    print(char)

# With index
for i, char in enumerate(word):
    print(i, char)


----------------------
📓 DICTIONARIES
----------------------
person = {'name': 'Alice', 'age': 30}

# Keys
for key in person:
    print(key, person[key])

# Keys & values
for key, value in person.items():
    print(key, value)

# Values only
for value in person.values():
    print(value)


----------------------
📊 PANDAS DataFrame
----------------------
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Iterate rows (slow)
for index, row in df.iterrows():
    print(index, row['A'], row['B'])

# Better: column access
for value in df['A']:
    print(value)


----------------------
🧰 USEFUL PATTERNS
----------------------
# enumerate()
for i, item in enumerate(mylist):
    print(i, item)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# list comprehension
squared = [x**2 for x in range(5)]


----------------------
🧮 NESTED LISTS
----------------------
matrix = [[1, 2, 3], [4, 5, 6]]

# Nested loop
for row in matrix:
    for val in row:
        print(val)

# Index access
print(matrix[0][1])  # 2

# With index
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"matrix[{i}][{j}] = {val}")


----------------------
🔢 RANGE PATTERNS
----------------------
# Basic
for i in range(5):
    print(i)

# Custom step
for i in range(1, 10, 2):
    print(i)

# Backwards
for i in range(5, 0, -1):
    print(i)


----------------------
🧾 LIST OF DICTS
----------------------
students = [{'name': 'Alice', 'score': 92}, {'name': 'Bob', 'score': 87}]

for student in students:
    print(student['name'], student['score'])


----------------------
🧮 NUMPY
----------------------
import numpy as np
arr = np.array([[1, 2], [3, 4]])

# Loop
for row in arr:
    for val in row:
        print(val)

# Access
print(arr[0, 1])  # 2


----------------------
⚡ COMPREHENSIONS
----------------------

# List
[x**2 for x in range(5)]

# With filter
[x for x in range(10) if x % 2 == 0]

# If-else
['even' if x % 2 == 0 else 'odd' for x in range(5)]

# Set
{x**2 for x in [1, 2, 2, 3]}  # {1, 4, 9}

# Dict
{char: word.count(char) for char in set("banana")}  # {'b':1, 'a':3, 'n':2}

# With zip()
{k: v for k, v in zip(keys, values)}

# Nested list flatten
[val for row in matrix for val in row]


----------------------
🧪 CHALLENGES TO TRY
----------------------
# Count characters
char_count = {}
for char in sentence:
    if char != ' ':
        char_count[char] = char_count.get(char, 0) + 1

# Dict comprehension to count
{char: sentence.count(char) for char in set(sentence) if char != ' '}

# Get first letter from each word
words = ['cat', 'car', 'dog']
first_letters = {word[0] for word in words}


----------------------
⚠️ GOTCHAS & TIPS
----------------------
- Strings are iterable but not mutable
- Avoid modifying a list while looping over it
- Use vectorized ops with pandas when possible
- df.iterrows() returns Series — slow for big data
- Comprehensions = fast, clean, readable — but don't over-nest!


# 100 Python Data Structure Practice Problems
# Lists, Dictionaries, Tuples, and Nested Structures
# Uncomment each problem to practice, then check your solution

# ====== LISTS - LESSON & EXPLANATION ======
"""
LISTS are ordered, mutable collections that can hold any data type.
They are defined with square brackets: [1, 2, 3]

Key characteristics:
- Ordered: Items have a defined order and maintain that order
- Mutable: You can change, add, or remove items after creation
- Allow duplicates: Same value can appear multiple times
- Indexed: Access items using index numbers (starting from 0)

Common operations:
-list.append(item): Add item to end
-list.insert(index, item): Insert item at specific position
-list.remove(item): Remove first occurrence of item
-list.pop(index): Remove and return item at index (default: last item)
-list.index(item): Find index of first occurrence
-list.count(item): Count occurrences of item
-list.sort(): Sort in place
-list.reverse(): Reverse in place
-list.extend(iterable): Add all items from another iterable

List slicing: list[start:end:step]
- list[2:5] gets items from index 2 to 4
- list[:3] gets first 3 items
- list[-1] gets last item
- list[::-1] reverses the list

List comprehensions: [expression for item in iterable if condition]
- [x*2 for x in range(5)] creates [0, 2, 4, 6, 8]
- [x for x in range(10) if x % 2 == 0] creates [0, 2, 4, 6, 8]
"""

# ====== BASIC LIST OPERATIONS (Problems 1-15) ======

# Problem 1: Create a list of numbers 1-10
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# Problem 2: Add the number 11 to the end of the list
# numbers.append(11)

# Problem 3: Insert the number 0 at the beginning of the list
# numbers.insert(0, 0)

# Problem 4: Remove the number 5 from the list
# numbers.remove(5)

# Problem 5: Get the last element using negative indexing
# last_element = numbers[-1]

# Problem 6: Get elements from index 2 to 7 (slicing)
# slice_result = numbers[2:7]

# Problem 7: Reverse the list
# numbers.reverse()

# Problem 8: Sort a list of names alphabetically
# names = ['Alice', 'Charlie', 'Bob', 'Diana']
# names.sort()   #sorts in place

# sorted_names_list = sorted(names) #create a new list that is sorted without altering original



# Problem 9: Find the index of 'Bob' in the names list
# bob_index = names.index('Bob')

# Problem 10: Count how many times 'a' appears in the string list
# letters = ['a', 'b', 'a', 'c', 'a', 'd']
# count_a = letters.count('a')
# print(count_a)

# Problem 11: Extend a list with another list
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)

# Problem 12: Create a list using list comprehension (squares of 1-5)
# squares = [x**2 for x in range(0,6)]

# Problem 13: Filter even numbers from a list using list comprehension
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [x % 2 == 0 for x in numbers]  #This returns booleans. The %modulo check to start returns True/False
# print(evens)
# evens_as_int = [x for x in numbers if x % 2 == 0]
# print(evens_as_int)

# def iterative_version(numbers):
    # for x in numbers:
        # if x % 2 == 0:
            # print(x)

# print(iterative_version(numbers))
# Problem 14: Pop the last element and store it in a variable
# numbers = [1, 2, 3, 4, 5]
# last = numbers.pop() 

# # Problem 15: Clear all elements from a list
# numbers.clear()

# ====== DICTIONARIES - LESSON & EXPLANATION ======
"""
DICTIONARIES are unordered, mutable collections of key-value pairs.
They are defined with curly braces: {'key': 'value'}

Key characteristics:
- Unordered: Items don't have a defined order (Python 3.7+ maintains insertion order)
- Mutable: You can change, add, or remove items after creation
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any data type and can be duplicated
- Fast lookup: Finding values by key is very efficient

Common operations:
- dict[key] = value: Add or update key-value pair
- dict[key]: Access value by key (raises KeyError if key doesn't exist)
- dict.get(key, default): Access value by key (returns default if key doesn't exist)
- dict.pop(key): Remove and return value for key
- dict.keys(): Get all keys
- dict.values(): Get all values
- dict.items(): Get all key-value pairs as tuples
- dict.update(other_dict): Add/update multiple key-value pairs
- key in dict: Check if key exists
- len(dict): Get number of key-value pairs

Dictionary comprehensions: {key_expr: value_expr for item in iterable if condition}
- {x: x**2 for x in range(5)} creates {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
"""

# ====== BASIC DICTIONARY OPERATIONS (Problems 16-30) ======

# Problem 16: Create a dictionary with person information


# Problem 17: Add a new key-value pair to the dictionary
# person['email'] = 

# Problem 18: Update an existing value in the dictionary
# person['age'] = 

# Problem 19: Get a value using the get() method with default
# phone = person.get('phone', 'Not provided')

# Problem 20: Remove a key-value pair using pop()
# removed = person.pop('email')

# Problem 21: Get all keys from the dictionary
# keys = 

# Problem 22: Get all values from the dictionary
# values = 

# Problem 23: Get all items (key-value pairs) from the dictionary
# items = 

# Problem 24: Check if a key exists in the dictionary
# has_name = 

# Problem 25: Update dictionary with another dictionary
# person.update({'city': 'New York', 'country': 'USA'})

# Problem 26: Create a dictionary using dict comprehension (squares)
# squares_dict = 

# Problem 27: Get the length of a dictionary
# dict_length = 

# Problem 28: Copy a dictionary
# person_copy = 

# Problem 29: Remove all items from dictionary
# person.clear()

# Problem 30: Create dictionary from two lists (zip)
# keys = ['name', 'age', 'city']
# values = ['John', 25, 'Boston']
# combined = 

# ====== TUPLES - LESSON & EXPLANATION ======
"""
TUPLES are ordered, immutable collections that can hold any data type.
They are defined with parentheses: (1, 2, 3) or just commas: 1, 2, 3

Key characteristics:
- Ordered: Items have a defined order and maintain that order
- Immutable: You cannot change items after creation (but can reassign entire tuple)
- Allow duplicates: Same value can appear multiple times
- Indexed: Access items using index numbers (starting from 0)
- Hashable: Can be used as dictionary keys (unlike lists)

Common operations:
- tuple[index]: Access item by index
- tuple.index(item): Find index of first occurrence
- tuple.count(item): Count occurrences of item
- len(tuple): Get number of items
- item in tuple: Check if item exists
- tuple1 + tuple2: Concatenate tuples
- tuple * n: Repeat tuple n times

Tuple unpacking: Assign tuple elements to multiple variables
- x, y, z = (1, 2, 3)  # x=1, y=2, z=3
- a, *rest, last = (1, 2, 3, 4, 5)  # a=1, rest=[2,3,4], last=5

Single-element tuples: Need a trailing comma
- single = (42,)  # Tuple with one element
- not_tuple = (42)  # This is just parentheses around an integer

Use cases:
- Coordinates: (x, y, z)
- RGB colors: (255, 0, 128)
- Database records: (id, name, email)
- Return multiple values from functions
"""

# ====== BASIC TUPLE OPERATIONS (Problems 31-40) ======

# Problem 31: Create a tuple with coordinates
# coordinates = 

# Problem 32: Access the second element of the tuple
# y_coord = 

# Problem 33: Unpack a tuple into variables
# x, y, z = 

# Problem 34: Create a tuple with one element (note the comma!)
# single_tuple = 

# Problem 35: Concatenate two tuples
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# combined = 

# Problem 36: Repeat a tuple
# repeated = (1, 2) * 3

# Problem 37: Find the index of an element in tuple
# numbers = (1, 2, 3, 2, 4)
# index_of_2 = 

# Problem 38: Count occurrences in tuple
# count_of_2 = 

# Problem 39: Convert tuple to list
# tuple_data = (1, 2, 3, 4)
# list_data = 

# Problem 40: Check if element exists in tuple
# exists = 3 in (1, 2, 3, 4)

# ====== NESTED LISTS - LESSON & EXPLANATION ======
"""
NESTED LISTS are lists that contain other lists as elements.
Common example: 2D lists (matrices) like [[1, 2, 3], [4, 5, 6]]

Key concepts:
- 2D lists represent rows and columns (like spreadsheets)
- Access elements with double indexing: matrix[row][column]
- First index selects the row (inner list)
- Second index selects the column (element within that list)

Creating nested lists:
- Manual: [[1, 2], [3, 4], [5, 6]]
- List comprehension: [[i*3 + j for j in range(3)] for i in range(3)]
- Using loops: 
  matrix = []
  for i in range(3):
      row = []
      for j in range(3):
          row.append(i*3 + j)
      matrix.append(row)

Common operations:
- matrix[i]: Get entire row i
- matrix[i][j]: Get element at row i, column j
- [row[j] for row in matrix]: Get entire column j
- matrix.append(new_row): Add new row
- matrix[i].append(item): Add item to row i

Flattening: Convert 2D to 1D
- [item for row in matrix for item in row]

Be careful with references!
- wrong = [[0] * 3] * 3  # Creates 3 references to same list!
- right = [[0] * 3 for _ in range(3)]  # Creates 3 separate lists
"""

# ====== NESTED LISTS (Problems 41-50) ======

# Problem 41: Create a 2D list (matrix)
# matrix = 

# Problem 42: Access element in 2D list (row 1, column 2)
# element = 

# Problem 43: Add a new row to the matrix
# matrix.append([7, 8, 9])

# Problem 44: Modify an element in the matrix
# matrix[0][0] = 

# Problem 45: Get all elements in the first row
# first_row = 

# Problem 46: Get all elements in the first column
# first_column = 

# Problem 47: Flatten a 2D list into 1D
# flattened = 

# Problem 48: Create a list of lists using list comprehension
# nested = 

# Problem 49: Find the sum of all elements in a 2D list
# total = 

# Problem 50: Transpose a matrix (swap rows and columns)
# transposed = 

# ====== LISTS OF DICTIONARIES - LESSON & EXPLANATION ======
"""
LISTS OF DICTIONARIES are very common in real-world programming.
Think of them as tables where each dictionary is a row with named columns.

Example: Student records
students = [
    {'name': 'Alice', 'grade': 95, 'age': 20},
    {'name': 'Bob', 'grade': 87, 'age': 19}
]

Key concepts:
- Each dictionary represents one record/entity
- All dictionaries typically have the same keys (like table columns)
- Access: students[0]['name'] gets first student's name
- Very useful for JSON data, database results, CSV files

Common operations:
- Add record: students.append({'name': 'Charlie', 'grade': 92})
- Find record: next((s for s in students if s['name'] == 'Alice'), None)
- Update record: 
  for student in students:
      if student['name'] == 'Alice':
          student['grade'] = 95
- Filter records: [s for s in students if s['grade'] > 90]
- Sort records: students.sort(key=lambda x: x['grade'], reverse=True)
- Extract column: [s['name'] for s in students]
- Calculate stats: sum(s['grade'] for s in students) / len(students)

Advanced operations:
- Group by field: Group students by grade level
- Aggregate data: Average grades, count by category
- Join data: Combine with other lists based on common fields
"""

# ====== LISTS OF DICTIONARIES (Problems 51-60) ======

# Problem 51: Create a list of student dictionaries
# students = 

# Problem 52: Add a new student to the list
# students.append()

# Problem 53: Find a student by name
# def find_student(name):
#     pass

# Problem 54: Update a student's grade
# # Update Alice's grade to 95

# Problem 55: Remove a student from the list
# # Remove the student named 'Bob'

# Problem 56: Get all student names
# names = 

# Problem 57: Calculate average grade of all students
# avg_grade = 

# Problem 58: Find students with grade above 85
# high_performers = 

# Problem 59: Sort students by grade (highest first)
# students.sort()

# Problem 60: Group students by grade range (A, B, C)
# grade_groups = {'A': [], 'B': [], 'C': []}

# ====== DICTIONARIES WITH LISTS - LESSON & EXPLANATION ======
"""
DICTIONARIES WITH LISTS as values are great for categorizing and grouping data.
Think of them as folders containing multiple items.

Example: Shopping lists by category
shopping = {
    'fruits': ['apple', 'banana', 'orange'],
    'vegetables': ['carrot', 'broccoli'],
    'dairy': ['milk', 'cheese']
}

Key concepts:
- Keys represent categories/groups
- Values are lists of items in each category
- Access: shopping['fruits'] gets the fruits list
- Modify: shopping['fruits'].append('grape') adds to fruits

Common operations:
- Add to category: shopping['fruits'].append('grape')
- Remove from category: shopping['fruits'].remove('apple')
- Add new category: shopping['meat'] = ['chicken', 'beef']
- Get all items: [item for items in shopping.values() for item in items]
- Count items in category: len(shopping['fruits'])
- Count total items: sum(len(items) for items in shopping.values())
- Find category of item: 
  next((cat for cat, items in shopping.items() if 'apple' in items), None)

Use cases:
- Organizing files by type
- Grouping students by class
- Categorizing tasks by priority
- Managing inventory by department
- Social media: users and their posts/followers

Advanced patterns:
- defaultdict(list): Automatically creates empty lists for new keys
- Sorting items within categories
- Merging categories from multiple dictionaries
"""

# ====== DICTIONARIES WITH LISTS (Problems 61-70) ======

# Problem 61: Create a dictionary with list values (shopping lists)
# shopping = {
#     'fruits': ['apple', 'banana'],
#     'vegetables': ['carrot', 'broccoli']
# }

# Problem 62: Add an item to the fruits list
# shopping['fruits'].append()

# Problem 63: Remove an item from vegetables list
# shopping['vegetables'].remove()

# Problem 64: Add a new category with items
# shopping['dairy'] = 

# Problem 65: Get all items from all categories (flatten)
# all_items = 

# Problem 66: Count total items across all categories
# total_items = 

# Problem 67: Find which category contains 'apple'
# category = 

# Problem 68: Remove empty categories
# # Remove any categories that have empty lists

# Problem 69: Sort items within each category
# for category in shopping:
#     shopping[category].sort()

# Problem 70: Create a dictionary of lists using comprehension
# number_lists = 

# ====== NESTED DICTIONARIES - LESSON & EXPLANATION ======
"""
NESTED DICTIONARIES are dictionaries containing other dictionaries.
They represent hierarchical or tree-like data structures.

Example: Company organization
company = {
    'departments': {
        'engineering': {'manager': 'Alice', 'employees': 10},
        'marketing': {'manager': 'Bob', 'employees': 5}
    }
}

Key concepts:
- Multiple levels of nesting: dict['key1']['key2']['key3']
- Each level represents a category or classification
- Access: company['departments']['engineering']['manager']
- Can mix with lists: departments can contain employee lists

Common patterns:
- Configuration files (JSON-like structures)
- API responses with nested data
- Hierarchical data (organizations, file systems)
- Multi-dimensional categorization

Navigation techniques:
- Step by step: dept = company['departments']['engineering']
- Direct access: manager = company['departments']['engineering']['manager']
- Safe access with get(): 
  manager = company.get('departments', {}).get('engineering', {}).get('manager')

Common operations:
- Add nested structure: company['departments']['sales'] = {'manager': 'Charlie'}
- Update nested value: company['departments']['marketing']['employees'] = 7
- Get all keys at level: list(company['departments'].keys())
- Extract values: [dept['manager'] for dept in company['departments'].values()]
- Calculate aggregates: sum(dept['employees'] for dept in company['departments'].values())

Best practices:
- Keep nesting levels reasonable (2-4 levels max)
- Use consistent key names across similar structures
- Consider flattening if structure becomes too complex
- Handle missing keys gracefully with get() or try/except
"""

# ====== NESTED DICTIONARIES (Problems 71-80) ======

# Problem 71: Create a nested dictionary (company structure)
# company = {
#     'departments': {
#         'engineering': {'manager': 'Alice', 'employees': 10},
#         'marketing': {'manager': 'Bob', 'employees': 5}
#     }
# }

# Problem 72: Access nested value (engineering manager)
# eng_manager = 

# Problem 73: Add a new department
# company['departments']['sales'] = 

# Problem 74: Update number of employees in marketing
# company['departments']['marketing']['employees'] = 

# Problem 75: Add employee list to each department
# company['departments']['engineering']['employee_list'] = 

# Problem 76: Get all department names
# dept_names = 

# Problem 77: Get all managers
# managers = 

# Problem 78: Calculate total employees
# total_employees = 

# Problem 79: Find department with most employees
# largest_dept = 

# Problem 80: Remove a department
# removed_dept = company['departments'].pop()

# ====== COMPLEX NESTED STRUCTURES - LESSON & EXPLANATION ======
"""
COMPLEX NESTED STRUCTURES combine multiple data types in sophisticated ways.
Real-world data often requires mixing lists, dictionaries, and tuples.

Example: School management system
school = {
    'name': 'Tech High',
    'grades': {
        9: {
            'classes': ['Math', 'English', 'Science'],  # List in dict
            'students': [                               # List of dicts
                {'name': 'Alice', 'subjects': {'Math': 95, 'English': 87}},  # Nested dict
                {'name': 'Bob', 'subjects': {'Math': 78, 'Science': 92}}
            ]
        }
    }
}

Understanding the structure:
- school: Main dictionary
- school['grades']: Dictionary of grade levels
- school['grades'][9]: Dictionary for 9th grade
- school['grades'][9]['students']: List of student dictionaries
- school['grades'][9]['students'][0]: First student (Alice)
- school['grades'][9]['students'][0]['subjects']: Alice's grades dictionary

Navigation strategies:
1. Step by step:
   grade_9 = school['grades'][9]
   students = grade_9['students']
   alice = students[0]
   alice_math = alice['subjects']['Math']

2. Direct path:
   alice_math = school['grades'][9]['students'][0]['subjects']['Math']

3. With variables:
   grade = 9
   student_index = 0
   subject = 'Math'
   score = school['grades'][grade]['students'][student_index]['subjects'][subject]

Common challenges and solutions:
- KeyError: Use get() with defaults or try/except
- Finding items: Use loops or list comprehensions with conditions
- Modifying nested data: Navigate to the right level, then modify
- Aggregating data: Use nested loops or comprehensions

Performance considerations:
- Deep nesting can slow access
- Consider caching frequently accessed paths
- For complex queries, consider using pandas or databases
- Balance between structure complexity and ease of use

Real-world examples:
- JSON APIs (weather data, social media posts)
- Configuration files
- Database query results
- Game state (players, inventory, stats)
- File system representations
"""

# ====== COMPLEX NESTED STRUCTURES (Problems 81-90) ======

# Problem 81: Create a complex nested structure (school system)
# school = {
#     'name': 'Tech High',
#     'grades': {
#         9: {
#             'classes': ['Math', 'English', 'Science'],
#             'students': [
#                 {'name': 'Alice', 'subjects': {'Math': 95, 'English': 87}},
#                 {'name': 'Bob', 'subjects': {'Math': 78, 'Science': 92}}
#             ]
#         }
#     }
# }

# Problem 82: Add a new student to grade 9
# new_student = 

# Problem 83: Update Alice's English grade
# school['grades'][9]['students'][0]['subjects']['English'] = 

# Problem 84: Add a new subject to the grade 9 classes
# school['grades'][9]['classes'].append()

# Problem 85: Get all student names in grade 9
# grade_9_students = 

# Problem 86: Calculate Alice's average grade
# alice_avg = 

# Problem 87: Find the student with the highest Math grade
# best_math_student = 

# Problem 88: Add a new grade level (10th grade)
# school['grades'][10] = 

# Problem 89: Count total students in the school
# total_students = 

# Problem 90: Create a report of all students and their averages
# student_reports = 

# ====== ADVANCED OPERATIONS - LESSON & EXPLANATION ======
"""
ADVANCED OPERATIONS involve sophisticated manipulation of nested data structures.
These techniques are essential for real-world data processing.

Key concepts covered:

1. MERGING DATA STRUCTURES
   - Combining dictionaries with overlapping keys
   - Merging lists within dictionaries
   - Handling conflicts and duplicates

2. COPYING (Shallow vs Deep)
   - Shallow copy: copy.copy() or dict.copy()
     * Copies the container but not nested objects
     * Changes to nested objects affect both copies
   - Deep copy: copy.deepcopy()
     * Recursively copies all nested objects
     * Completely independent copies

3. DATA TRANSFORMATION
   - Inverting dictionaries (swap keys/values)
   - Flattening nested structures
   - Creating nested structures from flat data
   - Reshaping data for different use cases

4. SEARCHING AND FILTERING
   - Finding paths to specific values
   - Searching across multiple nesting levels
   - Complex filtering with multiple conditions
   - Pattern matching in nested data

5. GROUPING AND AGGREGATION
   - Grouping items by multiple criteria
   - Creating summary statistics
   - Pivoting data structures
   - Creating reports from raw data

6. SORTING COMPLEX DATA
   - Multi-key sorting (primary, secondary sorts)
   - Custom sort functions
   - Sorting nested structures
   - Maintaining relationships during sorts

7. RECURSIVE OPERATIONS
   - Functions that call themselves
   - Processing arbitrarily nested data
   - Tree traversal algorithms
   - Counting, searching, and transforming at any depth

Best practices for advanced operations:
- Always handle edge cases (empty structures, missing keys)
- Use appropriate data structures for your use case
- Consider performance implications of deep nesting
- Write reusable functions for common operations
- Test with various data shapes and sizes
- Document complex data structures clearly

These skills prepare you for working with:
- JSON APIs and web services
- Database query results
- Configuration files
- Data science and analytics
- Complex application state management
"""

# ====== ADVANCED OPERATIONS (Problems 91-100) ======

# Problem 91: Merge two dictionaries with list values
# dict1 = {'a': [1, 2], 'b': [3, 4]}
# dict2 = {'a': [5, 6], 'c': [7, 8]}
# merged = 

# Problem 92: Deep copy vs shallow copy demonstration
# import copy
# original = {'list': [1, 2, 3]}
# shallow = 
# deep = 

# Problem 93: Create a defaultdict-like behavior
# from collections import defaultdict
# dd = defaultdict(list)
# # Add items to keys that don't exist yet

# Problem 94: Invert a dictionary (swap keys and values)
# original = {'a': 1, 'b': 2, 'c': 3}
# inverted = 

# Problem 95: Group items by a criterion
# people = [
#     {'name': 'Alice', 'age': 25, 'city': 'NYC'},
#     {'name': 'Bob', 'age': 30, 'city': 'NYC'},
#     {'name': 'Charlie', 'age': 25, 'city': 'LA'}
# ]
# # Group by age
# by_age = 

# Problem 96: Flatten a deeply nested list
# nested = [1, [2, 3], [4, [5, 6]], 7]
# def flatten(lst):
#     pass

# Problem 97: Create a nested dictionary from a flat dictionary
# flat = {'user.name': 'Alice', 'user.age': 25, 'user.address.city': 'NYC'}
# nested = 

# Problem 98: Find the path to a value in nested dictionary
# data = {'a': {'b': {'c': 'target'}}}
# def find_path(d, target):
#     pass

# Problem 99: Sort a list of dictionaries by multiple keys
# students = [
#     {'name': 'Alice', 'grade': 95, 'age': 20},
#     {'name': 'Bob', 'grade': 95, 'age': 19},
#     {'name': 'Charlie', 'grade': 87, 'age': 21}
# ]
# # Sort by grade (desc), then by age (asc)
# sorted_students = 

# Problem 100: Create a recursive function to count all items in nested structure
# data = {
#     'level1': [1, 2, {'level2': [3, 4, {'level3': [5, 6]}]}]
# }
# def count_all_items(obj):
#     pass

# ====== SOLUTIONS SECTION ======
# Uncomment the solutions below to check your work

"""
SOLUTIONS:

# Problem 1
numbers = list(range(1, 11))

# Problem 2
numbers.append(11)

# Problem 3
numbers.insert(0, 0)

# Problem 4
numbers.remove(5)

# Problem 5
last_element = numbers[-1]

# Problem 6
slice_result = numbers[2:8]

# Problem 7
numbers.reverse()

# Problem 8
names = ['Alice', 'Charlie', 'Bob', 'Diana']
names.sort()

# Problem 9
bob_index = names.index('Bob')

# Problem 10
letters = ['a', 'b', 'a', 'c', 'a', 'd']
count_a = letters.count('a')

# Problem 11
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)

# Problem 12
squares = [x**2 for x in range(1, 6)]

# Problem 13
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]

# Problem 14
numbers = [1, 2, 3, 4, 5]
last = numbers.pop()

# Problem 15
numbers.clear()

# Problem 16
person = {'name': 'John', 'age': 30, 'city': 'Boston'}

# Problem 17
person['email'] = 'john@email.com'

# Problem 18
person['age'] = 31

# Problem 19
phone = person.get('phone', 'Not provided')

# Problem 20
removed = person.pop('email')

# Problem 21
keys = list(person.keys())

# Problem 22
values = list(person.values())

# Problem 23
items = list(person.items())

# Problem 24
has_name = 'name' in person

# Problem 25
person.update({'city': 'New York', 'country': 'USA'})

# Problem 26
squares_dict = {x: x**2 for x in range(1, 6)}

# Problem 27
dict_length = len(person)

# Problem 28
person_copy = person.copy()

# Problem 29
person.clear()

# Problem 30
keys = ['name', 'age', 'city']
values = ['John', 25, 'Boston']
combined = dict(zip(keys, values))

# Problem 31
coordinates = (10, 20, 30)

# Problem 32
y_coord = coordinates[1]

# Problem 33
x, y, z = coordinates

# Problem 34
single_tuple = (42,)

# Problem 35
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2

# Problem 36
repeated = (1, 2) * 3

# Problem 37
numbers = (1, 2, 3, 2, 4)
index_of_2 = numbers.index(2)

# Problem 38
count_of_2 = numbers.count(2)

# Problem 39
tuple_data = (1, 2, 3, 4)
list_data = list(tuple_data)

# Problem 40
exists = 3 in (1, 2, 3, 4)

# Problem 41
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Problem 42
element = matrix[1][2]  # row 1, column 2 (value 6)

# Problem 43
matrix.append([7, 8, 9])

# Problem 44
matrix[0][0] = 99

# Problem 45
first_row = matrix[0]

# Problem 46
first_column = [row[0] for row in matrix]

# Problem 47
flattened = [item for row in matrix for item in row]

# Problem 48
nested = [[i*3 + j for j in range(3)] for i in range(3)]

# Problem 49
total = sum(sum(row) for row in matrix)

# Problem 50
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Problem 51
students = [
    {'name': 'Alice', 'grade': 95, 'age': 20},
    {'name': 'Bob', 'grade': 87, 'age': 19},
    {'name': 'Charlie', 'grade': 92, 'age': 21}
]

# Problem 52
students.append({'name': 'Diana', 'grade': 89, 'age': 20})

# Problem 53
def find_student(name):
    for student in students:
        if student['name'] == name:
            return student
    return None

# Problem 54
for student in students:
    if student['name'] == 'Alice':
        student['grade'] = 95

# Problem 55
students = [s for s in students if s['name'] != 'Bob']

# Problem 56
names = [student['name'] for student in students]

# Problem 57
avg_grade = sum(student['grade'] for student in students) / len(students)

# Problem 58
high_performers = [s for s in students if s['grade'] > 85]

# Problem 59
students.sort(key=lambda x: x['grade'], reverse=True)

# Problem 60
grade_groups = {'A': [], 'B': [], 'C': []}
for student in students:
    if student['grade'] >= 90:
        grade_groups['A'].append(student)
    elif student['grade'] >= 80:
        grade_groups['B'].append(student)
    else:
        grade_groups['C'].append(student)

# Problem 61
shopping = {
    'fruits': ['apple', 'banana'],
    'vegetables': ['carrot', 'broccoli']
}

# Problem 62
shopping['fruits'].append('orange')

# Problem 63
shopping['vegetables'].remove('carrot')

# Problem 64
shopping['dairy'] = ['milk', 'cheese']

# Problem 65
all_items = [item for items in shopping.values() for item in items]

# Problem 66
total_items = sum(len(items) for items in shopping.values())

# Problem 67
category = next((cat for cat, items in shopping.items() if 'apple' in items), None)

# Problem 68
shopping = {k: v for k, v in shopping.items() if v}

# Problem 69
for category in shopping:
    shopping[category].sort()

# Problem 70
number_lists = {f'list_{i}': list(range(i*3, (i+1)*3)) for i in range(3)}

# Problem 71
company = {
    'departments': {
        'engineering': {'manager': 'Alice', 'employees': 10},
        'marketing': {'manager': 'Bob', 'employees': 5}
    }
}

# Problem 72
eng_manager = company['departments']['engineering']['manager']

# Problem 73
company['departments']['sales'] = {'manager': 'Charlie', 'employees': 8}

# Problem 74
company['departments']['marketing']['employees'] = 7

# Problem 75
company['departments']['engineering']['employee_list'] = ['Dave', 'Eve', 'Frank']

# Problem 76
dept_names = list(company['departments'].keys())

# Problem 77
managers = [dept['manager'] for dept in company['departments'].values()]

# Problem 78
total_employees = sum(dept['employees'] for dept in company['departments'].values())

# Problem 79
largest_dept = max(company['departments'].items(), key=lambda x: x[1]['employees'])[0]

# Problem 80
removed_dept = company['departments'].pop('sales')

# Problem 91
dict1 = {'a': [1, 2], 'b': [3, 4]}
dict2 = {'a': [5, 6], 'c': [7, 8]}
merged = {}
for d in [dict1, dict2]:
    for k, v in d.items():
        merged.setdefault(k, []).extend(v)

# Problem 94
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}

# Problem 95
people = [
    {'name': 'Alice', 'age': 25, 'city': 'NYC'},
    {'name': 'Bob', 'age': 30, 'city': 'NYC'},
    {'name': 'Charlie', 'age': 25, 'city': 'LA'}
]
by_age = {}
for person in people:
    age = person['age']
    if age not in by_age:
        by_age[age] = []
    by_age[age].append(person)

# Problem 96
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Problem 99
students = [
    {'name': 'Alice', 'grade': 95, 'age': 20},
    {'name': 'Bob', 'grade': 95, 'age': 19},
    {'name': 'Charlie', 'grade': 87, 'age': 21}
]
sorted_students = sorted(students, key=lambda x: (-x['grade'], x['age']))

# Problem 100
def count_all_items(obj):
    count = 0
    if isinstance(obj, dict):
        count += len(obj)
        for value in obj.values():
            count += count_all_items(value)
    elif isinstance(obj, (list, tuple)):
        count += len(obj)
        for item in obj:
            count += count_all_items(item)
    return count
"""

print("Python Data Structure Practice Problems Loaded!")
print("Uncomment each problem section to practice.")
print("Solutions are provided at the bottom of the file.")
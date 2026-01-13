# ============================================================================
# CODE BLOCK 1: VARIABLES AND DATA TYPES
# ============================================================================

# Integers
age = 25
student_id = 12345
negative_number = -100

# Floats
height = 5.9
weight = 65.5
pi = 3.14159

# Strings
name = "Al Faiz"
course = 'Python Programming'
multiline_text = """This is a
multiline string in Python"""

# Booleans
is_student = True
is_graduated = False

# Lists (Mutable)
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# Tuples (Immutable)
coordinates = (10, 20)
rgb_color = (255, 0, 128)

# Dictionaries
student_info = {"name": "Al Faiz", "age": 25, "course": "Python"}
scores = {"math": 95, "english": 88, "science": 92}

# Using type() to check data types
print("Type of age:", type(age))              # <class 'int'>
print("Type of height:", type(height))        # <class 'float'>
print("Type of name:", type(name))            # <class 'str'>
print("Type of is_student:", type(is_student)) # <class 'bool'>
print("Type of fruits:", type(fruits))        # <class 'list'>
print("Type of coordinates:", type(coordinates)) # <class 'tuple'>
print("Type of student_info:", type(student_info)) # <class 'dict'>


# ============================================================================
# CODE BLOCK 2: TYPE CASTING
# ============================================================================

# String to Integer
string_number = "42"
converted_int = int(string_number)
print(f"String '{string_number}' to int: {converted_int}")  # 42

# String to Float
string_float = "3.14"
converted_float = float(string_float)
print(f"String '{string_float}' to float: {converted_float}")  # 3.14

# Integer to String
integer_value = 100
converted_string = str(integer_value)
print(f"Integer {integer_value} to string: '{converted_string}'")  # '100'

# Integer to Float
int_to_float = float(50)
print(f"Integer 50 to float: {int_to_float}")  # 50.0

# String to Boolean
bool_value = bool("hello")  # Non-empty string is True
print(f"Boolean value of 'hello': {bool_value}")  # True

bool_value2 = bool("")  # Empty string is False
print(f"Boolean value of '': {bool_value2}")  # False

# List to Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List to Tuple: {my_tuple}")  # (1, 2, 3, 4, 5)

# Tuple to List
my_tuple2 = (10, 20, 30)
my_list2 = list(my_tuple2)
print(f"Tuple to List: {my_list2}")  # [10, 20, 30]


# ============================================================================
# CODE BLOCK 3: OPERATORS
# ============================================================================

# ARITHMETIC OPERATORS
print("\n--- ARITHMETIC OPERATORS ---")
a = 20
b = 5

addition = a + b          # 25
subtraction = a - b       # 15
multiplication = a * b    # 100
division = a / b          # 4.0
floor_division = a // b   # 4
modulus = a % b           # 0
exponentiation = a ** b   # 3200000

print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {subtraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {division}")
print(f"{a} // {b} = {floor_division}")
print(f"{a} % {b} = {modulus}")
print(f"{a} ** {b} = {exponentiation}")

# COMPARISON OPERATORS
print("\n--- COMPARISON OPERATORS ---")
x = 10
y = 20

print(f"{x} == {y}: {x == y}")  # False
print(f"{x} != {y}: {x != y}")  # True
print(f"{x} < {y}: {x < y}")   # True
print(f"{x} > {y}: {x > y}")   # False
print(f"{x} <= {y}: {x <= y}") # True
print(f"{x} >= {y}: {x >= y}") # False

# LOGICAL OPERATORS
print("\n--- LOGICAL OPERATORS ---")
condition1 = True
condition2 = False

print(f"{condition1} and {condition2}: {condition1 and condition2}")  # False
print(f"{condition1} or {condition2}: {condition1 or condition2}")   # True
print(f"not {condition1}: {not condition1}")                        # False
print(f"not {condition2}: {not condition2}")                        # True

# ASSIGNMENT OPERATORS
print("\n--- ASSIGNMENT OPERATORS ---")
num = 10
print(f"Initial value: {num}")  # 10

num += 5
print(f"After += 5: {num}")  # 15

num -= 3
print(f"After -= 3: {num}")  # 12

num *= 2
print(f"After *= 2: {num}")  # 24

num /= 4
print(f"After /= 4: {num}")  # 6.0

# MEMBERSHIP OPERATORS
print("\n--- MEMBERSHIP OPERATORS ---")
fruits_list = ["apple", "banana", "orange"]

print("apple" in fruits_list)        # True
print("grape" in fruits_list)        # False
print("apple" not in fruits_list)    # False
print("grape" not in fruits_list)    # True

# IDENTITY OPERATORS
print("\n--- IDENTITY OPERATORS ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")  # False
print(f"list1 is not list2: {list1 is not list2}")  # True
print(f"list1 is list3: {list1 is list3}")  # True
print(f"list1 == list2: {list1 == list2}")  # True

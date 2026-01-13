# Python Syntax & Data Types - Complete Module Overview

## 📚 Module Information

**Course:** Basic Python (ByteXL)  
**Module:** Python Syntax & Data Types  
**Total Duration:** 200 minutes (4 x 50 mins + 1 hr test)  
**Level:** Beginner  
**Topics:** 5 | Labs: 4 | Quizzes: 4 | Tests: 1

---

## 🎯 Module Objective

This comprehensive module introduces students to Python's fundamental syntax, data types, and core concepts. Students will learn how to set up the Python environment, understand variables and data types, perform type conversions, and work with various operators.

---

## 📋 Topics Covered

### 1. **Introduction to Python** (50 mins)
- What is Python?
- Python characteristics (Interpreted, Beginner-Friendly, OOP, Interactive)
- History and features
- Platform support
- Installation and setup (Unix/Linux, Windows, Mac)
- Environment setup and PATH configuration
- Running Python programs

### 2. **Variables and Data Types** (50 mins)
- Variable declaration and naming conventions
- Python's dynamic typing
- Data types: int, float, str, bool, list, dict, tuple
- Type identification with type()
- Mutable vs Immutable types

### 3. **Type Casting** (50 mins)
- Implicit type conversion
- Explicit type conversion
- int(), float(), str(), bool() functions
- Casting between different data types
- Common casting errors and solutions

### 4. **Operators** (50 mins)
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Assignment operators (=, +=, -=, etc.)
- Membership operators (in, not in)
- Identity operators (is, is not)

### 5. **Module Test** (1 hour)
- Comprehensive assessment of all topics
- MCQ format
- Hands-on coding exercises

---

## 🔑 Key Concepts

| Concept | Description | Example |
|---------|-------------|----------|
| **Variables** | Named containers for storing values | `name = "Python"` |
| **Data Types** | Categories of values (int, str, float, bool, etc.) | `x = 42` (int), `y = "hello"` (str) |
| **Type Casting** | Converting one data type to another | `int("10")` converts string to integer |
| **Operators** | Symbols for performing operations | `+`, `-`, `*`, `/`, `==`, `and`, `or` |
| **Dynamic Typing** | Python determines type at runtime | No need to declare variable types |

---

## 💻 Complete Code Examples

```python
# ============================================================================
# PYTHON SYNTAX & DATA TYPES - COMPLETE CODE REFERENCE
# ============================================================================

# SECTION 1: VARIABLES AND DATA TYPES
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

# SECTION 2: TYPE CASTING
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

# SECTION 3: ARITHMETIC OPERATORS
# ============================================================================

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

# SECTION 4: COMPARISON OPERATORS
# ============================================================================

x = 10
y = 20

print(f"{x} == {y}: {x == y}")  # False
print(f"{x} != {y}: {x != y}")  # True
print(f"{x} < {y}: {x < y}")   # True
print(f"{x} > {y}: {x > y}")   # False
print(f"{x} <= {y}: {x <= y}") # True
print(f"{x} >= {y}: {x >= y}") # False

# SECTION 5: LOGICAL OPERATORS
# ============================================================================

condition1 = True
condition2 = False

print(f"{condition1} and {condition2}: {condition1 and condition2}")  # False
print(f"{condition1} or {condition2}: {condition1 or condition2}")   # True
print(f"not {condition1}: {not condition1}")                        # False
print(f"not {condition2}: {not condition2}")                        # True

# SECTION 6: ASSIGNMENT OPERATORS
# ============================================================================

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

# SECTION 7: MEMBERSHIP OPERATORS
# ============================================================================

fruits_list = ["apple", "banana", "orange"]

print("apple" in fruits_list)        # True
print("grape" in fruits_list)        # False
print("apple" not in fruits_list)    # False
print("grape" not in fruits_list)    # True

# SECTION 8: IDENTITY OPERATORS
# ============================================================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is not list2: {list1 is not list2}")  # True
print(f"list1 is list3: {list1 is list3}")  # True (same object)
print(f"list1 == list2: {list1 == list2}")  # True (same content)

# SECTION 9: COMPLEX EXPRESSIONS
# ============================================================================

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Calculating average
scores = [95, 88, 92, 85, 90]
average_score = sum(scores) / len(scores)
print(f"Average score: {average_score}")

# String concatenation and type casting
first_name = "Al"
last_name = "Faiz"
age = 25
full_info = first_name + " " + last_name + " is " + str(age) + " years old"
print(full_info)

# Using f-strings (Python 3.6+)
full_info_f = f"{first_name} {last_name} is {age} years old"
print(full_info_f)

# SECTION 10: PRACTICAL EXAMPLES
# ============================================================================

# Calculator function
def calculate(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Unknown operation"

print("\n--- Calculator Examples ---")
print(f"10 + 5 = {calculate('+', 10, 5)}")
print(f"10 - 5 = {calculate('-', 10, 5)}")
print(f"10 * 5 = {calculate('*', 10, 5)}")
print(f"10 / 5 = {calculate('/', 10, 5)}")

# Grade assignment based on score
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("\n--- Grade Assignment ---")
for score in [95, 85, 75, 65, 55]:
    grade = assign_grade(score)
    print(f"Score: {score} -> Grade: {grade}")

print("\n✅ All examples completed successfully!")
```

---

## 🎓 Learning Outcomes

After completing this module, students will be able to:

✅ Understand Python's syntax and basic structure  
✅ Declare and use variables effectively  
✅ Work with different data types (int, float, str, bool, collections)  
✅ Perform type conversions when needed  
✅ Use arithmetic, comparison, and logical operators  
✅ Write expressions and solve real-world problems  
✅ Understand when to use different data types  
✅ Apply operators in practical scenarios

---

## 🚀 Next Steps

After mastering Python Syntax & Data Types, proceed to:
1. **Control Structures** - Learn if/else, loops
2. **Data Structures** - Deep dive into lists, dictionaries, sets
3. **Functions** - Create reusable code
4. **OOP** - Object-Oriented Programming concepts

---

## 📊 Quick Reference

**Data Types Summary:**
- `int`: Whole numbers
- `float`: Decimal numbers
- `str`: Text/characters
- `bool`: True/False
- `list`: Ordered, mutable collection
- `tuple`: Ordered, immutable collection
- `dict`: Key-value pairs

**Common Functions:**
- `type(x)`: Get the data type
- `len(x)`: Get length/count
- `int()`, `float()`, `str()`, `bool()`: Type conversion
- `print()`: Display output
- `input()`: Get user input

---

**Happy Learning! 🎉**

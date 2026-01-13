"""Module 8: Input and Output Examples
Different ways to take input and display output in Python
"""

# Example 1: Basic input and output
print("=" * 50)
print("EXAMPLE 1: Basic Input and Output")
print("=" * 50)

# Taking input from user
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Example 2: Type conversion
print("\n" + "=" * 50)
print("EXAMPLE 2: Taking Integer Input")
print("=" * 50)

age = int(input("Enter your age: "))
print(f"Your age is: {age}")
print(f"Next year you will be: {age + 1}")

# Example 3: Taking multiple inputs
print("\n" + "=" * 50)
print("EXAMPLE 3: Multiple Inputs")
print("=" * 50)

x, y = input("Enter two numbers separated by space: ").split()
print(f"First number: {x}")
print(f"Second number: {y}")

# Example 4: Float input and calculations
print("\n" + "=" * 50)
print("EXAMPLE 4: Float Input and Calculations")
print("=" * 50)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Example 5: String operations
print("\n" + "=" * 50)
print("EXAMPLE 5: String Input Operations")
print("=" * 50)

sentence = input("Enter a sentence: ")
print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")

# Example 6: List of numbers
print("\n" + "=" * 50)
print("EXAMPLE 6: Processing List of Numbers")
print("=" * 50)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# Example 7: Using print with different separators
print("\n" + "=" * 50)
print("EXAMPLE 7: Print with Different Separators")
print("=" * 50)

print("A", "B", "C", sep="-")
print("Item1", "Item2", "Item3", sep=" | ")
print("Start", "End", sep=" --> ")

# Example 8: Using print with different end parameters
print("\n" + "=" * 50)
print("EXAMPLE 8: Print with Different End Parameters")
print("=" * 50)

print("Loading", end="")
for i in range(3):
    print(".", end="")
print("Done!")

print("\n" + "=" * 50)
print("All examples completed!")
print("=" * 50)

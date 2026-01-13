"""
╔═══════════════════════════════════════════════════════════════════════════╗
║         MODULE 1: VARIABLES AND DATA TYPES IN PYTHON                      ║
║     Understanding variable assignment and different data types             ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 1: Variable Case Sensitivity
# ═════════════════════════════════════════════════════════════════════════════
print("\n" + "="*80)
print("EXAMPLE 1: VARIABLE CASE SENSITIVITY")
print("="*80)
print("Description: Variables are case-sensitive in Python\n")

x = int(input("➤ Enter value for x (lowercase): "))
X = int(input("➤ Enter value for X (uppercase): "))
print(f"📊 Value of x: {x}")
print(f"📊 Value of X: {X}")
print(f"ℹ️  x and X are DIFFERENT variables!\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 2: String Concatenation
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 2: STRING CONCATENATION")
print("="*80)
print("Description: Combining strings with concatenation operator (+)\n")

greeting = "Hello"
name = input("➤ Enter your name: ")
print(f"📝 Greeting variable: {greeting}")
print(f"👤 Name variable: {name}")
print(f"✨ Result: {greeting + ', ' + name + '!'}\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 3: String Input and Data Type
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 3: STRING DATA TYPE")
print("="*80)
print("Description: Taking and displaying string input\n")

A = str(input("➤ Enter any text: "))
print(f"📌 Type of input: <class 'str'>")
print(f"📌 Value: {A}")
print(f"📌 Length: {len(A)} characters\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 4: Float Input and Arithmetic Operations
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 4: FLOAT INPUT AND ARITHMETIC")
print("="*80)
print("Description: Working with floating-point numbers\n")

a = float(input("➤ Enter a number: "))
print(f"📌 Number entered: {a}")
print(f"📊 Square of {a}: {a * a}")
print(f"📊 Formula: {a} × {a} = {a * a:.2f}\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 5: Temperature Conversion (Celsius to Fahrenheit)
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 5: TEMPERATURE CONVERSION")
print("="*80)
print("Description: Converting Celsius to Fahrenheit\n")

celsius = float(input("➤ Enter temperature in Celsius: "))
fahren = (celsius * 9/5) + 32
print(f"🌡️  Celsius: {celsius}°C")
print(f"🌡️  Fahrenheit: {fahren:.2f}°F")
print(f"📈 Formula: (°C × 9/5) + 32 = °F\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 6: Mixed Data Type Operations
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 6: MIXED DATA TYPES")
print("="*80)
print("Description: Adding different numeric types (int + float)\n")

x = int(input("➤ Enter an integer: "))
y = float(input("➤ Enter a float: "))
z = int(input("➤ Enter another integer: "))

sum_result = x + y + z
product = x * y * z

print(f"\n📊 Integer x: {x}")
print(f"📊 Float y: {y}")
print(f"📊 Integer z: {z}")
print(f"➕ Sum (x + y + z): {sum_result}")
print(f"✖️  Product (x × y × z): {product:.2f}\n")


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 7: Data Type Detection and Classification
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 7: DATA TYPE CLASSIFICATION")
print("="*80)
print("Description: Identifying data types (Boolean, Integer, Float, String)\n")

import sys

def detect_data_type():
    """Detect and classify input data type"""
    data = input("➤ Enter a value (True/False/number/text): ").strip()
    
    if data == "True" or data == "False":
        result_type = "Boolean"
    elif data.isdigit() or (data[0] == '-' and data[1:].isdigit()):
        result_type = "Integer"
    elif data.count('.') == 1:
        parts = data.split('.')
        if (parts[0].isdigit() or parts[0] == "-" or parts[0] == "") and \
           (parts[1].isdigit() or parts[1] == ""):
            result_type = "Float"
        else:
            result_type = "String"
    else:
        result_type = "String"
    
    print(f"\n📌 Input: {data}")
    print(f"🔍 Detected Type: {result_type}\n")

detect_data_type()


# ═════════════════════════════════════════════════════════════════════════════
# EXAMPLE 8: File Path Construction with Variables
# ═════════════════════════════════════════════════════════════════════════════
print("="*80)
print("EXAMPLE 8: DYNAMIC FILE PATH CONSTRUCTION")
print("="*80)
print("Description: Building file paths with multiple variables\n")

folder_name = input("➤ Enter folder name: ")
subfolder_name = input("➤ Enter subfolder name: ")
file_base_name = input("➤ Enter file name (without extension): ")
drive_number = int(input("➤ Enter drive number (3-10): "))
file_extension = input("➤ Enter file extension (e.g., .txt, .py): ")
separator_type = input("➤ Choose separator (forward/backward): ")

full_file_name = file_base_name + file_extension
forward_sep = "/"
backward_sep = "\\"

# Drive letter mapping
drive_map = {
    3: 'D', 4: 'F', 5: 'H', 6: 'J',
    7: 'L', 8: 'N', 9: 'P', 10: 'R'
}

drive_letter = drive_map.get(drive_number, 'C')

# Build paths
linux_path = forward_sep + folder_name + forward_sep + subfolder_name + forward_sep + full_file_name
windows_path = drive_letter + ":\\" + folder_name + "\\" + subfolder_name + "\\" + full_file_name

final_path = linux_path if separator_type == "forward" else windows_path

print(f"\n📁 Folder: {folder_name}")
print(f"📁 Subfolder: {subfolder_name}")
print(f"📄 File: {full_file_name}")
print(f"💾 Drive: {drive_letter}:")
print(f"🔀 Separator: {separator_type}")
print(f"\n✨ Final Path: {final_path}\n")


print("="*80)
print("✨ ALL 8 EXAMPLES COMPLETED SUCCESSFULLY! ✨")
print("="*80)
print("\n📚 Module Summary:")
print("   1️⃣  Variable case sensitivity")
print("   2️⃣  String concatenation")
print("   3️⃣  String data type")
print("   4️⃣  Float arithmetic operations")
print("   5️⃣  Temperature conversion")
print("   6️⃣  Mixed data type operations")
print("   7️⃣  Data type classification")
print("   8️⃣  Dynamic file path construction")
print("="*80 + "\n")

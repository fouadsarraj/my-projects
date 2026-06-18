# 1. Define mathematical operations as functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

# 2. Main loop
while True:
    print("\n--- Python Calculator ---")
    operator = input("Select operation (+, -, *, /) or 'exit': ")
    if operator.lower() == 'exit': break
        
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # 3. Perform calculation
        if operator == '+': print(f"Result: {add(num1, num2)}")
        elif operator == '-': print(f"Result: {subtract(num1, num2)}")
        elif operator == '*': print(f"Result: {multiply(num1, num2)}")
        elif operator == '/': print(f"Result: {divide(num1, num2)}")
        else: print("Invalid operator.")
    except ValueError:
        print("Invalid input. Please enter numbers.")

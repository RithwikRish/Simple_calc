def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print("Simple Calculator — type 'quit' to exit\n")
    while True:
        try:
            user_input = input("Enter expression (e.g. 3 + 4): ").strip()
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Please use the format: number operator number\n")
                continue

            a, op, b = parts
            a, b = float(a), float(b)

            if op not in OPERATIONS:
                print(f"Unsupported operator '{op}'. Use +, -, *, /\n")
                continue

            result = OPERATIONS[op](a, b)
            # Display as int if result is a whole number
            print(f"= {int(result) if result == int(result) else result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    calculator()

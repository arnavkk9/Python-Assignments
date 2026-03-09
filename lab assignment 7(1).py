def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def mod(a, b):
    return a % b


while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(num1, num2))
    elif choice == 2:
        print("Result =", sub(num1, num2))
    elif choice == 3:
        print("Result =", mul(num1, num2))
    elif choice == 4:
        print("Result =", div(num1, num2))
    elif choice == 5:
        print("Result =", mod(num1, num2))
    else:
        print("Invalid choice")

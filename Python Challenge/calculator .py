def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error! Division by zero."

def main():
    print("Welcome to the basic calculator!")
    print("Operations: +, -, *, /")

    while True:
        print("Enter choice of operation:")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operations = {'1': '+', '2': '-', '3': '*', '4': '/'}
            operation = operations[choice]
            result = calculate(num1, num2, operation)
            print(f"Result: {num1} {operation} {num2} = {result}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

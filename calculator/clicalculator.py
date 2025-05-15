def calculate(num1, num2, operation):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        if num2 == 0:
            return "Error! Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation input"

print("Simple CLI Calculator")
print("Operations:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("Type 'exit' to quit")

result = None

while True:
    if result is None:
        user_input = input("Enter a number: ")
        if user_input.lower() == "exit":
            print("Exiting calculator.")
            break
        try:
            result = float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
    else:
        operation = input("Enter operation (1/2/3/4) or 'exit' to quit: ")
        if operation.lower() == "exit":
            print("Exiting calculator.")
            break
        if operation not in ["1", "2", "3", "4"]:
            print("Invalid operation! Please enter 1, 2, 3, or 4.")
            continue
        user_input = input("Enter next number: ")
        if user_input.lower() == "exit":
            print("Exiting calculator.")
            break
        try:
            num = float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        result = calculate(result, num, operation)
        print("Result:", result)
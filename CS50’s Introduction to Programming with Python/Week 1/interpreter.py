def evaluate_expression(expression):
    # Split the expression into operands and operator
    x, operator, y = expression.split()

    # Convert operands to floats
    x = float(x)
    y = float(y)

    # Perform arithmetic operation based on the operator
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        # Check if y is not zero to avoid division by zero error
        if y != 0:
            result = x / y
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"

    # Format the result to one decimal place and return
    return round(result, 1)


def main():
    # Prompt the user for input
    expression = input("Enter an arithmetic expression (format: x y z): ")

    # Evaluate the expression
    result = evaluate_expression(expression)

    # Output the result
    print("Result:", result)


if __name__ == "__main__":
    main()

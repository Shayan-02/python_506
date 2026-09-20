def add(num1: int, num2: int) -> str:
    """
    Add two integers and return the formatted result.

    Args:
        num1 (int): The first integer operand.
        num2 (int): The second integer operand.

    Returns:
        str: A formatted string containing the two operands and their sum.
    """
    return f"{num1} {op} {num2} = {num1 + num2}"


def minus(num1: int, num2: int) -> str:
    """
    Subtract the second integer from the first and return the formatted result.

    Args:
        num1 (int): The first integer operand.
        num2 (int): The second integer operand.

    Returns:
        str: A formatted string containing the two operands and their difference.
    """
    return f"{num1} {op} {num2} = {num1 - num2}"


def multiply(num1: int, num2: int) -> str:
    """
    Multiply two integers and return the formatted result.

    Args:
        num1 (int): The first integer operand.
        num2 (int): The second integer operand.

    Returns:
        str: A formatted string containing the two operands and their product.
    """
    return f"{num1} {op} {num2} = {num1 * num2}"


def divide(num1: int, num2: int) -> str:
    """
    Divide the first integer by the second and return the formatted result.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        str: A formatted string containing the operands and division result.
             If the divisor is zero, returns an error message instead.

    Notes:
        Integer results are displayed without a decimal part.
    """
    if num2 != 0:
        result = num1 / num2

        # Display integer results without the decimal part.
        if result == int(result):
            return f"{num1} / {num2} = {int(result)}"

        return f"{num1} / {num2} = {result}"

    return "Can't divide by zero."


# Read the first number, operator, and second number from the user.
num1: int = int(input())
op: str = input()
num2: int = int(input())

# Select the appropriate operation based on the input operator.
if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(minus(num1, num2))
elif op == "*":
    print(multiply(num1, num2))
elif op == "/":
    print(divide(num1, num2))



def parse_expression(expression):
    parts = expression.split()

    if len(parts) != 3:
        return None

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        return num1, operator, num2

    except ValueError:
        return None


def calculate(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return None

        return num1 / num2

    else:
        return None
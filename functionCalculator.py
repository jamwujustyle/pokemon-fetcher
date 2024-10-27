def calculator(num1, sym, num2):
    if (
        num1 is not None
        and num2 is not None
        and isinstance(num1, (int, float))
        and isinstance(num2, (int, float))
    ):
        if sym == "+":
            return round(num1 + num2, 3)
        elif sym == "-":
            return round(num1 - num2, 3)
        elif sym == "*":
            return round(num1 * num2, 3)
        elif sym == "/":
            if num2 != 0:
                return round(num1 / num2, 3)
            else:
                return "Error: division by zero"
        else:
            return "Error: invalid operator"
    else:
        return "Error: invalid operand"

def calculate (operator, number1, number2):
    if operator == "+":
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        raise Exception (f"unknown operator: {operator}")
        

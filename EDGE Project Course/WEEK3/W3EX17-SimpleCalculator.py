

def calculator():
    num1=float(input("Enter first number : "))
    operator=input("Enter an operator(+,-<*,/) : ")
    num2=float(input("Enter second number : "))
    if operator=='+':
        result=num1+num2
    elif operator=='-':
        result = num1 - num2
    elif operator=='*':
        result = num1 * num2
    elif operator=='/':
        if num2!=0:
            result = num1 / num2
        else :
            return "Division by Zero is not allowed"
    else :
        return "Invalid Operator"
    return f"The result is : {result}"

print(calculator())
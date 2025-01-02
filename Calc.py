number1 = float(input("Enter the first number: "))
operator = (input("Enter a symbol: **,-,/,*,+: "))
number2 = float(input("Enter a second number: "))


def calculator(number1, operator, number2):

    if operator == '**':
        operator2 = (input("Now please enter a second operator: "))
        number3 = float(input("please add in a third number: "))

        if operator2 == '**':
            print(number1 ** number2 ** number3)
        elif operator2 == '-':
            print(number1 ** number2 - number3)
        elif operator2 == '/':
            print(number1 ** number2 / number3)
        elif operator2 == '*':
            print(number1 ** number2 * number3)
        elif operator2 == '+':
            print(number1 ** number2 + number3)
        else:
            print("You have not selected a second operator")

    elif operator == '-':
        print(number1 - number2)

    elif operator == '/':
        print(number1 / number2)

    elif operator == '*':
        print(number1 * number2)

    elif operator == '+':
        print(number1 + number2)
    else:
        print("Invalid symbol or no symbol has been enterd")


calculator(number1, operator, number2)

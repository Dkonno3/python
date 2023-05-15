from art import logo

print(logo)


def soma(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


result = 0
run = True
operations = {
    "+": soma,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}
firstnum = float(input("Enter the first number: "))
while run:
    for symbol in operations:
        print(symbol)
    operation = input(f"select the operation above:")
    secondnum = float(input("Enter the second number: "))
    calculate = operations[operation]
    result = calculate(firstnum, secondnum)
    print(f"{firstnum} {operation} {secondnum} = {result}")
    print(f"Type 'y' to continue calculating with {result} or 'n' to start a new operation, to stop enter any other "
          f"key: ")
    question = input().lower()
    if question == "y" or question == "yes":
        firstnum = result
    elif question == "n" or question == "no":
        firstnum = float(input("Enter the first number: "))
    else:
        run = False
        break

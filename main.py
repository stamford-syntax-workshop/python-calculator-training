# Add your functions here!

# tawan
def add(input1, input2):
    return input1 + input2

# pumin
def subtract(input1, input2):
    return input1 - input2

# bas
def multiply(input1, input2):
    return input1 * input2

# naris
def divide(input1, input2):
    return input1 / input2

# ana
def modulo(input1, input2):
    return input1 % input2

def main():
    print("Enter the operation you want to perform: ")

    user_operation = input()
    user_input1 = int(input("Enter the first number: "))
    user_input2 = int(input("Enter the second number: "))

    if user_operation == "add":
        add(user_input1, user_input2)
    elif user_operation == "subtract":
        subtract(user_input1, user_input2)
    elif user_operation == "multiply":
        multiply(user_input1, user_input2)
    elif user_operation == "divide":
        divide(user_input1, user_input2)
    elif user_operation == "modulo":
        modulo(user_input1, user_input2)


main()

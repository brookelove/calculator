# need to import the arethmatic functions
from cmath import pi
from arethmatic import add, divide, subtract, multiply
# need first ask for a persons input
print("What would you like to calculate today?\nSubmit the number of the corresponding mathmatic calculation.\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
userResponse = input()
# have to give a response of what the person wants then ask them for the two numbers that they want to calculate
# have to have conditional statements for what they want to do
if userResponse == '1':
    # this is adding
    print("You want to add two numbers together")
    num1 = input("What's the first number: ")
    num2 = input("What's the second number: ")
    result = add(int(num1), int(num2))
    print("The resulting number is", str(result))
elif userResponse == '2':
    # this is subtracting
    print("You want to subtract two numbers together")
    num1 = input("What's the first number: ")
    num2 = input("What's the second number: ")
    result = subtract(int(num1), int(num2))
    print("The resulting number is", str(result))
elif userResponse == '3':
    # this is multiplying
    print("You want to multiply two numbers together")
    num1 = input("What's the first number: ")
    num2 = input("What's the second number: ")
    result = multiply(int(num1), int(num2))
    print("The resulting number is", str(result))
else:
    # this is dividing
    print("You want to divide two numbers together")
    num1 = input("What's the first number: ")
    num2 = input("What's the second number: ")
    result = divide(int(num1), int(num2))
    print("The resulting number is", str(result))
    # have two numbers that are num 1 and num 2

    # print the num 1 used and the num 2

print('Welcome to my calculator program')


# Add a prompt icon for display purposes
def prompt(message):
    print(f"==> {message}")


# Define an invalid number
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False


# Ask the user for the first number
prompt('What is the first number?')
num1 = input()

# Check validity of first number
while invalid_number(num1):
    prompt("Hmm... That doesn't look like a valid number")
    num1 = input()

# Ask the user for the second number
prompt('What is the second number?')
num2 = input()

# Check validity of second number
while invalid_number(num2):
    prompt("Hmm... That doesn't look like a valid number")
    num2 = input()

# Ask the user for the operation to be performed
prompt('What operation would you like to be performed?\n1)Add '
       '2) Subtract 3)Multiply 4) Divide 5')
operation = input()

# Check validity of operation selection
while invalid_number(operation):
    prompt("Hmm... That doesn't look like a valid operation")
    operation = input()

# Perform the calculation of the two numbers - change to case match
match operation:
    case '1':
        result = int(num1) + int(num2)
    case '2':
        result = int(num1) - int(num2)
    case '3':
        result = int(num1) * int(num2)
    case '4':
        result = int(num1) / int(num2)

# Display the result of the calculation
prompt(f"The answer is {result}!")

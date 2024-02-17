"""
Calculator program that takes two numbers 
and an operation and performs the operation
on the two numbers.
"""
def prompt(message):
    print(f'=> {message}')
    
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False


# Ask the user for the first number
# Ask the user for the second number
# Ask the user for the operation
# Perform the operation
# Print the result

prompt('Welcome to the calculator!')

prompt('Enter the first number:')
number1 = input()

while invalid_number(number1):
    prompt('Invalid number. Please enter a valid number:')
    number1 = input()
    
prompt('Enter the second number:')
number2 = input()

while invalid_number(number2):
    prompt('Invalid number. Please enter a valid number:')
    number2 = input()
    
prompt("""What operation would you like to 
perform? 1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('Invalid operation. You must choose 1, 2, 3, or 4:')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)
    

prompt(f'The result is {output}')
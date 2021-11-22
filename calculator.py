from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

keep_going = True
keep_running = True

while keep_running == True:
    print(logo)
    print("\nWelcome to the start of your operations.")
    num1 = float(input("\nWhat is the first number? : "))

    for operation in operations:
        print(operation)

    operation_symbol = input("\nPick an operation from the list above: ")
    key_list = list(dict.keys(operations))

    if not operation_symbol in key_list:
        print("\nThat is not a valid operation. \n")
    else:
        num2 = float(input("\nWhat is the second number? : "))
        function = operations[operation_symbol]
        answer = function(num1, num2)


    print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")

    response = input("\nType 'y' if you would like to keep going with this operation, 'n' if you would like to start afresh, or 'exit' if you would like to close the program : ")

    if response == 'n':
        clear()
    elif response == 'y':
        while keep_going == True:
            for operation in operations:
                print(operation)

            operation_symbol = input("\nPick an operation from the list above: ")
            key_list = list(dict.keys(operations))

            if not operation_symbol in key_list:
                print("\nThat is not a valid operation. \n")
            else:
                num2 = float(input("\nWhat is the next number? : "))
                function = operations[operation_symbol]
                answer = function(answer, num2)

            print(f"\n{answer} {operation_symbol} {num2} = {answer}\n")

            response = input("\nType 'y' if you would like to keep going with this operation, 'n' if you would like to start afresh, or 'exit' if you would like to close the program : ")

            if response == 'y':
                continue
            elif response == 'n':
                keep_going == False
                break
            else:
                clear()
                keep_running = False
            

    else:
        clear()
        keep_running = False



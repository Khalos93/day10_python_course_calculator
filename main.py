from util import calculate, operations_available, possible_user_follow_up

print("Welcome to this simple calculator..!")

calculator_is_on = True
while calculator_is_on:

    first_number = float(input("Digit your first number"))
    while type(first_number) is not float:
        first_number = float(input("Digit your first number"))
    continue_with_result = True
    initial_number = None
    while continue_with_result:

        if first_number is not None:
            initial_number = first_number
            first_number = None
        print(initial_number)
        operator = input("What operation you would like to perform? Type +, -, *, / ")
        while operator not in operations_available:
            operator = input("What operation you would like to perform? Type +, -, *, / ")

        second_number = float(input("Digit your second number"))
        while type(second_number) is not float:
            second_number = float(input("Digit your second number"))

        result = calculate(initial_number, operator, second_number)

        print(result)
        print("\n" * 3)
        next_user_decision = input("Do you want to progress further with this result or starting anew? "
                                   "Type C to continue or N to reset the calculator").lower()

        while next_user_decision not in possible_user_follow_up:
            next_user_decision = input("Do you want to progress further with this result or starting anew? "
                                       "Type C to continue or N to reset the calculator").lower()
        if next_user_decision == "c":
            initial_number = result
        elif next_user_decision == "n":
            continue_with_result = False
        elif next_user_decision == "e":
            continue_with_result = False
            calculator_is_on = False



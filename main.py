from util import calculate, operations_available, possible_user_follow_up, get_float_input, get_valid_input

print("Welcome to this simple calculator..!\n")

calculator_is_on = True
while calculator_is_on:

    first_number = get_float_input("Digit your first number")

    continue_with_result = True
    initial_number = None
    while continue_with_result:

        if first_number is not None:
            initial_number = first_number
            first_number = None
        print(initial_number)
        operator = get_valid_input("What operation you would like to perform? Type +, -, *, / ", operations_available)

        second_number = get_float_input("Digit your second number")

        result = calculate(initial_number, operator, second_number)

        print(f"Result: {result}\n")
        print("\n" * 3)
        next_user_decision = get_valid_input("Do you want to progress further with this result or starting anew? "
                                             "Type C to continue or N to reset the calculator", possible_user_follow_up)
        if next_user_decision == "c":
            initial_number = result
        else:
            continue_with_result = False
            if next_user_decision == "e":
                calculator_is_on = False


def calculate(first_n:float, operator_input:str, second_n:float)->float:
    if operator_input == "+":
        return first_n + second_n
    elif operator_input == "-":
        return  first_n - second_n
    elif operator_input == "*":
        return first_n * second_n
    elif operator_input == "/":
        return  first_n / second_n


operations_available = {
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/"
}

possible_user_follow_up = ("c", "n", "e")
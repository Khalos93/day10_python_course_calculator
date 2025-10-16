def calculate(first_n: float, operator_input: str, second_n: float) -> float:
    if operator_input == "+":
        return first_n + second_n
    elif operator_input == "-":
        return first_n - second_n
    elif operator_input == "*":
        return first_n * second_n
    elif operator_input == "/":
        return first_n / second_n


operations_available = ("+", "-", "*", "/")

possible_user_follow_up = ("c", "n", "e")


def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_valid_input(prompt: str, valid_options: tuple[str, ...]) -> str:
    while True:
        value = input(prompt).lower()
        if value in valid_options:
            return value
        print("Invalid input. Try again.")

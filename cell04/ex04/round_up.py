import math
user_input = input("Give me a number: ")
try:
    number = float(user_input)
    rounded_number = math.ceil(number)
    print(f"{rounded_number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
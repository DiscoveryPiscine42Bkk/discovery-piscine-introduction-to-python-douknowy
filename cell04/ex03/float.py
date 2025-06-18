user_input = input("Give me a number: ")
try:
    number = float(user_input)
    if number.is_integer():
        print("This number is NOT a decimal.")
    else:
        print("This number iS a decimal.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
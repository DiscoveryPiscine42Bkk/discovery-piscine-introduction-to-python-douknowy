num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))
print("Thank you")
print(f"\nResults:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Division by zero is not allowed.")
    
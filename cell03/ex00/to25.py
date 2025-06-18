num = int(input("Enter a number: "))
if num > 25:
    print("Error")
else:
    for num in range(num, 26):
        print(f"Inside the loop, my variable is {num}")
        
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 13):
    result = num * i
    print(f"{num} x {i} = {result}")
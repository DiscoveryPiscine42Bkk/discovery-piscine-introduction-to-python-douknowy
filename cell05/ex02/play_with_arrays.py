original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for num in original_array:
    if num > 5:
        new_array.append(num + 2)
print("Original array:", original_array)
print("New array (only values > 5, then +2):", new_array)
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
seen = set()
for num in original_array:
    if num > 5:
        result = num + 2
        if result not in seen:
            new_array.append(result)
            seen.add(result)
print("Original array:", original_array)
print("New array (values > 5, +2, no duplicates):", new_array)
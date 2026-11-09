numbers = [2, 3, 2, 4, 3, 5, 5]
result = 0
for num in numbers:
    result = result ^ num
if result != 0:
    print("The odd occurring number is:", result)
else:
    print("No odd occurring number found")

numbers = [1,2,3,2,7,2,3,6]

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

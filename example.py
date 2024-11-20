numbers = [5,2,5,2,2]
for x in numbers:
    print(x * "x")
    
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)     
         
         
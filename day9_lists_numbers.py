# Day 9: Working with lists of numbers

numbers = [2, 4, 5, 6, 8]

total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)

print("Total is", total)
print("Average is", average)

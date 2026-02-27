# Day 10: Lists, Loops, Total and Average
# Author: Ezekiel Kang'ombe

numbers = []

for i in range(3):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Numbers entered:", numbers)

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print("Total is", total)
print("Average is", average)

# Day 11: Functions – Total and Average
# Author: Ezekiel Kang'ombe

def calculate_total_and_average():
    numbers = []

    for i in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)

    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)

    print("Numbers entered:", numbers)
    print("Total is", total)
    print("Average is", average)

# Function call
calculate_total_and_average()

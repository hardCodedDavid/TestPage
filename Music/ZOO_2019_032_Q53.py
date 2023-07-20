import random

def generate_numbers(n, start, end):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(start, end))
    return numbers

n = int(input("Enter the number of random numbers to generate: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

numbers = generate_numbers(n, start, end)

print("Original list of numbers:")
print(numbers)

ascending = sorted(numbers)
print("Numbers in ascending order:")
print(ascending)

descending = sorted(numbers, reverse=True)
print("Numbers in descending order:")
print(descending)

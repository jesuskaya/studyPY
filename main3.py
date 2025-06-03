# Задача: Напиши программу, которая получает список чисел и находит все уникальные чётные числа.


user_input = input("Enter numbers (separated by space or comma): ")

numbers_str = user_input.split()

numbers = [int(num) for num in numbers_str]

unique_numbers = set(numbers)

for num in unique_numbers:
    if num % 2 == 0:
        print(f"{num} is even")

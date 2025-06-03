# Написать программу, которая принимает список чисел и выводит все числа, которые делятся на 3 и 5.

user_input = input("Enter some numbers: ")
numbers_str = user_input.split()
numbers_int = [int(num) for num in numbers_str]

def division(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False

for num in numbers_int:
    if division(num):
        print(f"The number {num} is divisible by both 3 and 5.")

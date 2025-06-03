# Напиши программу, которая из списка чисел находит все числа, которые являются простыми.
import math

user_input = input("Enter some numbers separated by space: ")

numbers_str = user_input.split()

numbers_int = [int(num) for num in numbers_str]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for num in numbers_int:
    if is_prime(num):
        print(f"The number {num} is a prime.")

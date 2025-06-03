#Напиши программу, которая получает список чисел и находит два наибольших числа. Если таких чисел несколько, выведи все.

user_input = input("Enter numbers separated by a space: ")

numbers_str = user_input.split()

numbers = [int(num) for num in numbers_str]

# Проверяем, есть ли в списке хотя бы два числа
if len(numbers) < 2:
    print("Not enough numbers to find two maximum values.")
else:
    sorted_numbers = sorted(numbers)

    max_number = max(numbers)

    # Удаляем первое максимальное число
    numbers.remove(max_number)

    max_number2 = max(numbers)  # Находим следующее максимальное

    # Удаляем второе максимальное число
    numbers.remove(max_number2)

    print(f"First maximum number is {max_number} and the second maximum number is {max_number2}")



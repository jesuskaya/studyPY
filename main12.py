# Найти все числа Фибоначчи в заданном диапазоне


lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

a = 0
b = 1

fib_numbers = []

while a <= upper_bound:
    if a >= lower_bound and a <= upper_bound:
        fib_numbers.append(a)
    a, b = b, a + b

print(f"Fibonacci numbers in range [{lower_bound}, {upper_bound}]: {fib_numbers}")





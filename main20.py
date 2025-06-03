def calculator(a, b, operation):
    match operation:
        case "+":
            return f"{a} + {b} = {a + b}"
        case "-":
            return f"{a} - {b} = {a - b}"
        case "*":
            return f"{a} * {b} = {a * b}"
        case "/":
            return f"{a} / {b} = {a / b}" if b != 0 else "Ошибка: деление на ноль"
        case _:
            return "Ошибка: неизвестная операция"

# Ввод данных
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

# Вывод результата
print(calculator(num1, num2, op))

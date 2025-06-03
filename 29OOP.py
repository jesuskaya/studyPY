import tkinter as tk
import random

# Список головоломок
puzzles = [
    {"question": "Перед вами три двери: \n1) За первой дверью — огненная ловушка.\n2) За второй — голодные волки.\n3) За третьей — магическая стена.\nКакая дверь безопаснее?",
     "answer": "3", "hint": "Магическая стена может быть иллюзией."},
    {"question": "У вас есть два сосуда: 5 литров и 3 литра. Как отмерить ровно 4 литра?",
     "answer": "налить 3 в 5, потом еще 3, вылить 5 и перелить 3", "hint": "Используй оба сосуда."},
    {"question": "Что идёт вверх, но никогда не опускается?",
     "answer": "возраст", "hint": "Стареет каждый."}
]

# Выбираем случайную головоломку
puzzle = random.choice(puzzles)

# Функция проверки ответа
def check_answer():
    user_input = entry.get().strip().lower()
    if user_input == puzzle["answer"].lower():
        result_label.config(text="Верно! Вы прошли испытание!", fg="green")
    else:
        result_label.config(text="Неверно! Попробуйте ещё раз.", fg="red")

# Создаём графическое окно
root = tk.Tk()
root.title("Головоломка D&D")
root.geometry("500x300")

# Текст с головоломкой
question_label = tk.Label(root, text=puzzle["question"], wraplength=480, font=("Arial", 12))
question_label.pack(pady=20)

# Поле ввода
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

# Кнопка проверки ответа
submit_button = tk.Button(root, text="Ответить", command=check_answer, font=("Arial", 12))
submit_button.pack(pady=10)

# Лейбл с результатом
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Подсказка
hint_label = tk.Label(root, text=f"Подсказка: {puzzle['hint']}", font=("Arial", 10), fg="gray")
hint_label.pack(pady=5)

root.mainloop()
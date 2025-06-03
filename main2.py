# Задача: Создайте программу для подсчёта всех гласных букв в строке


text = input("Write your text: ")
print(text)
vowels = "aeiou"
text = text.lower()
vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} # Объявил словарь вне цикла, в начале в цикле поэтому ошибка.

for char in text:
    if char in vowels:
        vowels_count[char] += 1

total_vowels = sum(vowels_count.values())  # подсчёт тоже за циклом
for vowel, count in vowels_count.items():  # покажет количество каждой гласной отдельно
    print(f"The letter '{vowel}' appears {count} times.")





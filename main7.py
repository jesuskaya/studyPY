# Найти самое часто встречающееся слово в тексте

text = input("Write your text here: ")

words = text.split()
words_lower = [word.lower() for word in text.split()]

my_dict = {}

for key in words_lower:
    if key in my_dict:
        my_dict[key] += 1
    else:
        my_dict[key] = 1


most_common_word = max(my_dict, key=my_dict.get)

print(f"The most common word is {most_common_word} and the number of times it occurs {my_dict[most_common_word]}")


# Напиши программу, которая подсчитывает, сколько раз каждое слово встречается в тексте, игнорируя регистр.
from collections import Counter


text = input("Enter a sentence: ")
words = text.split()
lower_word = [word.lower() for word in words]

words_count = Counter(lower_word)
most_common_word, count = words_count.most_common(1)[0]

print(f"The most common word is: {most_common_word}, it appears {count} times.")


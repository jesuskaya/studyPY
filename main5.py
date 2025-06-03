# Напиши программу, которая получает строку от пользователя и находит все уникальные слова,
# отсортированные в лексикографическом порядке (по алфавиту).

text = input("Enter a string: ")
words = text.split()
unique_words = set(words)
sorted_unique_words = sorted(unique_words)


print("Sorted unique words:", sorted_unique_words)




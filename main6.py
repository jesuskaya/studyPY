# Найти самое длинное слово в строке

text = input("Write some text here: ").strip()

if text:
    words = text.split()
    longest_word = max(words, key=len)
    len_word = len(longest_word)

    print(f"The longest word is {longest_word}. The length of the longest word is {len_word}.")

else:
    print("No text entered")


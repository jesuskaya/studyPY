my_img = ('1920', '1080')

if len(my_img) == 2:
    print(f"{my_img[0]}x{my_img[1]}")
else:
    print("Incorrect image formatting")

info = f"String is long" if len(my_img) > 79 else "String is short"

print(info)
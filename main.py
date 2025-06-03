import string


def password():
    while True:
        password = input("Enter your password: ")
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        if len(password) < 8:
            print("Password must be at least 8 characters long!")
            continue

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in string.punctuation:
                has_special = True

        if not has_upper:
            print("Password must contain at least one uppercase letter!")
        if not has_lower:
            print("Password must contain at least one lowercase letter!")
        if not has_digit:
            print("Password must contain at least one number!")
        if not has_special:
            print("Password must contain at least one special character!")

        if has_upper and has_lower and has_digit and has_special:
            print("Password correct!")
            break


password()

my_list = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9})

first_list, second_list, third_list = my_list

print(first_list)
print(second_list)
print(third_list)


def some_numbers(first, second):
    if not second:
        return f"There's no second list, only first: {first}"

    return f"first: {first} and second: {second}"


print(some_numbers(second_list, first_list))

print(some_numbers(first_list, second_list))

print(some_numbers(third_list, first_list))



"""
в нас є список чисел [1, 2, 3, 4, 5, 6, 7, 8]

потрібно написати функцію яка перебиратиме усі числа у списку та виводити лише парні числа

2, 4, 6, 8
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8]


def print_even_numbers(number_list):
    new_list = []
    # pass
    for number in number_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


# def other_function():
#     # ...

print(print_even_numbers(lst))

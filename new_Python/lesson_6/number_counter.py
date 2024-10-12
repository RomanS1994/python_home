from collections import Counter

'''
В нас є список чисел, потрібно написати функцію яка повертає кількість входжень чисел'''

numbers = [5, 0, 1, 2, 1, 1, 2, 2, 3, 5, 0]

# 1)Пройтися по усім числам списку
# 2.1)Якщо число не зустрічалося потрібно задати йому значення 1
# 2.2) Якщо число вже зустрічалося, потрібно взяти попереднє значення і збільшити його на 1
# 3) Зберегти інформацію
# 4) Повернути значення
#


def count_numbers_in_a_list(numbers_list: list[int]):
    counted_numbers = {}
    for number in numbers_list:
        if number in counted_numbers:
            counted_numbers[number] +=1
        else:
            counted_numbers[number] = 1
    return counted_numbers

print(count_numbers_in_a_list(numbers))


def count_numbers_in_a_list_alternative(numbers_list: list[int]):
    return Counter(numbers_list)

print(count_numbers_in_a_list_alternative(numbers))
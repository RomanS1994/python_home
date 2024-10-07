my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_string = "Hello, World!"

# print(my_list[:3]) - Перші три
# print(my_list[-3:]) - Останні три
# print(my_list[1:]) - всі крім першого
# print(my_list[:-1]) - крім останнього
# print(my_string[1:-1]) - без першого та останнього елемента
# print(my_list[2::2]) - кожен другий елемент

# print(my_list[::-2])


##### ---- зрізи з використанням змінних.
start = 1
end = 8
step = 2
# print(my_list[start:end])


# task1 Напишіть функцію, яка приймає рядок і повертає його середню частину (без першої та останньої літери).

str = "hello world"


def removestr(s):
    return s[1:-1]


# print(removestr(str))
# print(removestr(my_list))

# task2 Напишіть функцію, яка приймає список або рядок і повертає його у зворотному порядку.

# def revers(s):
#     return s[::-1]

# print(revers(my_list))

# task3 Напишіть функцію, яка видаляє певну кількість елементів з початку та кінця списку.

# def trim_list(lst: list, num: int):
#     return lst[num:-num]

# print(trim_list(my_list, 2))

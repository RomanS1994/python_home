# def new_func():
#     def get_numbers(x):
#         numbers = []
#         for i in range(x):
#             num = i ** 2
#             if not num % 2:
#                 numbers.append(num)
#         print(numbers)


#     def get_numbers_short(x):
#         print([i**2 for i in range(x) if not i%2])

#     get_numbers(10)
#     get_numbers_short(10)

# new_func()
# ==============================================================
# comprehension
# ==============================================================

# -------------------------
# 1 Ти можеш почати з простого завдання — створити список квадратів чисел від 1 до 10
def created_list(number):
    res = [char ** 2 for char in range(number)]
    print(res)


# created_list(11)


# 2 Створи список з довжин кожного слова у реченні:
sentence = "I am learning Python and improving my comprehension"

def created_word_lend(message):
    word_lend = {i: len(i) for i in message.split(' ')}
    print(word_lend)


# created_word_lend(sentence)


# 3 Перетвори список цілих чисел у список рядків:

numbers = [2, 3, 4, 5, 7, 23, 43, 52]

def transformations(lst):
    res = {i: str(i)  for i in lst if  not i % 2}
    print(res)


transformations(numbers)

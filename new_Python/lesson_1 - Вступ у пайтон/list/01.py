fruit_list = ["mango", "apple", "apple", "pear", "banana", "pomegranate"]
numbers = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
fruit_list.append("orange")
# fruit_list.clear()
# fruit_list.
fruit_list.sort()

# print(fruit_list)


# numbers.sort()
# number = numbers.pop(-1)
# numbers.insert(4,22)
# print(number)
# numbers.sort(reverse=True)
# print(numbers)


fruit_list = ["mango", "apple", "apple", "pear", "banana", "pomegranate"]

numbers = [
    1,
    3,
    2,
]
new_numbers = [5, 6, 7, 8]

# додавання
numbers.sort()  # сортує
numbers.append(4)  # додає в кінець
numbers.extend(new_numbers)  # Розширити
numbers.insert(0, 0)  # Вставити

# Видалення
numbers.remove(4)  # видаляє перше входження
# test = numbers.pop() # вирізає по індексу або з кінця
# print(test)
# print(numbers)


# print(numbers.index(4,2,6))
# print(numbers)


# ==============================================================
# task1 Додати числа 9, 10 і 11 в кінець списку

numbers.insert(4, 4)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test_numbers = [9, 10, 11]
numbers.extend(test_numbers)
# print(numbers)


# ==============================================================
# task2 Видалити всі входження числа 5 зі списку
numbers.remove(5)
# print(numbers)
# [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
numbers.insert(5, 5)
# print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# ==============================================================
# task.3 Знайти індекс числа 6 у списку і замінити його на 99
my_index = numbers[6]
numbers[my_index] = 99
print(numbers)

numbers[6] = 6
print(numbers)

# [0, 1, 2, 3, 4, 5, 99, 7, 8, 9, 10, 11]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

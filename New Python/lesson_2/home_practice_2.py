#### ============== Конструкція If
# a = 3
# if a > 2:
# print("True")
# else:
#     print("False")


#### ============== Ternarnik
# is_nice = 0
# state = "nice" if is_nice else "not nice"
# print(state)


#### ============== For
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2, end=" ")


#### ============== while
# a = 1
# while a:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

#
# a = 0
# while a < 6:
#     a = a + 1
#     print(a)
#     if not a % 2:
#         continue
#     print(a)
# a = 6
# print(a % 5)

# some_list = ["apple", "banana", "cherry"]
# for a, n in enumerate(some_list):
#     print(a, n)

#
# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for n1, m2 in zip(list1, list2):
#     print(n1, m2)

#### ============== Функції
# def say_hello (a: int, b: int):
#     if a > b:
#         print( "a is max, a > b")
#     elif a == b:
#         print("a = b")
#     else:
#         print("b is max, b > a")
# say_hello(4, 5)


# def calculator (a, b) -> float:
#     return a + b
#
# result = calculator(2, 4)
# print(type(result))


# def true_or_falce(a: int) -> bool:
#     return a % 2 == 0;
# print(true_or_falce(8))


# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}
#     # Перебір кожного символу в рядку
#     for ch in string:
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник
#             codes[ch] = ord(ch)
#     return codes
#
# print(string_to_codes("Roman"))
# # print(ord('a'))
# x = 43
# def func_outer():
#     x = 2
#
#     def func_inner():
#         nonlocal x
#
#         x = 5
#
#     func_inner()
#     return x
#
# result = func_outer()  # 5
# print(x)
# print(result)


# def say(message, times=1):
#     print(message  * times)
#
# say('Привіт')
# say('Світ ', 5)

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# greet(name="Alice", age=25, vigth=186)

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result
#
# print(factorial(5))


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
#
# while num > 0:
#     sum += num
#     num -= 1


#
# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#     return price * (1 - discount)
#
#     apply_discount()
#
#     return price
#
# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         return f"{first_name} {last_name} {middle_name}"
#     else:
#         return f"{first_name} {last_name}"
#
# print(get_fullname("Petro", "Ivanovich", "Zaliznyak"))

#
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         total = (length - len(string)) // 2
#         spaces = " " * total
#         return f'{spaces}{string}'
#
# print(format_string('abaa', 15))


def first(size, *arg):
    print(len(*arg))


print(first(5, "first", "second", "third"))

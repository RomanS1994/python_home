# from typing import Callable

# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)

# # Використання
# result_add = apply_operation(5, 3, add)
# result_multiply = apply_operation(5, 3, multiply)

# print(result_add, result_multiply)


# -------------------------
# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b

# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)


# -------------------------
# def apply_discount(price: float, discount_percentage: int) -> float:
#     return price * ( discount_percentage / 100)

# # Використання
# discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
# print(discounted_price)

# discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
# print(discounted_price)


# -------------------------
# def complicated(x: int, y: int) -> int:
#     return x + y

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# xs = logger(complicated)
# print(xs(2, 3))


# -------------------------
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = [i ** 2 for i in numbers]
print(sq)
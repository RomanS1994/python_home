from time import time
from functools import wraps
"""
Написати декоратор який буде рахувати час виконання функцій
"""

def timing_decorator(func):
    # def wrapper(*args, **kwargs):
    @wraps(func)
    def wrapper(numbers):
        start_time = time()
        result = func(numbers)
        end_time = time()
        print('Function running time:')
        print((start_time - end_time) * 1000)
        return result
    return wrapper

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@timing_decorator
def count_sum(numbers: list[int]) -> int:
    return sum(numbers)


# start_time = time()
print(count_sum(numbers))
# end_time = time()

# print(start_time - end_time)
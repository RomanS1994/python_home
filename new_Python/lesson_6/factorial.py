''' Написати функцію, яка буде рахувати факторіал'''

def factorial_non_recursive(n: int) -> int:
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial_non_recursive(5))


# Формула рекуксії
#   1) Задати функцію
#   2.1) Написати умову, за якою зупинається наща рекурсія
#   2.2) Якщо умова зупинки не виконується, ми йдемо далі (Рекурсивний крок)
#   3) Якщо дійшли до умови виходу, зупиняємось і повертаємо кінцеве значення


def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
# -------------------------
# Функція як аргумент
def sum(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def division(a: int, b: int) -> int:
    return a // b


def operation(a, b, func):
    return func(a, b)



add = operation(4, 3, sum)
# print(add)


separation = operation(12, 4, division)
# print(separation)


# -------------------------
# Функція як кузультат функції

def sum(a, b):
    return a + b

def division(a, b):
    return a // b


def operation(operator: str):
    match operator:
        case  '+':
            return sum
        case  '//':
            return  division
        case '-':
            return minus

res_func = operation('+') 
# print(res_func(2, 3))
 
 

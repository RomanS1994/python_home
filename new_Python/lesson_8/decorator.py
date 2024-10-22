


def args_logger(func):
    def inner(*args):
        if Debug:
            print(f'I am args logger. Args: {args}')
        result = func(*args)
        return result
    return inner

def result_logger(func):
     
    def inner(*args):
        result = func(*args)
        if Debug:
            print(f'I am args logger. Result: {result}')
        return result
    return inner

@result_logger
@args_logger
def calc(x, y):
    result = x + y
    return result


Debug = True





# ==============================================================
# Практика декоратори
# ==============================================================

#1. Декоратор для виводу аргументів
def print_args(func):
    def inner(*args):
        # print(f'this is your arguments {args}')
        return func(*args)
    return inner

@print_args
def calc(x, y):
    res = x + y
    return res

sum = calc(4, 5)
# print(sum)



#2. Декоратор для затримки виконання 



from time import sleep

seconds = 5

def delay(seconds):
    def decorator(func):
        def wrapper(*args):
            sleep(seconds)
            return func(*args)
        return wrapper
    return decorator



@delay(seconds)
def greeting(name):
    return f"Hello {name}"




output = greeting('Roman')
print(output)



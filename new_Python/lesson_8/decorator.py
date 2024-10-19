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

if __name__ == '__main__':
    print(calc(5, 8))
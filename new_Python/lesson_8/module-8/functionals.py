import math


def get_length(d):
    result = d * math.pi
    return result


get_lambda_length = lambda d: d * math.pi


if __name__ == '__main__':
    length_1 = get_length(10)
    length_2 = get_lambda_length(10)

    # print(length_1, length_2, sep="\n")
# ==============================================================
# lambda functions
# ==============================================================

# -------------------------
# Проста лямбда функція


add = lambda x, y: x + y

# print(add(2, 3))

# -------------------------
# Використання з мап
#Основна мета використання map — це автоматизувати процес перебору елементів у ітерованому об'єкті

lst = [i for i in range(10)]
# print(lst)

arr = []
res = tuple(map(lambda x: x ** 2, lst))
# print(res)


people = [("John", 25), ("Alice", 30), ("Bob", 20)]
sorted_people = sorted(people, key=lambda a: -a[1])

print(sorted_people)
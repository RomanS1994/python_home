# fruit_list = ["mango", "apple", "apple", "pear", "banana", "pomegranate"]


# print(set(fruit_list))

# print('hello world')


my_set = {1, 2, 3, 4}

# ==============================================================
# Додавання і видалення елементів
# ==============================================================

# add and remove elements
# my_set.add(2.5) - # adds elements
# my_set.discard(3) - remove elements without error

# my_set.remove(54) #- remove elenement with error
# print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# -------------------------
# обєднання
union_set = set1 | set2
# print(union_set)


# -------------------------
# перетин &
intersection = set1 & set2
# print(intersection)


# -------------------------

sym_dyf_set = set1 ^ set2
# print(sym_dyf_set)

my_list = list(union_set)
# print(my_list)


# print(2 is set1)

a = 2
b = [2]

print(a in b)

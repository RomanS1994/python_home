import random

# AK 2023 HI

# 0-9, ['A', 'B', 'C', 'D', 'E']

def generate_plate_number():
    set_of_letters = ['A', 'B', 'C', 'D', 'E']
    set_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    l1 = random.choices(set_of_letters, k=2)
    l2 = random.choices(set_of_numbers, k=4)
    l3 = random.choices(set_of_letters,k=2)
    return "".join(l1+[" "])
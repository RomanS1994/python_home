my_dict = {
    "name": "Roman",
    "age": 30,
    "country": "USA"
}

my_dict["age"] = 31
my_dict['car'] = 'BMW'

# print(my_dict["car"] == 'BMW')
# print(my_dict)


# ==============================================================
# task1 Підрахунок кількості слів у реченні 

test_string = "hello, hello hello Roman, hov are you"
print

def word_count(s):
    count = 1
    lst = {}

    for world in s.split():
        if world not in lst:
            lst[world] = count
        else:
            lst[world] = count + 1
            
   
    return lst

print(word_count(test_string))

# ==============================================================
# task2 Перевертання словника
# Дано словник, де ключами є імена студентів, а значеннями — їх оцінки. Переверни цей словник так, щоб ключами стали оцінки, а значеннями — списки студентів з відповідними оцінками.

students_grades = {'Олена': 90, 'Іван': 85, 'Марія': 92, 'Андрій': 90}
# Вихід:
{90: ['Олена', 'Андрій'], 85: ['Іван'], 92: ['Марія']}
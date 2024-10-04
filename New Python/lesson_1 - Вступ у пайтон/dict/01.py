my_dict = {"name": "Roman", "age": 30, "country": "USA"}

my_dict["age"] = 31
my_dict["car"] = "BMW"

# print(my_dict["car"] == 'BMW')
# print(my_dict)


# ==============================================================
# task1 Підрахунок кількості слів у реченні

test_string = "hello, hello hello Roman, hov are you"
print


def word_count(s):
    count = 1
    lst = {}

    for word in s.split():
        if word not in lst:
            lst[word] = count
        else:
            lst[word] = count + 1

    return lst


# print(word_count(test_string))

# ==============================================================
# task2 Перевертання словника
# Дано словник, де ключами є імена студентів, а значеннями — їх оцінки. Переверни цей словник так, щоб ключами стали оцінки, а значеннями — списки студентів з відповідними оцінками.

students_grades = {"Олена": 90, "Іван": 85, "Марія": 92, "Андрій": 90}
# Вихід:
{90: ["Олена", "Андрій"], 85: ["Іван"], 92: ["Марія"]}


def revers_gict(obj: dict) -> dict:
    new_obj = {}
    for student, grade in obj.items():
        if grade not in new_obj:
            new_obj[grade] = []
        new_obj[grade].append(student)

    return new_obj


print(revers_gict(students_grades))

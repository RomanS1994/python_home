from datetime import datetime

''' написати функцію, яка буде рахувати вік людини'''

def calculate_persons_age(birthday_date: datetime) -> int:
    '''A function to calculate person age'''
    today = datetime.now().date()

    age = today.year - birthday_date.year
    
    if ((today.month, today.day) < (birthday_date.month, birthday_date.day)):
        age += 1

    
    return age

print(datetime.today)

person_one_birthday = datetime(2000, 1, 1) # age = 24
person_two_birthday = datetime(2000, 9, 5) # age = 0
person_three_birthday = datetime(2000, 10, 4) # age = 1
person_four_birthday = datetime(2000, 11, 4) # age = 0
person_five_birthday = datetime(2000, 10, 10) # age = 0


print(calculate_persons_age(person_one_birthday))
print(calculate_persons_age(person_two_birthday))
print(calculate_persons_age(person_three_birthday))
print(calculate_persons_age(person_four_birthday))
print(calculate_persons_age(person_five_birthday))
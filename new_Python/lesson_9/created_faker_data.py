from faker import Faker
from pathlib import Path
import json

def created_faker_data(value):
    fake = Faker()
    contacts = []
    for el in range(value):
        obj = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address()
        }
        contacts.append(obj)
    return contacts

count = 5
res = created_faker_data(count)

def markup(lst):
    # Використаємо абсолютний шлях до файлу
    path = Path('./lesson_9/data.json').resolve()  # Змінив на .json для більш зрозумілого збереження
    print(f"Saving data to: {path}")  # Перевірка шляху
    with open(path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(lst, indent=4))  # Зберігаємо дані у вигляді JSON

markup(res)
 
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0  # Ініціалізація атрибута count_save

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)  # Зберігаємо об'єкт в файл

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)  # Завантажуємо об'єкт з файлу
        return content

    def __getstate__(self):
        state = self.__dict__.copy()  # Копіюємо всі атрибути
        state['count_save'] += 1  # Збільшуємо count_save тільки в копії
        return state 
        
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]

persons = Contacts("user_class.dat", contacts)
print(persons.filename)

persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
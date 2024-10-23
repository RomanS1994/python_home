class User:
    name = None
    age = None
    phone = None

    def greating(self):
        return f'I am {self.name} my self {self}'
    

user_1 = User()
user_1.name = 'Vlad'
user_1.age = 32
user_1.phone = '09343243'

print(user_1.name, user_1.age, user_1.phone)
print(user_1.greating())
print(user_1)
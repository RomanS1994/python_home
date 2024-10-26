class User:
    def __init__(self, name, lst_name=None) -> None:
        self.name = None
        self.last_name= None


    def __str__(self):
        return f"Fullname: {self.name} {self.last_name}"
    
    def __repr__(self):
        return f"Fullname: {self.name} {self.last_name}"

user_1 = User('Boris', 'Jonson')
print(user_1.name, user_1.last_name)

users = []
users.append(user_1)
print(users)
##### ----------- Тема 4. Регулярні вирази та розширена робота з рядками
# test1 = 'Roman'
# test2 = "Strizhko"

# print("roman\nstrizhko")

# print("roman\tstrizhko")

# print("Hello roman\bstrizhko")



##### -------- Методи рядків

### find()
# str = "Hello World"
#
# print(str.find("lo", 1, 8))


##### ------- Поділ та об'єднання рядків
## --- Поділ
# text = "apple, banana, cherry"
# result = text.split()
# print(result)

## --- об'єднання

# list = ["hello", "world"]
# result = ', hi '.join(list)
# print(result)

# str = "Hello @ World"
# test,_ = str.split("@")
# print(test)

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)
#
# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)


##### ------ Форматува

# for num in range(6):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')


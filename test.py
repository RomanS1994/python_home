

# a = 3 
# b = a
# print(a)
# a = 4 
# print(a)
# print(b)


# x = 1 
# x += 4
# print(x)

######## Модуль 2 ######

#### №1
# name = input("What is your name? ")
# print(f"Hello {name}!!!")


#### №2

# age = input("How old are you? ")
# if int(age) >= 18:
#     print(111)
# else: 
#     print(222)

#### №3

# a = int(input("Введіть число"))
# if a == 1:
#     print(1)
# elif a == 2:
#     print(2)
# elif a == 3:
#     print(3)
# elif a == 4:
#     print(4)
# else:
#     print("number")

### №4

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#      print("X can`t be equal to zero")
#      x = int(input("X: "))

#     if x == 0:
#         print("X can`t be equal to zero")
#         x = int(input("X: "))

#         if x == 0:
#             print("X can`t be equal to zero")
#             x = int(input("X: "))

# result = y / x

### №4 for in
# a = 'Apple'
# for b in a:
#     print(b)

### №5 while 

# a = 1
# while a < 5:
#     print(a)
#     a += 1
#############################

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break

#-------------------------------
# while
# counter = 1
# while counter <= 5:
#     a = int(input("value "))
#     print(a)
#     counter += 1
#     if counter == 6:
#         print("Finish")
    
#--------------------------------
# try_except
# while True:
#     age = int(input("How old are you? "))
#     try:
#         if age >= 18:
#             print("Access allowed")
#             break
#         else:
#             print("access denied")
#             break
#     except:
#         print(f"{age} isn't a number... please write number ")
#     finally:
#         print('_'*100)
#--------------------------------

# num = int(input("Enter integer (0 for output): "))
# sum = 0

# while num != 0:
#     for i in range(num):
#         sum += i  # Виправлено синтаксичну помилку



#--------------------------------

# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     pos = ord(f"{ch}") + offset
#     print(pos)
#     encoded_message += chr(pos)   
#     print(encoded_message)
        
        
#--------------------------------

# result = None
# operand = None
# operator = None
# wait_for_number = True

# while True:
    


#Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
#Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0
#--------------------------------
"""
def total(a=5, *numbers, **phone_book):
    print('a', a)
    # прохід по всіх елементах кортежу
    for single_item in numbers:
        print('single_item', single_item)

    #прохід по всіх елементах словника
    for first_part, second_part in phone_book.items():
        print(first_part,second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
"""
#--------- Кортеджі -----------------------
# a = (1,2,3)
# print(a)
# print(a[1])

# b = ("Roman", "Dima")
# print(b)
# print(b[1])

#-------------- Калькулятор ------------------

# result = 0
# operand = None
# operator = None
# wait_for_number = True

# while True:
#     response = input(">>> ")
#     try:
#         if wait_for_number:
#             parts = response.split(".")
#             erg_msg = f"{response} not a number: Try again"

#             if len(parts) > 2:
#                 raise ValueError(erg_msg)
#             for part in parts:
#                 if not part.replace("-", "").isnumeric():
#                     raise ValueError(erg_msg)

#             if len(parts) == 1:
#                 operand = int(response)
#             else:
#                 operand = float(response)

#             if operator is None or operator == "+":
#                 result += operand
#             elif operator == "-":
#                 result -= operand
#             elif operator == "*":
#                 result *= operand
#             elif operator == "/":
#                 if operand == 0:
#                     raise ValueError("Division by zero is not allowed.")
#                 result /= operand
#         else: 
#             if response == "=":
#                 print(f"Result: {result}")
#                 break

#             if response not in ["+", "-", "*", "/"]:
#                 raise ValueError(f"{response} is not +, -, *, /, Try again")
#             operator = response
#         wait_for_number = not wait_for_number
#     except ValueError as e:
#         print(e)


# Тестові послідовності:

# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
# Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0


#----------- Modul 4 ---------------------

# a = 4


# def first_fun():
  
#     b = 3
#     # print(a)
#     def second_fun():
#         nonlocal b
#         b += a
#         print(b)
#     second_fun()
# first_fun()

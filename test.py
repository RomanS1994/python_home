

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
        
        
    
        
        
        
        
    
        
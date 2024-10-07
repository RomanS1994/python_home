fh = open('test.txt', 'w')
symbols_written = fh.write('hello !')
# print(symbols_written)
fh.close()

fh = open('test.txt', mode = "r")
# print(fh.read(8))
# fh.close()
# print(fh.read())


fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
# print(lines)

fh.close()
str = " Hello Roman \n".strip()

# print(str)


# ==============================================================
# 
# ==============================================================
'''
encode() з байт рядків
bytearray(b " ") в байт рядки
decode()
'''

# -------------------------
# байт рядки

s = b'Hello!'
# print(s[0])  # Виведе: 101 (це ASCII-код символу 'e')


byte_str = 'some text'.encode()
# print(byte_str)

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")
print('straße'.casefold())
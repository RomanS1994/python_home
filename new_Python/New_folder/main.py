from pathlib import Path

file_name = Path('./lesson_6/text.txt')
file_name.touch()


with open(file_name, 'w') as file:
    file.write('Hello world ghbdsn hjvfy')
   
with open(file_name, 'r') as file:
    print(file.read())

# try:
#     file_name.unlink()
# except FileNotFoundError:
#     pass    
# print(file_name.exists())  # Виведе True, якщо файл існує

# with open(file_name, 'r') as file:
#     print(file.read())

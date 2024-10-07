from pathlib import Path

file_name = Path('./lesson_6/test.txt')
print(file_name.exists())  # Виведе True, якщо файл існує

with open(file_name, 'r') as file:
    print(file.read())

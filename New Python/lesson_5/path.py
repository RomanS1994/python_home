from pathlib import Path


file_name = Path('./lesson_6/test.txt')


with open(file_name, 'r', encoding='utf-8') as file:
    print(file.read())
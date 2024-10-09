from pathlib import Path 

new_file = Path('./lesson_5/write_text.py')
new_file_1 = Path('./lesson_5/archiv.py')
# new_file_1.touch()
# new_file.touch()

text = ["first line", "second line", "third line"]

with open(new_file, "r+", encoding='utf-8') as file:
    for line in text:
        file.write(line + '\n')
    
    file.seek(0)
    print(file.read())


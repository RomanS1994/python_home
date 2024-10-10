import random
import pathlib

# Поточна директорія файлу jokes_handler.py
current_dir = pathlib.Path(__file__).parent

def get_random_joke():
    try:
        with open(current_dir / "joke.txt", 'r', encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."

from collections import Counter
# Person = collections.namedtuple('person',['first_name', 'last_name'])

# person = Person('Roman', 'Strizhko')

# print(person.first_name)



# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]

# mark_counts = collections.Counter(student_marks)
# print(mark_counts)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")


# -------------------------
# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)

# -------------------------
# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue))

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)

# # Size: Розмір черги
# print("Розмір черги:", len(queue))

# -------------------------

# from collections import deque

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' в кінець черги
# d.append('last')    # Додаємо 'last' в кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))


# -------------------------
from collections import deque

# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

# Ініціалізація черги завдань
task_queue = deque()

# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")

# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")

from collections import namedtuple



person_1 = ('Bob', 30, 'Kyiv')

print(f'Simple tuple: Name {person_1[0]} Age {person_1[1]} City {person_1[2]} ')


Person = namedtuple('Person', ['name', 'age', 'city'])

person_2 = Person('Nike', 40, 'Lviv')
person_3 = Person('Olena', 18, 'Odesa')

print(f'Named Tuple: Name {person_2.name} Age {person_2.age} City {person_2.city}')
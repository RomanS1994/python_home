from dataclasses import dataclass

'''
Напишіть систему яка буде керувати автоматом для їжі
'''

'''
{
"Snickers": Product(10, 'Snickers', 100)
"Snickers": Product(10, 'Coca Cola', 150)
}
'''

@dataclass
class Product:
    price: int
    name: str
    calories: int

class Machine:
    
    def __init__(self, products_dict: dict, starting_money: int):
        self.products_dict = products_dict
        self.money = starting_money


    def add_product(self, product: Product):
        if product.price > 100:
            raise ValueError
        self.products_dict[product.name] = product

    def __str__(self):
        return f'Machine products_dict={self.products_dict}, money = {self.money} '

product_one = Product(100, 'My product', 300)
product_two = Product(100, 'My product', 300)

machine = Machine((dict(), 0))
machine.add_product(product_one)

print(product_one, product_two)
print(machine)
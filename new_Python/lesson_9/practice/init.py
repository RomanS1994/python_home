class Item:
    pay_rate = 0.8 # сума після знижки в 20%
    all_class_instance = list()

    def __init__(self, name: str, price: float, quantity = 0 ):
        self.name = name
        self.price = price
        self.quantity = quantity 


        Item.all_class_instance.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate

    def info(self):
        return f'Item (name:{self.name}, price:{self.price}, quantity:{self.quantity})'



item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 5)


print(item1.price)
print(item2.price)
print(item2.apply_discount())  
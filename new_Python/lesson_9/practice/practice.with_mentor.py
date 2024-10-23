class Item:
    def calculate(self, x, y):
        return x + y


sums = Item()

print(sums.calculate(2, 3))
sums.x = 2
sums.y = 4
print(sums.__dict__)
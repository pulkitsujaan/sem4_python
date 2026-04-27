class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        print(f"Added: {product.name}")

    def remove(self, name):
        self.items = [p for p in self.items if p.name != name]
        print(f"Removed: {name}")

    def total(self):
        return sum(p.price for p in self.items)

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

u = User("Alice")
u.cart.add(Product("Book", 299))
u.cart.add(Product("Pen", 50))
u.cart.remove("Pen")
print("Total: Rs.", u.cart.total())
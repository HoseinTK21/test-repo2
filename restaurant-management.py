class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"the {self.name} price is {self.price}"
class Order:
    def __init__(self):
        self.item = []
        total_order.add_order(self)
    def add_item(self, food: Food, quantity):
        self.item.append((food, quantity))

    def total_price(self):
        result = 0
        for food, q in self.item:
            result += food.price * q
        return result

    def __str__(self):
        lines = []
        for food, q in self.item:
            lines.append(f"you ordered a {food.name} for {q} count and total price is {food.price * q}$")
        lines.append(f"--- Total = {self.total_price()}$ ---")
        return "\n".join(lines)

class total_order:
    all_orders = []
    @classmethod
    def add_order(cls,  order: Order):
        cls.all_orders.append(order)
    @classmethod
    def sum_all_orders(cls):
        result = 0
        for order in cls.all_orders:
            result += order.total_price()
        return result
    @classmethod
    def max_order(cls):
        if not cls.all_orders:
            return "your orders are empty"
        return max(order.total_price() for order in cls.all_orders)
    
        
    
food1 = Food("Pizza", 12)
food2 = Food("Burger", 9)
food3 = Food("Pasta", 6)
order1 = Order()
order1.add_item(food1, 2)
order1.add_item(food2, 6)
order2 = Order()
order2.add_item(food1, 120)
order3 = Order()
order3.add_item(food2, 24)

total = total_order()

print(total.sum_all_orders())
print(f"this is your shops maximum order price: {total.max_order()}")




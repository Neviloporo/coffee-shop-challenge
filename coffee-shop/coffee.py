from order import Order  

class Coffee:
    def __init__(self, name):
        self._set_name(name)  

    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value  

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]  

    def customers(self):
        return list({order.customer for order in self.orders()}) 

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0  

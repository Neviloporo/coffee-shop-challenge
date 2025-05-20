class Customer:
    def __init__(self, name):
        self.name = name

class Coffee:
    def __init__(self, type):
        self.type = type

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self._set_price(price)
        self.customer = customer
        self.coffee = coffee
        Order.all.append(self)

    def _set_price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        self._coffee = value

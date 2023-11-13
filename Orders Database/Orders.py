from Order import *


class Orders:

    # constructor
    def __init__(self):
        self.orders = {}

    # add order to dictionary; do not add if ono already exists.
    def add_order(self, o):
        if o.ono not in self.orders:
            self.orders[o.ono] = o


    # return Order object for ono; return None if no Order with ono
    def get_order(self, ono):
        if ono in self.orders:
            return self.orders[ono]
        return None

    # delete order with order number ono; return True
    # if ono not in dictionary do nothing and return False
    def delete_order(self, ono):
        if ono in self.orders:
            del self.orders[ono]
            return True
        return False

    # return a list of order numbers for orders placed by customer number cno
    def get_orders_for_customer(self, cno):
        customer_orders = [ono for ono, order in self.orders.items() if order.placed_by == cno]
        return customer_orders

    # return a list of all order numbers
    def get_onos(self):
        return list(self.orders.keys())

    # return string representation of Orders object
    def __str__(self):
        orders_str = "Orders:\n"
        for ono, order in self.orders.items():
            orders_str += f"{str(order)}\n"
        return orders_str

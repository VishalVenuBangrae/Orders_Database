class Order:

    # constructor
    def __init__(self, ono, cust, d):
        self.ono = ono
        self.placed_by = cust
        self.order_date = d
        self.items = []

    # add item (triple made up of part, quantity, and discount) to self.items
    def add_item(self, item):
        self.items.append(item)

    # getters
    def get_ono(self):
        return self.ono

    def get_placed_by(self):
        return self.placed_by

    def get_order_date(self):
        return self.order_date

    def get_items(self):
        return self.items

    # setters
    def set_ono(self, ono):
        self.ono = ono

    def set_placed_by(self, cust):
        self.placed_by = cust

    def set_order_date(self, d):
        self.order_date = d

    def set_items(self, items):
        self.items = items

    # update discount value for a give part number pno in order to discount; return True
    # do nothing if pno is not in items; return False
    def update_discount(self, pno, discount):
        for item in self.items:
            if item[0] == pno:
                item[2] = discount
                return True
        return False

    # delete part with part number pno from items and return True;
    # do nothing if pno is not in items; return False
    def delete_part(self, pno):
        for item in self.items:
            if item[0] == pno:
                self.items.remove(item)
                return True
        return False
    # return True if order contains no parts; False otherwise

    def empty_order(self):
        return not bool(self.items)

    # return string representation of the order (see output for format!)
    def __str__(self):
        order_str = f"ono: {self.ono}\nplaced_by: {self.placed_by}\norder_date: {self.order_date}\n"
        return order_str


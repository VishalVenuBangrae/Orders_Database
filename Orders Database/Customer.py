class Customer:

    # constructor
    def __init__(self, cnum, name, cty):
        self.cno = cnum
        self.cname = name
        self.city = cty

    # getter
    def get_cno(self):
        return self.cno

    # getter
    def get_cname(self):
        return self.cname

    # getter
    def get_city(self):
        return self.city

    # setter
    def set_cno(self, cnum):
        self.cno = cnum

    # setter
    def set_cname(self, name):
        self.cname = name

    # setter
    def set_city(self, cty):
        self.city = cty

    # return string representation of Customer object
    def __str__(self):
        return f"cno: {self.cno}\ncname: {self.cname}\ncity: {self.city}"

customer1 = Customer(12345, "Vishal", "Atlanta")
customer2 = Customer(2222, "Alice", "New York")

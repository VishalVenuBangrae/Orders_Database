from Customer import *


class Customers:

    # constructor
    def __init__(self):
        self.customers = {}

    # add Customer object c to dictionary; do not add if customer number already present
    def add_customer(self, cno, c):
        if cno not in self.customers:
            self.customers[cno] = c

    # return Customer object corresponding to cno; return None if no customer with cno
    def get_customer(self, cno):
        return self.customers[cno]

    # return a list of all customer numbers
    def get_cnos(self):
        list1 = []
        for i in self.customers:
            list1.append(i)
        return list1

    def __str__(self):
        return f"\n".join([f"{cno}:\n{customer}\n" for cno, customer in self.customers.items()])

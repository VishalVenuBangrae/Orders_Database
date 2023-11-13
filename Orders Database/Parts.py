from Part import *


class Parts():

    # constructor
    def __init__(self):
        self.parts = {}

    # add Part object p to dictionary; do not add if part number already exists
    def add_part(self, pno, p):
        if pno not in self.parts:
            self.parts[pno] = p

    # return Part object for pno; return None if no part with pno
    def get_part(self, pno):
        if pno in self.parts:
            return self.parts[pno]
        return False

    # return a list of all part numbers
    def get_pnos(self):
        list1 = []
        for i in self.parts:
            list1.append(i)
        return list1

    # return string representation of Parts object
    def __str__(self):
        return "\n".join([f"Part {pno}:\n{part}\n" for pno, part in self.parts.items()])




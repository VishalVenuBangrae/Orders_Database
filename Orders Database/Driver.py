import os
import sys

from Customer import *
from Customers import *
from Part import *
from Parts import *
from Order import *
from Orders import *


# Open three files, customer.dat, part.dat, and order.dat,
# present in directory dname.
# Read the data and construct the customers, parts, and orders objects
# Return the three objects as a tuple (see main() for the order)


def load_data(dname):
    customers = Customers()
    parts = Parts()
    orders = Orders()

    # load customers data
    with open(os.path.join(dname, "customer.dat")) as f_c:
        data_customer = f_c.read().splitlines()
        for data in data_customer:
            split_data = data.split(":")
            cno = int(split_data[0])
            cname = str(split_data[1])
            city = str(split_data[2])
            customer = Customer(cno, cname, city)
            customers.add_customer(cno, customer)

    with open(os.path.join(dname, "part.dat")) as f_p:
        data_parts = f_p.read().splitlines()
        for data in data_parts:
            split_parts_data = data.split(":")
            pno = split_parts_data[0]
            pname = split_parts_data[1]
            price = split_parts_data[2]
            part = Part(pno, pname, price)
            parts.add_part(pno, part)

    with open(os.path.join(dname, "order.dat")) as f_o:
        data_parts = f_o.read().splitlines()

        for data in data_parts:
            split_order_data = data.split(":")
            ono = str(split_order_data[0])
            placed_by = int(split_order_data[1])
            order_date = str(split_order_data[2])
            list_to_itv = split_order_data[3:]
            order = Order(ono, placed_by, order_date)
            for i in list_to_itv:
                split_new_data = i.split(",")
                part, quantity, discount = split_new_data
                triplet = [int(part), int(quantity), int(discount)]
                order.add_item(triplet)
            orders.add_order(order)
    return customers, parts, orders


# Store data from customers, parts, and orders objects into three files,
# customer.dat, part.dat, and order.dat in the folder named dname;
# Use same format as when you loaded the data
def store_data(customers, parts, orders, dname):
    # store customers data
    with open(os.path.join(dname, "customer.dat"), 'w') as f_c:
        for cno in customers.get_cnos():
            customer = customers.get_customer(cno)
            f_c.write(f"{customer.cno}:{customer.cname}:{customer.city}\n")

    # Store orders data
    with open(os.path.join(dname, "order.dat"), 'w') as f_o:
        for ono in orders.get_onos():
            order = orders.get_order(ono)
            items_str = ":".join([f"{item[0]},{item[1]},{item[2]}" for item in order.items])
            f_o.write(f"{order.ono}:{order.placed_by}:{order.order_date}:{items_str}\n")

    # Store parts data
    with open(os.path.join(dname, "part.dat"), 'w') as f_p:
        for pno in parts.get_pnos():
            part_obj = parts.get_part(pno)
            f_p.write(f"{part_obj.pno}:{part_obj.pname}:{part_obj.price}\n")


def main():
    customers, parts, orders = load_data(sys.argv[1])
    print("\nWelcome to Orders Database Program\n")
    while True:
        command = input("c, c cno, o ono, u ono pno discount, d ono pno, q: ").strip()
        if len(command) < 1:
            print("\nInvalid command!\n")
            continue
        elif command[0] == 'c' and len(command) == 1:
            print()
            print(customers)
        elif command[0] == 'c' and len(command) > 1:
            cno = int(command[1:].strip())
            c = customers.get_customer(cno)
            if c == None:
                print("\nInvalid Customer Number", cno, "\n")
                continue
            else:
                print()
                print(c)
                onos = orders.get_orders_for_customer(cno)
                print("ORDERS: ", end="")
                for ono in onos:
                    print(ono, " ", end="")
                print("\n")
        elif command[0] == 'o':
            ono = command[2:].strip().upper()
            o = orders.get_order(ono)
            if o is not None:
                print()
                print(o)
                print("\nOrder date:", o.order_date)
                print(f"{'PNO':<5}{'PNAME':<20}{'PRICE':<10}{'QTY':<5}{'%DISCOUNT':<10}{'COST':<10}")
                total_cost = 0
                for item in o.items:
                    pno, qty, discount = item
                    part = parts.get_part(str(pno))
                    new_str = part.__str__()
                    split_new_string = new_str.strip().split()
                    pname = split_new_string[3]
                    price = float(split_new_string[5])
                    cost = (price * qty) * (1 - discount / 100)
                    total_cost += cost
                    print(f"{pno:<5}{pname:<20}{price:<10.2f}{qty:<5}{discount:<10}{cost:<10.2f}")
                print(f"TOTAL{'':<28}{total_cost:.2f}\n")
            else:
                print("\n" + ono + " NOT FOUND\n")
        elif command[0] == 'u':
            ono, pno, discount = command[2:].split()
            pno = int(pno)
            discount = int(discount)
            o = orders.get_order(ono)
            if o != None:
                print()
                if o.update_discount(pno, discount):
                    print("Discount updated!\n")
                else:
                    print("No such part in order!\n")
            else:
                print("\n" + ono + " NOT FOUND\n")
        elif command[0] == 'd':
            ono, pno = command[2:].split()
            pno = int(pno)
            o = orders.get_order(ono)
            if o != None:
                print()
                if o.delete_part(pno):
                    print("Part deleted from order!\n")
                    if o.empty_order():
                        if orders.delete_order(o):
                            print("Empty order deleted!")
                        else:
                            print("Something went wrong!")
                else:
                    print("No such part in order!\n")
            else:
                print("\n" + ono + " NOT FOUND\n")
        elif command[0] == 'q':
            print("\nBye!\n")
            break
        else:
            print("\nInvalid command\n")
    store_data(customers, parts, orders, sys.argv[1])


main()

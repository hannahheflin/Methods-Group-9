import csv


customers = []


class Customer:
    def __init__(self):
        self.username = None
        self.password = None
        self.first_name = None
        self.last_name = None
        self.shippingAddress = None
        self.cardNumber = None

    def create_account(self, name, password, first, last, add, num):
        self.username = name
        self.password = password
        self.first_name = first
        self.last_name = last
        self.shippingAddress = add
        self.cardNumber = num
        with open("customer.csv", "a", newline='') as file:
            writer = csv.writer(file)
            row = [self.username, self.password, self.first_name, self.last_name, self.shippingAddress,
                   self.cardNumber]
            writer.writerow(row)

    def edit_add(self, address):
        self.shippingAddress = address

    def edit_card(self, card):
        self.cardNumber = card


def user_exists(username):
    for x in customers:
        if username == x.username:
            return False
    return True


def process_customer():
    with open("customer.csv") as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            username = row[0]
            password = row[1]
            fn = row[2]
            ln = row[3]
            add = row[4]
            card = row[5]
            newcustomer = Customer()
            newcustomer.create_account(username, password, fn, ln, add, card)
            customers.append(newcustomer)


def login(username, password):
    usernames = []
    for x in customers:
        usernames.append(x.username)
    try:
        index = usernames.index(username)
    except:
        return False, 0
    if username in usernames:
        temp = customers[index]
        if temp.password == password:
            return True, index


def rewrite_customer():
    with open("customer.csv", "w", newline='') as outfile:
        rows = []
        for x in customers:
            row = [x.username, x.password, x.firstName, x.lastName, x.shippingAddress,
                   x.cardNumber]
            rows.append(row)
        writer = csv.writer(outfile)
        writer.writerows(rows)


def delete_account(customer):
    for x in customers:
        if x is customer:
            customers.remove(x)
    rewrite_customer()

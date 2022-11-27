import csv


customers = []


class Customer:
    def __init__(self, name=None, password=None, first=None, last=None, add=None, num=None):
        self.username = name
        self.password = password
        self.first_name = first
        self.last_name = last
        self.shippingAddress = add
        self.cardNumber = num

    def create_account(self):
        with open("customers.csv", "a", newline='') as file:
            writer = csv.writer(file)
            row = [self.username, self.password, self.first_name, self.last_name, self.shippingAddress,
                   self.cardNumber]
            writer.writerow(row)
        customers.append(self)

    def edit_add(self, address):
        self.shippingAddress = address

    def edit_card(self, card):
        self.cardNumber = card


def process_customer():
    with open("customers.csv") as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            username = row[0]
            password = row[1]
            fn = row[2]
            ln = row[3]
            add = row[4]
            card = row[5]
            newcustomer = Customer(username, password, fn, ln, add, card)
            customers.append(newcustomer)


def login(username, password):
    usernames = []
    for x in customers:
        usernames.append(x.username)
    try:
        index = usernames.index(username)
    except:
        return False, "user"
    if username in usernames:
        temp = customers[index]
        if temp.password == password:
            return True, "Success"
        else:
            return False, "pass"


def rewrite_customer():
    with open("customers.csv", "w", newline='') as outfile:
        rows = []
        for x in customers:
            row = [x.username, x.password, x.first_name, x.last_name, x.shippingAddress,
                   x.cardNumber]
            rows.append(row)
        writer = csv.writer(outfile)
        writer.writerows(rows)


def delete_account(customer):
    for x in customers:
        if x is customer:
            customers.remove(x)
    rewrite_customer()


def user_exists(username):
    for x in customers:
        if username == x.username:
            return False
    return True

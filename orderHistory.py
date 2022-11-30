import csv
import pandas
from ShoppingCart import *


class OrderHistory:

    def __init__(self, username):
        self.username = username.strip()
        self.productID = None
        self.quantity = 0
        self.total = 0
        self.cardInfo = 0

    def getQuant(self):
        data = []
        with open('cart.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

            col = [x[0] for x in data]
            if self.username in col:
                for x in range(0, len(data)):
                    if self.username == data[x][0]:
                        # print the card number
                        # print("Quanitiy of Item:{}".format (data[x][2]))
                        return data[x][2]
            else:
                print("User not found")

    def getPID(self):
        data = []
        with open('cart.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

            col = [x[0] for x in data]
            if self.username in col:
                for x in range(0, len(data)):
                    if self.username == data[x][0]:
                        # print("Product ID:{}".format (data[x][1]))
                        # returns the product id
                        return data[x][1]
            else:
                print("User not found")

    def getCardInfo(self):
        data = []
        with open('customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

            col = [x[0] for x in data]
            if self.username in col:
                for x in range(0, len(data)):
                    if self.usernname == data[x][0]:
                        # print the card number
                        # print("Card Used:{}".format (data[x][5]))
                        return data[x][5]
            else:
                print("Card Info Not Found")

    def getTotal(self):
        username = self.username
        data1 = []  # cartInfo holds the quantity 
        data2 = []  # furniture info holds the price 
        # these are connected by ProductID
        with open('cart.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data1.append(row)

            with open('furniture.csv') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    data2.append(row)

            furnitureID = int(getPID(username))
            print('Product id:{} '.format(furnitureID))

        total = 0
        col = [x[0] for x in data2]
        if furnitureID in col:
            print('item found')
            for x in range(0, len(data2)):
                if furnitureID == data2[x][0]:
                    print('the card number')
                    total = (data2[x][5]) * (data1[x][2])
                    print("Total Price:{}".format(total))
        else:
            print("Total not found")
        return total

    def addHistory(self, quant):

        self.product_ID = self.getPID()
        self.quantity = quant
        #self.total_price = self.getTotal(username)
        self.card_used = self.getCardInfo()

        with open('OrderHistory.csv', mode='w') as csv_file:
            csv_reader = csv.reader(csv_file)
            fieldnames = ['Username', 'ProductID', 'Item Quant', 'Total Price', 'Payment Info']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Username': self.username, 'ProductID': self.product_ID, 'Item Quant': self.quantity,
                             'Total Price': self.total_price, 'Payment Info': self.card_used})

    def displayHistory(self):
        data = []
        with open('orderHistory.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

            col = [x[0] for x in data]
            if self.username in col:
                print('Username:{}'.format(row[0]), '\nProduct ID:{}'.format(row[1]),
                      '\nQuantity:{}'.format(row[2]), '\nCard Used:{}'.format(row[3]))
            else:
                print("No Order History")

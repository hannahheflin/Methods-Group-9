import csv
import pandas

class orderHistory:

    def __init__(self, username):
        self.username = username
        self.productID = None
        self.quantity = 0
        self.total = 0
        self.cardInfo = 0

    def getQuant(self):
        data = []
        with open('Cart.csv') as csv_file:
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
        with open('Cart.csv') as csv_file:
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
                    if self.username == data[x][0]:
                        # print the card number
                        # print("Card Used:{}".format (data[x][5]))
                        return data[x][5]
            else:
                print("Card Info Not Found")

    def getTotal(self):
        price = 0
        quantity = 0
        username = self.username
        data1 = []  # cartInfo holds the quantity
        data2 = []  # furniture info holds the price
        # these are connected by ProductID
        with open('Cart.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data1.append(row)

        col = [x[0] for x in data1]
        if username in col:
            for x in range(0, len(data1)):
                if username == data1[x][0]:
                    furnitureID = data1[x][1]
                    quantity = data1[x][2]

        with open('Furniture.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data2.append(row)
            col = [x[0] for x in data2]
            if furnitureID in col:
                for x in range(0, len(data1)):
                    if furnitureID == data1[x][0]:
                        price = data2[x][4]
                        total = price * quantity

                        return total

    def addHistory(self, quant):

        self.product_ID = self.getPID()
        self.quantity = quant
        self.total_price = self.getTotal()
        self.card_used = self.getCardInfo()

        with open('orderHistory.csv', mode='w') as csv_file:
            csv_reader = csv.reader(csv_file)
            fieldnames = ['Username', 'ProductID', 'Item Quant', 'Payment Info']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Username': self.username, 'ProductID': self.product_ID, 'Item Quant': self.quantity,
                             'Payment Info': self.card_used})

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

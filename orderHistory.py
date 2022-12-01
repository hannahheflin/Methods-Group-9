import csv
import pandas as pd


class orderHistory:
    def __init__(self, username):
        self.username = username
        self.product_ID = None
        self.quantity = None
        self.total_price = None
        self.cardInfo = None

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

    def getTotal(self):
        with open('Furniture.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0].strip() == self.product_ID:
                    return float(row[4]) * float(self.quantity)

    def getCardInfo(self):
        with open('customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0].strip() == self.username:
                    return row[5]

    def addHistory(self, itemID, quant):
        self.product_ID = itemID
        self.quantity = quant
        self.total_price = self.getTotal()
        self.card_used = self.getCardInfo()
        with open('OrderHistory.csv', mode='a', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            fieldnames = ['Username', 'ProductID', 'Item Quant', 'Total Price', 'Payment Info']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Username': self.username, 'ProductID': self.product_ID, 'Item Quant': self.quantity, 'Total Price': self.total_price,
                             'Payment Info': self.card_used})

    def displayHistory(self):
        data = []
        with open('orderHistory.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0].strip() == self.username:
                    with open('Furniture.csv') as furniture:
                        furn_reader = csv.reader(furniture)
                        for row2 in furn_reader:
                            if row2[0].strip() == row[1].strip():
                                print('\nProduct ID:{}'.format(row[1]), '\nProduct Name: {}'.format(row2[1]), '\nCategory: {}'.format(row2[2]),
                                      '\nDesigner: {}'.format(row2[3]), '\nPrice: {}'.format(row2[4]), '\nQuantity:{}'.format(row[2]), '\nTotal Price:{}'.format(row[3]), '\nCard Used:{}'.format(row[4]))

    def clearHistory(self):
        lineNum = 0
        linesFound = []
        with open("orderHistory.csv", "r") as history:
            historyCSV = csv.DictReader(history)
            for line in historyCSV:
                if line["Username"].strip() == self.username:
                    linesFound.append(lineNum)
                lineNum += 1
        if len(linesFound) != 0:
            df = pd.read_csv("orderHistory.csv")
            df = df.drop(linesFound)
            df.to_csv("orderHistory.csv", index=False)


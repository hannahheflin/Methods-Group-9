import csv
import pandas


class OrderHistory:
    def __init__(self, username):
        self.username = username
        self.productID = None
        self.quantity = None
        self.total = None
        self.cardInfo = None

    def getQuant(username):
        data = []
        with open('cart.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
            name = username
            col = [x[0] for x in data]
            if name in col:
                for x in range(0, len(data)):
                    if name == data[x][0]:
                        # print the card number
                        # print("Quanitiy of Item:{}".format (data[x][2]))
                        return data[x][2]
            else:
                print("User not found")

    def getPID(username):
        data = []
        with open('cart.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
            name = username
            col = [x[0] for x in data]
            if name in col:
                for x in range(0, len(data)):
                    if name == data[x][0]:
                        # print("Product ID:{}".format (data[x][1]))
                        # returns the product id
                        return data[x][1]
            else:
                print("User not found")
                
    def getTotal(username):
        data1 = [] #cartInfo
        data2 = [] #furnitureInfo
        with open('furniture.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
            data2.append(row)

        furnitureID = getPID(username)

        total = 0
        col = [x[0] for x in data2]
        if furnitureID in col:
            print('item found')
            for x in range (0, len(data2)):
                if furnitureID == data2[x][0]:
                    print('the card number')
                    total = (data2[x][5]) * (data1[x][2])
                    print("Total Price:{}".format (total))
        else:
        print("Item Not Found")
    return total


    def getCardInfo(username):
        data = []
        with open('customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
            name = username
            col = [x[0] for x in data]
            if name in col:
                for x in range(0, len(data)):
                    if name == data[x][0]:
                        # print the card number
                        # print("Card Used:{}".format (data[x][5]))
                        return data[x][5]
            else:
                print("Card Info Not Found")

    def addHistory(self, username, quantitiy):

        self.username = username
        self.product_ID = self.getPID(username)
        self.quantity = quantity
        #self.total_price = self.getTotal(username)
        self.card_used = self.getCardInfo(username)
        with open('OrderHistory.csv', mode='w') as csv_file:
            csv_reader = csv.reader(csv_file)
            fieldnames = ['Username', 'ProductID', 'Item Quant', 'Total Price', 'Payment Info']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Username': username, 'ProductID': self.product_ID, 'Item Quant': self.quantity,
                             'Total Price': self.total_price, 'Payment Info': self.card_used})

    def displayHistory(username):
        data = []
        with open('orderHistory.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
            name = username
            col = [x[0] for x in data]
            if name in col:
                print('Username:{}'.format(row[0]), '\nProduct ID:{}'.format(row[1]),
                      '\nQuantity:{}'.format(row[2]), '\nCard Used:{}'.format(row[3]))
            else:
                print("No Order History")

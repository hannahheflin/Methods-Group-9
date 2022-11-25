import csv
import pandas as pd
from Furniture import *
from orderHistory import *


class ShoppingCart:

    def __init__(self, user):
        self.__username = user.strip()
        self.__furniture_ID = None
        self.__quantity = 0
        self.furn = Furniture()
        #self.hist = OrderHistory(user)

    def addItem(self, itemID, quant):
        self.__furniture_ID = itemID.strip()
        self.__quantity = quant
        found = 0
        lineNum = 0
        lineFound = 0

        # checks to see if the user has added that item to their shopping cart previously
        with open("Cart.csv", "r") as cart:
            cartCSV = csv.DictReader(cart)

            for line in cartCSV:
                if line["username"].strip() == self.__username and line["productID"].strip() == self.__furniture_ID:
                    self.__quantity += float(line["quantity"])
                    found = 1
                    lineFound = lineNum
                    break

                lineNum += 1

        # makes sure the total quantity for that item does not exceed what's in stock (and that the item actually exist)
        with open("furniture.csv", "r") as furniture:
            furnitureCSV = csv.DictReader(furniture)
            furnitureFound = 0

            for line in furnitureCSV:
                if line["productID"].strip() == self.__furniture_ID:
                    furnitureFound = 1
                    if self.__quantity > float(line["quantity"]):
                        return -1
                    else:
                        break

            if not furnitureFound:
                return -1

        # if the item has previously been added to user's shopping cart, change that item's quantity in the Cart file
        if found:
            df = pd.read_csv("Cart.csv")
            df.loc[lineFound, 'quantity'] = self.__quantity
            df.to_csv("Cart.csv", index=False)

        # if the item has not been previously added, add a new record/entry
        if not found:
            with open("Cart.csv", "a") as cart2:
                cart2.write("%s, %s, %d\n" % (self.__username,
                            self.__furniture_ID, self.__quantity))

        return 0

    def removeItem(self, itemID, quant):
        self.__furniture_ID = itemID.strip()
        self.__quantity = quant
        found = 0
        lineNum = 0
        lineFound = 0

        # attempts to find the given item for the user in the cart file
        with open("Cart.csv", "r") as cart:
            cartCSV = csv.DictReader(cart)

            for line in cartCSV:
                if line["username"].strip() == self.__username and line["productID"].strip() == self.__furniture_ID:
                    self.__quantity = float(line["quantity"]) - self.__quantity
                    found = 1
                    lineFound = lineNum
                    break

                lineNum += 1

        # remove the record/entry or update the quantity accordingly
        if found:
            df = pd.read_csv("Cart.csv")

            if self.__quantity <= 0:
                df = df.drop(lineFound)
            else:
                df.loc[lineFound, 'quantity'] = self.__quantity

            df.to_csv("Cart.csv", index=False)
            return 0

        # return -1 if the item isn't even in user's shopping cart
        if not found:
            return -1

    def displayCart(self):
        print()
        print('{0: <13}'.format("Product ID"), '{0: <15}'.format("Product Name"), '{0: <10}'.format("Category"), '{0: <10}'.format("Designer"), '{0: <10}'.format("Price"), '{0: <10}'.format("Quantity"))
        print('{0: <13}'.format("----------"), '{0: <15}'.format("------------"), '{0: <10}'.format("--------"), '{0: <10}'.format("--------"), '{0: <10}'.format("-----"), '{0: <10}'.format("--------"))
        print()
        
        with open("Cart.csv", "r") as cart:
            cartCSV = csv.DictReader(cart)

            for line in cartCSV:      
                if line["username"].strip() == self.__username:
                    with open("furniture.csv", "r") as furniture:
                        furnitureCSV = csv.DictReader(furniture)

                        for line2 in furnitureCSV:                
                            if line2["productID"].strip() == line["productID"].strip():
                                print('{0: <13}'.format(line2["productID"].strip()), '{0: <15}'.format(line2["productName"].strip()), '{0: <10}'.format(line2["category"].strip(
                                )), '{0: <10}'.format(line2["designer"].strip()), '{0: <10}'.format(line2["price"].strip()), '{0: <10}'.format(line["quantity"].strip()))
                                break       
        print()

    def removeAll(self):
        lineNum = 0
        linesFound = []
        productID = []
        quantity = []

        # finds the matching item in the furniture file for the user and make sure the quantity in the cart does not exceed what's in stock
        with open("Cart.csv", "r") as cart:
            cartCSV = csv.DictReader(cart)

            for line in cartCSV:
                if line["username"].strip() == self.__username:
                    with open("Furniture.csv", "r") as furniture:
                        furnitureCSV = csv.DictReader(furniture)

                        for line2 in furnitureCSV:
                            if line2["productID"].strip() == line["productID"].strip():
                                if float(line2["quantity"]) < float(line["quantity"]):
                                    return -1
                                else:
                                    productID.append(line["productID"].strip())
                                    quantity.append(float(line["quantity"]))
                                    linesFound.append(lineNum)
                lineNum += 1

        # calls the other functions and clears the shopping cart
        if len(linesFound) != 0:
            for i in range(0, len(productID)):
                self.furn.removeItem(productID[i], quantity[i])
                #self.hist.addHistory(productID[i], quantity[i])

            df = pd.read_csv("Cart.csv")
            df = df.drop(linesFound)
            df.to_csv("Cart.csv", index=False)

        return 0

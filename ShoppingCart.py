import csv
import pandas as pd

class ShoppingCart:

    def __init__(self, user):
        self.__username = user
        self.__furniture_ID = None
        self.__quantity = 0

    def addItem(self, itemID, quant):
        self.__furniture_ID = itemID
        self.__quantity = quant 
        found = 0
        lineNum = -1
        lineFound = 0
        
        # checks to see if the user has added that item to their shopping cart previously
        with open("Cart.csv", "r") as cart:
            cartCSV = csv.DictReader(cart)
            
            for line in cartCSV:
                lineNum += 1
                if line["username"].strip() == self.__username.strip() and line["productID"].strip() == self.__furniture_ID.strip():
                    self.__quantity += float(line["quantity"])
                    found = 1
                    lineFound = lineNum

        # makes sure the total quantity for that item does not exceed what's in stock (and that the item actually exist)
        with open("Furniture.csv", "r") as furniture:
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
                cart2.write("%s, %s, %d\n"%(self.__username, self.__furniture_ID, self.__quantity))

        return 0

    def removeItem(self, itemID, quant):
        pass

    def displayCart(self):
        pass

    def removeAll(self):
        pass
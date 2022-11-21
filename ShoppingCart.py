import csv
import pandas as pd

class ShoppingCart:

    def __init__(self, user):
        self.__username = user.strip()
        self.__furniture_ID = None
        self.__quantity = 0

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
        """with open("Furniture.csv", "r") as furniture:
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
                return -1"""

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
        pass

    def removeAll(self):
        pass
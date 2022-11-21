from customers import *
from furniture import *
from ShoppingCart import *
from orderHistory import *


def afterLogin():
    # TODO: create an instance of customer, ShoppingCart, and OrderHistory
    while True:
        # TODO: display options to view furniture shop, view shopping cart, view order history, manage account, logout, and exit program
        choice = input("choice: ")
        if choice.strip().lower() == "view all furniture":
            # TODO: display all the furniture
            while True:
                choice = input(
                    "Please insert the furniture ID of the furniture that you want to add to cart or type 'go back' to go back: ")
                if choice.strip().lower() == "go back":
                    break
                else:
                    # TODO: add furniture to cart
                    pass

        elif choice.strip().lower() == "view cart":
            while True:
                # TODO: display user's cart
                # TODO: display options
                choice = input("choice: ")
                if choice.strip().lower() == "go back":
                    break
                elif choice.strip().lower() == "remove furniture":
                    # TODO: prompt for the furniture to be removed
                    # TODO: call the class to remove furniture
                    if valid:
                        # TODO: tell the user "successfully removed"
                        pass
                    if not valid:
                        # TODO: tell the user
                        pass
                elif choice.strip().lower() == "checkout":
                    # TODO: call the class function
                    print("Thank you. Your order has been processed")
                    break
                else:
                    print("unknown command")

        elif choice.strip().lower() == "view order history":
            # TODO: list all order history
            pass

        elif choice.strip().lower() == "manage account":
            while True:
                # TODO: list choices
                choice = input("choice: ")
                if choice.strip().lower() == "go back":
                    break
                elif choice.strip().lower() == "edit shipping info":
                    #TODO: prompt for new info
                    if choice.strip().lower() != "go back":
                        #TODO: call the class to update user info
                        print("info updated!")
                elif choice.strip().lower() == "edit payment info":
                    #TODO: prompt for new info
                    if choice.strip().lower() != "go back":
                        #TODO: call the class to update user info
                        print("info updated!")
                elif choice.strip().lower() == "delete account":
                    while True:
                        # TODO: ask user for confirmation
                        if choice.strip().lower() == "no" or choice.strip().lower() == "go back":
                            break
                        elif choice.strip().lower() == "yes":
                            # TODO: call delete customer
                            return
                        else:
                            print("try again")
                else:
                    print("unknown command")

        elif choice.strip().lower() == "logout":
            return
        elif choice.strip().lower() == "exit program":
            exit()
        else:
            print("unknown command")


# TODO: create an instance of Furniture

while True:
    # TODO: display welcome message and the 3 options
    choice = input("What would you like to do? ")
    if choice.strip().lower() == "login":
        while True:
            # TODO: prompt for user's username
            if user.strip().lower() == "go back":
                break
            # TODO: prompt for user's password
            if password.strip().lower() == "go back":
                break
            # TODO: calls valid = customers.login() with user.strip() and password.strip()
            if valid:
                afterLogin()
            if not valid:
                # TODO: print a message telling the user that their username/password combo is invalid
                pass

    elif choice.strip().lower() == "create account":
        while True:
            #TODO: ask for the info step by step
            # if at anytime they wanna go back then break
            # call the class function to create customer
            if valid:
                #TODO: ask them for their shipping and payment info
                #TODO: call the class functions to add those
                #TODO: tell them to use those info to login
                break
            if not valid:
                #TODO: tell them the username already exist so try again
                pass

    elif choice.strip().lower() == "exit program":
        exit()
    else:
        print("unknown command")

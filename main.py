from customers import *
from Furniture import *
from ShoppingCart import *
from OrderHistory import *

def afterLogin(user):
    current = Customer()
    for x in customers:
        if x.username == user:
            current = x
    # TODO: create an instance of ShoppingCart, and OrderHistory
    while True:
        print("\t1. view all furniture\n\t2. view shopping cart\n\t3. view order history\n\t4. manage account\n\t5. logout\n\t6. exit")
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
                print("\t\t1. go back\n\t\t2. edit shipping info\n\t\t3. edit payment info\n\t\t4. delete account")
                choice = input("choice: ")
                if choice.strip().lower() == "go back":
                    break
                elif choice.strip().lower() == "edit shipping info":
                    newadd = input("New shipping address: ")
                    if newadd.strip().lower() != "go back":
                        current.edit_add(newadd)
                        rewrite_customer()
                        print("info updated!")
                elif choice.strip().lower() == "edit payment info":
                    newcard = input("New card number: ")
                    if choice.strip().lower() != "go back":
                        current.edit_card(newcard)
                        rewrite_customer()
                        print("info updated!")
                elif choice.strip().lower() == "delete account":
                    while True:
                        choice = input("Are you sure you want to delete your account? ")
                        if choice.strip().lower() == "no" or choice.strip().lower() == "go back":
                            break
                        elif choice.strip().lower() == "yes":
                            delete_account(current)
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
process_customer()

while True:
    # Display welcome message
    print("Welcome!\n1. Login\n2. Create Account\n3. Exit\n")
    choice = input("What would you like to do? ")
    # chooses login
    if choice.strip().lower() == "login":
        while True:
            # ask for username
            user = input("Username: ")
            if user.strip().lower() == "go back":
                break
            # ask for password
            password = input("Password: ")
            if password.strip().lower() == "go back":
                break
            # try to log the user in
            valid = customers.login(user.stip(), password.strip())
            # successful login
            if valid:
                afterLogin(user)
            # not successful login
            if not valid:
                print("The username and/or password is incorrect.")
                pass

    elif choice.strip().lower() == "create account":
        while True:
            username = input("\tUsername: ")
            if username.strip().lower() == "go back":
                break
            exists = user_exists(username)
            if exists is False:
                print("\tThat user name already exists. Please pick a new one.")
            else:
                password = input("\tPassword: ")
                if password.strip().lower() == "go back":
                    break
                fn = input("\tFirst Name: ")
                if fn.strip().lower() == "go back":
                    break
                ln = input("\tLast Name: ")
                if ln.strip().lower() == "go back":
                    break
                add = input("\tShipping Address: ")
                if add.strip().lower() == "go back":
                    break
                card = input("\tCredit Card Number: ")
                if card.strip().lower() == "go back":
                    break
                newcustomer = Customer()
                newcustomer.create_account(username, password, fn, ln, add, card)
                print("\tAccount Created!")

    elif choice.strip().lower() == "exit program":
        exit()
    else:
        print("unknown command")

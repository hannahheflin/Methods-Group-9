from customers import *
from Furniture import *
from ShoppingCart import *
from orderHistory import *

furniture = Furniture()

def afterLogin(user):
    current = Customer()
    for x in customers:
        if x.username == user:
            current = x
    # TODO: create an instance of OrderHistory
    userCart = ShoppingCart(user)
    
    while True:
        print("\nPlease select an option\n1. view all furniture\n2. view shopping cart\n3. view order history\n4. manage account\n5. logout\n6. exit")
        choice = input("choice: ")
        
        if choice.strip().lower() == "view all furniture" or choice.strip() == "1":
            while True:
                furniture.displayInventory()
                doubleBreak = 0 #flag variable 
                itemID = input(
                    "\nPlease insert the furniture ID of the furniture that you want to add to cart or type 'go back' to go back: ")
                if itemID.strip().lower() == "go back":
                    break
                else:
                    while True:
                        quant = input("how many of that item do you want to add? ")
                        if quant.strip().lower() == "go back":
                            doubleBreak = 1
                            break
                        try:
                            quant = int(quant.strip())
                            break
                        except:
                            print("quantity must be an integer!")
                    if not doubleBreak:
                        validItem = userCart.addItem(itemID.strip(), quant)
                        if validItem == 0:
                            print("Item successfully added!")
                        else:
                            print("\nFailed to add the item. Make sure the item ID is correct and quantity being inputted into your cart does not exceed what is in stock")

        elif choice.strip().lower() == "view shopping cart" or choice.strip() == "2":
            while True:
                userCart.displayCart()
                print("Select a choice:\n1. go back\n2. remove furniture\n3. checkout")
                choice = input("choice: ")
                if choice.strip().lower() == "go back" or choice.strip() == "1":
                    break
                elif choice.strip().lower() == "remove furniture" or choice.strip() == "2":
                    while True:
                        doubleBreak = 0 #flag variable 
                        userCart.displayCart()
                        # removing furniture from the user's CART, not from store inventory
                        try:
                            itemID = input("Type the furniture ID of the furniture that you wish to be removed or 'go back' to go back: ")
                            if itemID.strip().lower() == "go back":
                                break
                            while True:
                                quant = input("How many of that item do you wish to remove? ")
                                if quant.strip().lower() == "go back":
                                    doubleBreak = 1
                                    break
                                try:
                                    quant = int(quant.strip())
                                    break
                                except:
                                    print("quantity must be an integer!")
                        except:
                            print("\n** Error! **\n")

                        if not doubleBreak:
                           valid = userCart.removeItem(itemID.strip(), quant)
                           if valid == 0:
                               print("Item successfully removed")
                           else:
                               print("\nFailed to remove the item. Make sure that you entered the correct item ID")  
                               
                elif choice.strip().lower() == "checkout" or choice.strip() == "3":
                    valid = userCart.removeAll()
                    if valid == 0:
                        print("\nThank you. Your order has been processed")
                        break
                    else:
                        print("\ncheckout failed. Please make sure the quantity of items in your cart is up to date")
                else:
                    print("\nunknown command")

        elif choice.strip().lower() == "view order history" or choice.strip() == "3":
            # TODO: list all order history
            pass

        elif choice.strip().lower() == "manage account" or choice.strip() == "4":
            while True:
                print("\nSelect a choice:\n1. go back\n2. edit shipping info\n3. edit payment info\n4. delete account")
                choice = input("choice: ")
                if choice.strip().lower() == "go back" or choice.strip() == "1":
                    break
                elif choice.strip().lower() == "edit shipping info" or choice.strip() == "2":
                    newadd = input("\nNew shipping address: ")
                    if newadd.strip().lower() != "go back":
                        current.edit_add(newadd)
                        rewrite_customer()
                        print("info updated!")
                elif choice.strip().lower() == "edit payment info" or choice.strip() == "3":
                    newcard = input("\nNew card number: ")
                    if newcard.strip().lower() != "go back":
                        current.edit_card(newcard)
                        rewrite_customer()
                        print("info updated!")
                elif choice.strip().lower() == "delete account" or choice.strip() == "4":
                    while True:
                        choice = input("\nAre you sure you want to delete your account? ")
                        if choice.strip().lower() == "no" or choice.strip().lower() == "go back":
                            break
                        elif choice.strip().lower() == "yes":
                            delete_account(current)
                            return
                        else:
                            print("try again")
                else:
                    print("\nunknown command")

        elif choice.strip().lower() == "logout" or choice.strip() == "5":
            return
        
        elif choice.strip().lower() == "exit program" or choice.strip() == "6" or choice.strip().lower() == "exit":
            exit()
            
        else:
            print("\nunknown command")

process_customer()

while True:
    # Display welcome message
    print("\nWelcome! Please select an option\n1. Login\n2. Create Account\n3. Exit program\n\nAt any point in the program you can type 'go back' to return to the previous menu")
    choice = input("What would you like to do? ")
    # chooses login
    if choice.strip().lower() == "login" or choice.strip() == "1":
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
            valid, error = login(user.strip(), password.strip())
            # successful login
            if valid:
                afterLogin(user)
                break
            # not successful login
            if not valid:
                if error == "user":
                    print("\nThat username doesn't exist.\n")
                elif error == "pass":
                    print("\nThe password you entered is incorrect.\n")

    elif choice.strip().lower() == "create account" or choice.strip() == "2":
        while True:
            username = input("Username: ")
            if username.strip().lower() == "go back":
                break
            exists = user_exists(username)
            if exists is False:
                print("That user name already exists. Please pick a new one.")
            else:
                password = input("Password: ")
                if password.strip().lower() == "go back":
                    break
                fn = input("First Name: ")
                if fn.strip().lower() == "go back":
                    break
                ln = input("Last Name: ")
                if ln.strip().lower() == "go back":
                    break
                add = input("Shipping Address: ")
                if add.strip().lower() == "go back":
                    break
                card = input("Credit Card Number: ")
                if card.strip().lower() == "go back":
                    break
                newcustomer = Customer(username, password, fn, ln, add, card)
                newcustomer.create_account()
                print("Account Created!")
                break
            
    elif choice.strip().lower() == "exit program" or choice.strip() == "3" or choice.strip().lower() == "exit":
        exit()
        
    else:
        print("\nunknown command")

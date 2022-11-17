import math

# openFile()
## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")
        print("File opened.")

    except OSError:
        print("Invalid file.")

    except:
        print("something went wrong!")

# numbers()
## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        return num1 / num2
    
    except TypeError:
        return "Invalid inputs"
    
    except ZeroDivisionError:
        return "Cannot divide by 0"

    except:
        return "something went wrong!"

# dist()


# isPalindrome()


# divide()
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
    except TypeError:
        return "Invalid Inputs."
    except:
        return "something went wrong."

    try:
        div = num1 / num2
    except ZeroDivisionError:
        return "Can't divide by 0"
    except:
        return "something went wrong."

    print("Your numbers divided is:", div)

# sq()
## returns the squareroot of a particular number
def sq(num):
    try:
        number = math.sqrt(num)
    except TypeError:
        return "Invalid input."
    except ValueError:
        return "Cannot square root a negative."
    except:
        return "something went wrong."

    return number

# greetUser()


# displayItem()


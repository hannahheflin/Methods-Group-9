import math

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

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)

        return dist
    
    except TypeError:
        return "Invalid inputs"
    
    except:
        return "something went wrong!"

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        test = temp[::-1]

        if(test == temp):
            return True

        else:
            return False
    
    except TypeError:
        return "Invalid input"

    except:
        return "something went wrong!"

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)

    except ValueError:
        print("Invalid inputs")

    except ZeroDivisionError:
        print("Cannot divide by 0")

    except:
        print("something went wrong!")

## returns the squareroot of a particular number
def sq(num):
    try:
        return math.sqrt(num)

    except TypeError:
        return "Invalid input."

    except ValueError:
        return "Cannot square root a negative."

    except:
        return "something went wrong."

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    if not (str(first).isalpha() and str(middle).isalpha() and str(last).isalpha()):
        print("Names should only contain letters")
    
    else:
        print("Hello!")
        print("Welcome to the program", first, middle, last)
        print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    try:
        print("Your item at", index, "index is", numbers[index])

    except TypeError:
        print("numbers must be a list and index must be an integer!")

    except IndexError:
        print("Index out of range")

    except:
        print("something went wrong!")
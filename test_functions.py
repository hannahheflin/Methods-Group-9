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
import pytest
from functions import *

# tests for openFile
@pytest.mark.parametrize("filename, output", [("dne.txt", "Invalid file."), (101, "Invalid file."), ("testing.txt", "File opened.")])
def test_openFile(filename, output, capsys):
    openFile(filename)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == output

# tests for numbers
@pytest.mark.parametrize("num1, num2, output", [("one", 2, "Invalid inputs"), (1, 0, "Cannot divide by 0"), (20, 4, 5), (0.5, -2.5, -0.2)])
def test_numbers(num1, num2, output):
    assert numbers(num1, num2) == output

# tests for dist
@pytest.mark.parametrize("x1, y1, x2, y2, output", [(1, 2, 1, "two", "Invalid inputs"), (1, 5, 2, -6, 11.045361017187261), (3.5, -2.6, 0.5, 1.4, 5)])
def test_dist(x1, y1, x2, y2, output):
    assert dist(x1, y1, x2, y2) == output

# tests for isPalindrone
@pytest.mark.parametrize("temp, value", [(101, "Invalid input"), ("racecar", True), ("race", False)])
def test_isPalindrome(temp, value):
    assert isPalindrome(temp) == value

# tests for divide
def geninputs():
    inputs = ["one", "two"]
            
    for item in inputs:
        yield item
        
GEN = geninputs()

def test_divide(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    divide()

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Invalid inputs"

def geninputs2():
    inputs = [123.456, 789.123]
            
    for item in inputs:
        yield item
        
GEN2 = geninputs2()

def test_divide2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN2))

    assert divide() == None

def geninputs3():
    inputs = [5, 0]
            
    for item in inputs:
        yield item
        
GEN3 = geninputs3()

def test_divide3(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN3))

    divide()

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Cannot divide by 0"

def geninputs4():
    inputs = [5, -2]
            
    for item in inputs:
        yield item
        
GEN4 = geninputs4()

def test_divide4(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN4))

    divide()

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: -2.5"

def geninputs5():
    inputs = [6.6, 2.4]
            
    for item in inputs:
        yield item
        
GEN5 = geninputs5()

def test_divide5(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN5))

    divide()

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 2.75"

# tests for sq
@pytest.mark.parametrize("num, result", [("five thousand", "Invalid input"), (-4, "Input cannot be negative"), (9, 3), (4.84, 2.2)])
def test_sq(num, result):
    assert sq(num) == result

# tests for greetUser
@pytest.mark.parametrize("first, middle, last, greeting", [("M!llie", "Br3nda", "Br0wn!!!", "Hello!\nWelcome to the program M!llie Br3nda Br0wn!!!\nGlad to have you!"), (123, 456, 7890, "Names should only contain letters"), ("John", "Doe", "Smith", "Hello!\nWelcome to the program John Doe Smith\nGlad to have you!")])
def test_greetUser(first, middle, last, greeting, capsys):
    greetUser(first, middle, last)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == greeting

# tests for displayItem
@pytest.mark.parametrize("numbers, index, output", [(-3, 0, "No list is given"), ([1, 2.5, -3], 0.1, "Index must be an integer"), ([1, 2.5, -3], "zero", "Index must be an integer"), ([1, 2.5, -3], 3, "Index out of range"), ([1, 2.5, -3], 2, "Your item at 2 index is -3")])
def test_displayItem(numbers, index, output, capsys):
    displayItem(numbers, index)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == output
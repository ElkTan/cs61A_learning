import random
import string

def old():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=3))
    return letters + numbers

def new():
    numbers = ''.join(random.choices(string.digits, k=4))
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    return numbers + letters

def func():
    if random.choice([1, 0]):
        return old()
    else:
        return new()

def main():
    plate =func()
    print(plate)


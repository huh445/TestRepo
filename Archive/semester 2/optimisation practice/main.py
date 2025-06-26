import time
import random

class App:
    def __init__(self):
        john = 0
        steve = []
        while john != 47:
            john = random.randint(1,1000000)
            steve.append(john)
        print(len(steve))

if __name__ == "__main__":
    App()
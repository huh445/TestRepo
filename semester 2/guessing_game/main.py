import random


number = random.randint(1,100)
while True:
    user_input = int(input("Guess a Number"))
    print(number)

    if user_input < number:
        print("Guess Higher!")
    elif user_input > number:
        print("Guess Lower!")
    elif user_input == number:
        print("You Win!")
        break
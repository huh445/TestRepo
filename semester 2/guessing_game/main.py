import random  # Import the random module to generate random numbers

random_number = random.randint(1, 100)  # Generate a random integer between 1 and 100

while True:  # Start an infinite loop to allow continuous guessing
    user_input = int(input("Guess a number between 1 and 100: "))  # Prompt the user to enter their guess and convert it to an integer

    if user_input < random_number:  # Check if the guess is less than the random number
        print("Guess Higher!")  # Inform the user to guess a higher number
    elif user_input > random_number:  # Check if the guess is greater than the random number
        print("Guess Lower!")  # Inform the user to guess a lower number
    elif user_input == random_number:  # Check if the guess is equal to the random number
        print("You Win!")  # Congratulate the user for guessing correctly
        break  # Exit the loop since the correct number was guessed

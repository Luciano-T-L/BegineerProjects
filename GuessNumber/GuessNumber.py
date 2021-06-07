# Guess the number - Computer

import random
import os


# Function to clear the command line after a game
def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


# function for the game
def random_game():
    attempts = []
    try:
        x = int(input("Chose a number for the range 0 to: "))
        random_number = random.randint(0, x)
        guess = int(input("Try a number: "))

        while guess != random_number:
            if random_number < guess:
                print("Too high")
            else:
                print("Too low")

            attempts.append(guess)
            print(f"attempts: {attempts}")
            guess = int(input("Try other number: "))
        print("Congratulation, you won!!")
    except ValueError:
        print("you have to give a number!")



# Function to start the game with some strings/make the loop until the user quit the game
def engine():
    print("-----------Welcome to the Guess Number game-----------")
    print("")
    random_game()

    while True:
        play_again = input("Do you want to play again? Yes/No ").upper()
        clear()
        if play_again == "YES":
            engine()
        else:
            print("\nBye bye! See you!")
            return False


engine()

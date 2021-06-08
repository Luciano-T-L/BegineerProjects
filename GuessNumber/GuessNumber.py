# Guess the number - Computer

import random
import os


# Function to clear the command line after a game
def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


# function for the game where the user try to guess the number
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


def guess_number_computer():
    print("Chosing the range...")
    maximum = random.randint(0, 100)
    minimum = 0
    print(f"The range is {minimum} to {maximum}")
    choice = int(input("Choise a number in the range: "))
    print('')
    
    try:
        while True:
            print(f"Chosen number: {choice}")
            try1 = random.randint(minimum, maximum)
            print(f"Is the number {try1}?")
            print('')
            high_low = input("Too high? (H) / Too low (L) or Correct (C) ").upper()

            if high_low == "H":
                maximum = try1 - 1
                clear()
            elif high_low == 'L':
                minimum = try1 + 1
                clear()
            elif choice == try1:
                print("Haha, I'm correct")
                return False
            else:
                print("Sothing went wrong!")

    except ValueError:
            print("There're no more options!")


# Function to start the game with some strings/make the loop until the user quit the game
def engine():
    print("-----------Welcome to the Guess Number game-----------")
    print("")
    game_play = input("Do you want to guess de number (1) or chose the number for the computer try to guess (2)")

    if game_play == "1":
        random_game()
        while True:
            play_again = input("Do you want to play again? Yes/No ").upper()
            clear()
            if play_again == "YES":
                engine()
            else:
                clear()
                print("\nBye bye! See you!")
                exit()

    elif game_play == "2":
        guess_number_computer()
        while True:
            play_again = input("Do you want to play again? Yes/No ").upper()
            clear()
            if play_again == "YES":
                engine()
            else:
                clear()
                print("\nBye bye! See you!")
                exit()


engine()

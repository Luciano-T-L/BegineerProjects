import random
import os   


def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


def game():
    print("\n---------------Welcome to the rock, paper and scissors---------------\n")

    print("Rock (R), Paper (P) or Scissors(S)")
    choice = input("> ").upper()
    computer = random.choice(["R", "P", "S"])

    if choice == computer:
        print(f"You = {choice} and computer = {computer}")
        print("Tied game!")
    elif choice == "R" and computer == "S":
        print(f"You = {choice} and computer = {computer}")
        print("You win")
    elif choice == "R" and computer == "P":
        print(f"You = {choice} and computer = {computer}")
        print("You lose")
    elif choice == "P" and computer == "S":
        print(f"You = {choice} and computer = {computer}")
        print("You lose")
    elif choice == "P" and computer == "R":
        print(f"You = {choice} and computer = {computer}")
        print("You won")
    elif choice == "S" and computer == "R":
        print(f"You = {choice} and computer = {computer}")
        print("You lose")
    elif choice == "S" and computer == "P":
        print(f"You = {choice} and computer = {computer}")
        print("You won")
    else:
        print("Somthing went wrong!")


def engine():
    game()

    while True:
        play_again = input("Do you want to play again? Yes/No ").upper()

        if play_again == "YES":
            clear()
            game()
        else:
            print("Bye Bye")
            quit()


engine()
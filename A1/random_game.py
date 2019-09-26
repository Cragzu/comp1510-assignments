"""
Module containing a function to play a rudimentary rock-paper-scissors game.
"""
import random


def determine_winner(cpu, user_loss, user_win):
    if cpu == user_loss:  # paper beats rock
        print("You lost. :(")
    elif cpu == user_win:
        print("You won!")
    else:
        print("Stalemate.")


def rock_paper_scissors():
    cpu_choice = random.randint(0, 2)  # 0 = rock, 1 = paper, 2 = scissors

    user_choice = input("Choose rock, paper, or scissors?: ")
    # todo: clean input with string methods

    if cpu_choice == 0:
        print("CPU chose rock.")
    elif cpu_choice == 1:
        print("CPU chose paper.")
    else:
        print("CPU chose scissors.")

    if user_choice == "rock":
        determine_winner(cpu_choice, 1, 2)
    elif user_choice == "paper":
        determine_winner(cpu_choice, 2, 0)
    elif user_choice == "scissors":
        determine_winner(cpu_choice, 0, 1)
    else:
        print("That wasn't a valid input. Choose only rock, paper, or scissors.")


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    rock_paper_scissors()


if __name__ == "__main__":
    main()


'''
Generate a random number between 0 and 1 to represent rock, paper, and scissors. Ask the user for their selection, and
clean it of irregular characters and whitespace. If the input is not 'rock', 'paper', or 'scissors' return a warning
message. Otherwise determine who won and return that info.

    0 = rock, 1 = paper, 2 = scissors
    paper beats rock beats scissors beats paper

Computational thinking:
   
'''
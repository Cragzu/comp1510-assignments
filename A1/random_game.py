"""
Module containing a function to play a rudimentary rock-paper-scissors game.
"""
import random


def determine_winner(cpu, user_loss, user_win):
    """
    Determine the winner of a rock-paper-scissors game between the user and the CPU based on the given parameters.

    :precondition: all parameters must be the types specified below
    :postcondition: function will print a string letting the user know whether they won, lost, or tied the game
    :param cpu: an int between 0 and 2, randomly generated and passed to this function
    :param user_loss: an int between 0 and 2 representing the choice that would let the CPU win
    :param user_win: an int between 0 and 2 representing the choice that would let the CPU lose
    :return: none, uses print statements
    """
    if cpu == user_loss:  # cpu beats player
        print("You lost. :(")
    elif cpu == user_win:  # player beats cpu
        print("You won!")
    else:
        print("Stalemate.")


def rock_paper_scissors():
    """
    Play a simple game of rock-paper-scissors with the user.

    Generate a random number between 0 and 2 to represent the CPU's choice and display it to the user. Ask the user
    for their choice, and clean it. If it was invalid, display an error message.

    Pass parameters into the determine_winner function to find the winner, display it.

    :precondition: user must input either rock, paper, or scissors
    :postcondition: function will run the game and determine who won, or if there was a draw
    :return: none, uses print statements
    """
    cpu_choice = random.randint(0, 2)  # 0 = rock, 1 = paper, 2 = scissors

    user_choice = input("Choose rock, paper, or scissors?: ")
    user_choice = user_choice.lower()
    user_choice = user_choice.strip()

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
        print("That wasn't a valid input. Please type only rock, paper, or scissors.")


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
   Decomposition: Broke the function down into helper functions to reduce repetition.
   Abstraction: Used generated numbers to represent the CPU's choice to keep things simple.
'''

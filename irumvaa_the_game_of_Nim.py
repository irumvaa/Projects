######################################################################
# Author: Alain Irumva
# Username: irumvaa
#
# Assignment: HW06: The Game of Nim
#
# Purpose: This program is designed to implement the game of Nim
######################################################################
# Acknowledgements:
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random
def balls_to_start_with():
    """
  Prompt for a username and a valid starting number of balls (>= 15).
    Returns the starting number as an int
"""
    user_name = input("Enter your username for the game: ")
    print(f" Welcome to the Game of Nim, {user_name}")
    balls = int(input(f"Dear {user_name}, Enter the number of the balls you want to start with(15 or more): "))
    while balls < 15:
        print(f"Dear {user_name} make sure to start with at least 15.")
        balls = int(input("Re-enter your number again (15 or more): "))
    return balls


def human_playing():
    """
   Prompt the human for a move between 1 and 4 (inclusive).
    Returns the chosen amount a
"""
    remove = int(input("How many balls do you remove? (1–4): "))
    while remove < 1 or remove > 4:
        print("Invalid move. Pick between 1 and 4.")
        remove = int(input("{How many balls do you remove? (1–4): "))
    return remove


def computer_playing(balls_left):
    """
Computer chooses (using randomness) a number of balls to remove (1–4).
Return int
"""
    return random.randint(1, 4)


def main():
    """
Run one game of Nim: human vs computer, human goes first.
    The player who takes the last ball wins.
"""
    balls = balls_to_start_with()
    print(f"\nGame begins with {balls} balls!")

    # Human always goes first
    human_turn = True

    while balls > 0:
        print(f"\nBalls remaining: {balls}")

        if human_turn:
            remove = human_playing()
            print(f"You remove {remove} ball(s).")
        else:
            remove = computer_playing(balls)
            print(f"Computer removes {remove} ball(s).")

        balls -= remove
        human_turn = not human_turn


    if human_turn:
        print("\nComputer wins!")
    else:
        print("\nYou win!")

main()
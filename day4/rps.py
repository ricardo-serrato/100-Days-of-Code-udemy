# 1. Just entering on Y or N breaks the program
# 2. The computer does not reroll

from ascii_art import rock, paper, scissors
import random
import os
import time

ARTWORK = [rock, paper, scissors]
COMPUTER_MOVE = random.randint(0, 2)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_choice():
    while True:
        try:
            choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

            if choice < 0 or choice > 2:
                raise ValueError
            else:
                return choice
        except ValueError:

            # os.system('cls||clear')
            print('Please enter a valid input Ex: 0, 1, or 2')


def get_winner(p1Move, p2Move):
    time.sleep(.2)
    if p1Move == 0 and p2Move == 2:
        print(f"player one plays:\n{ARTWORK[p1Move]}\n player two plays:{ARTWORK[p2Move]}")
        print("PLAYER ONE WINS.")
    elif p2Move == 2 and p1Move == 0:
        print(f"player one plays:\n{ARTWORK[p1Move]}\n player two plays:{ARTWORK[p2Move]}")
        print("PLAYER TWO WINS.")
    elif p1Move > p2Move:
        print(f"player one plays:\n{ARTWORK[p1Move]}\n player two plays:{ARTWORK[p2Move]}")
        print('PLAYER ONE WINS')
    elif p1Move < p2Move:
        print(f"player one plays:\n{ARTWORK[p1Move]}\n player two plays:{ARTWORK[p2Move]}")
        print('PLAYER TWO WINS')
    else:
        print(f"player one plays:\n{ARTWORK[p1Move]}\n player two plays:{ARTWORK[p2Move]}")
        print("It's a Tie!")


def play_game():
    player_choice = get_choice()
    get_winner(player_choice, COMPUTER_MOVE)


def play_again():
    while True:
        answer = input('Would you want to play again? press [Y] or [N]: ').upper()[0]

        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            print("invalid choice")


def start_game():
    while True:
        game_on = input('Would you like to start a game of Rock Paper & Scissors?: [Y] or [N]: ').upper()[0]
        if game_on == 'Y':
            return True
        elif game_on == 'N':
            return False
        else:
            print("Invalid input")



print('Welcome to My text based game of Rock, Paper, and Scissors.')

game_is_on = start_game()
while game_is_on:
    play_game()
    if not play_again():
        game_is_on = False
    clear_screen()
print('Thank you for playing!')











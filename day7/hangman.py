from hangman_art import stages, logo
from hangman_wordlist import word_list
import os, random


word = random.choice(word_list)
lives = len(stages)-1
correct_guesses = ['_' for _ in range(len(word))]
guesses = set()


def get_letter_input():
    while True:
        char = input("Guess a letter: ").lower()

        if char == "":
            print("Expected a single character but instead received nothing.")
            continue

        if len(char) != 1:
            print("Only enter a single character at a time")
            continue


        if not char.isalpha():
            print("please enter a valid entry")
            continue
        else:
            return char


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_win():
    if '_' not in correct_guesses:
        return True
    return False


def print_word():
    print("".join(correct_guesses))


def print_mannequin():
    print(stages[lives])


def update_correct_guesses(g):
    for i in range(len(word)):
        if word[i] == g:
            correct_guesses[i] = g


print(logo)


while lives > 0:
    if check_win():
        print('You Won!')
        break

    guess = get_letter_input()

    if guess in guesses:
        clear_screen()
        print(f'You have already guessed {guess}')
        print_word()
        print_mannequin()
        continue

    if guess in word:
        guesses.add(guess)
        update_correct_guesses(guess)
        clear_screen()
    else:
        lives -= 1
        guesses.add(guess)
        clear_screen()
        print(f"The word {guess} is not in the word.")

    if lives == 0:
        print_mannequin()
        print("You Lost")
        break

    print_word()
    print_mannequin()


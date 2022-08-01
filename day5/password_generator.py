import random
import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
symbols = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ',', "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_integer(char):
    while True:
        try:
            size = int(input(f"How many {char} would you like in your password?\nEnter amount: "))

        except ValueError:
            print("Invalid input")
        else:
            return size


letter = get_integer('letters')
symbol = get_integer('symbols')
number = get_integer('numbers')

letter_list = [random.choice(alphabet) for _ in range(letter)]
symbol_list = [random.choice(symbols) for _ in range(symbol)]
number_list = [random.choice(numbers) for _ in range(number)]

shuffled_pass = letter_list+symbol_list+number_list
random.shuffle(shuffled_pass)

password = "".join(char for char in shuffled_pass)















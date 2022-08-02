import string,os
from art import logo

letters = list(string.ascii_lowercase)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_choice():
    while True:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()

        if choice == 'e' or choice =='d' or choice == 'encode' or choice == 'decode':
            return choice
        else:
            clear_screen()
            print("Invalid Entry please enter either 'encode or 'decode'. ")


def get_shift_number():
    while True:
        n = input("Type the shift number: ")
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('Only positive integers are accepted.')
            continue


def encode(t, s):
    encoded_text = ''
    for char in t:
        if char not in letters:
            encoded_text += char
            continue
        final_shift = (s + letters.index(char)) % 26
        encoded_text += letters[final_shift]
    return encoded_text


def decode(t, s):
    decoded_text = ''
    for char in t:
        if char not in letters:
            decoded_text += char
            continue
        final_shift = (letters.index(char) - s) % 26
        decoded_text += letters[final_shift]
    return decoded_text


def run_again():
    while True:
        rerun = input("Type 'yes' if you want to go again. Otherwise type 'no': ").strip().lower()

        if rerun == 'yes' or rerun == 'y':
            return True
        if rerun == 'no' or rerun == 'n':
            return False
        else:
            clear_screen()
            print('Invalid Entry. please enter the appropriate command.')


start_cypher = True
print(logo)
while start_cypher:
    choice = get_choice()
    text = input('Type your message: ').strip().lower()
    shift = get_shift_number()
    if choice == 'e' or choice == 'encode':
        print("Your encoded text is: ")
        print(encode(text, shift))
    elif choice == 'd' or choice == 'decode':
        print("Your decoded text is: ")
        print(decode(text, shift))

    start_cypher = run_again()
    clear_screen()



import os

def draw(errors):
    if errors == 0:
        print("  +----------------------------+")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 1:
        print("  +----------------------------+")
        print("  |                            0")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 2:
        print("  +----------------------------+")
        print("  |                            0")
        print("  |                            |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 3:
        print("  +----------------------------+")
        print("  |                            0")
        print("  |                           /|")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 4:
        print("  +----------------------------+")
        print("  |                            0")
        print("  |                           /|\\")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 5:
        print("  +----------------------------+")
        print("  |                            0")
        print("  |                           /|\\")
        print("  |                           /")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 6:
        print("  +----------------------------+")
        print("  |                            0")
        print("  |                           /|\\")
        print("  |                           / \\")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")
    elif errors == 7:
        print("  +----------------------------+")
        print("  |                         ___0___")
        print("  |                           /|\\")
        print("  |                           / \\")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("--+------------------------------------")

def check_word(letter, secret):
    if letter in secret:
        return True
    else:
        return False

def check_used_letters(letter, letters_array):
    if letter in letters_array:
        return True
    else:
        return False

def check_winner(hidden_word):
    if " " not in hidden_word:
        return True
    else:
        return False

def check_looser(n_error):
    if n_error == 7:
        return True
    else:
        return False

secret = input("Player 2 enter the secret: ")
secret = secret.upper()

hidden_word = [" " for i in range(0,len(secret))]
letters_array = list()

os.system('cls')

n_error = 0

while True:
    print(chr(27) + "[2J")
    draw(n_error)
    
    if check_looser(n_error):
        os.system('cls')
        print("Player 2 won!")
        print("The secret is: ", secret,".", sep='')
        break

    if check_winner(hidden_word):
        os.system('cls')
        print("Player 1 won!")
        print("The secret is: ", secret,".", sep='')
        break
    
    print("Secret:", hidden_word)
    print("Tries:", letters_array)
    letter = input ("Player 1 enter one letter: ")
    letter = letter.upper()
    if check_used_letters(letter, letters_array):
        print("Letter already selected, please choose other!")
    else:
        letters_array.append(letter)
        if check_word(letter, secret):
            for i in range(len(secret)):
                if secret[i] == letter:
                    hidden_word[i] = letter
        else:
            n_error += 1

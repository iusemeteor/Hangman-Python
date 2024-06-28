import os
import random
from colorama import init, Fore, Back, Style

a = Fore.CYAN + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
r = Fore.RED + Style.BRIGHT
res = Style.RESET_ALL

with open('words.txt', 'r') as file:
    words = file.readlines()

random_word = random.choice(words).strip()
word = '_' * len(random_word)
incorrect_letters = []

VERSION = "v2.0.0"
AUTHOR = "meteor"

CHEAT = False

attempts = 6

tries = 0


def startup():
    clear()
    print(f"{a}Hangman Game {res}| {a}{VERSION}{res}")
    print(f"{a}Author: {res}{AUTHOR}")
    if CHEAT == True:
        print(f"{a}Word: {res}{random_word}")
    else:
        print(f"{a}Word: {res}{word}")
    if attempts == 6:
        print(f''' ______
|/   |
|   
|    
|    
|    
|______{res}
    ''')


def game():
    global attempts, word, tries
    while True:
        if word == random_word and tries == 0:
            print(f"{g}Wow, you beat that in only one attempt.{res}")
            input()
            exit()
        elif tries == 1 and word == random_word:
            print(f"{g}Congratulations, you won in only {tries} try!{res}")
            input()
            exit()
        elif word == random_word:
            print(f"{g}Congratulations, you won in only {tries} tries!{res}")
            input()
            exit()
        elif attempts == 0:
            print(f"{r}You lost! The word was {random_word}.{res}")
            input()
            exit()

        letter = input(f"{Fore.WHITE}{Style.BRIGHT}Enter a letter or the entire word: ").lower()
        if len(letter) != 1 and letter != random_word:
            print(f"{r}Please enter one letter or the entire word.")
        elif not letter.isalpha() and letter != random_word:
            print(f"{r}Please enter a letter or the entire word.")
        elif letter in incorrect_letters or letter in word:
            print(f"{r}You already guessed that!{res}")

        elif letter in random_word:
            word = random_word if letter == random_word else ''.join(
                [letter if random_word[i] == letter else word[i] for i in range(len(random_word))])
            if word != random_word:
                print(f"{Fore.GREEN}{Style.BRIGHT}Correct! The word is now {word}.{res}")
        elif letter not in random_word and tries == 0:
            attempts -= 1
            tries += 1
            startup()
            print(f"{Fore.RED}{Style.BRIGHT}Incorrect! You have {attempts} attempts left!{res}")
            print(f''' ______
|/   |
|   (_)
|    
|    
|    
|______{res}
    ''')
            incorrect_letters.append(letter)
        elif letter not in random_word and tries == 1:
            startup()
            attempts -= 1
            tries += 1
            print(f"{Fore.RED}{Style.BRIGHT}Incorrect! You have {attempts} attempts left!{res}")
            print(f''' ______
|/   |
|   (_)
|    |
|    |    
|    
|______{res}
    ''')
            incorrect_letters.append(letter)
        elif letter not in random_word and tries == 2:
            startup()
            attempts -= 1
            tries += 1
            print(f"{Fore.RED}{Style.BRIGHT}Incorrect! You have {attempts} attempts left!{res}")
            print(f''' ______
|/   |
|   (_)
|   \|
|    |
|    
|______{res}
    ''')
            incorrect_letters.append(letter)
        elif letter not in random_word and tries == 3:
            startup()
            attempts -= 1
            tries += 1
            print(f"{Fore.RED}{Style.BRIGHT}Incorrect! You have {attempts} attempts left!{res}")
            print(f''' ______
|/   |
|   (_)
|   \|/
|    |
|    
|______{res}
    ''')
            incorrect_letters.append(letter)
        elif letter not in random_word and tries == 4:
            startup()
            attempts -= 1
            tries += 1
            print(f"{Fore.RED}{Style.BRIGHT}Incorrect! You have {attempts} attempts left!{res}")
            print(f''' ______
|/   |
|   (_)
|   \|/
|    |
|   / 
|______{res}
    ''')
            incorrect_letters.append(letter)
        elif letter not in random_word and tries == 5:
            startup()
            attempts -= 1
            tries += 1
            print(f"{Fore.RED}{Style.BRIGHT}Incorrect! You have no attempts left!{res}")
            print(f''' ______
|/   |
|   (_)
|   \|/
|    |
|   / \\
|______{res}
    ''')
            incorrect_letters.append(letter)
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    startup()
    game()

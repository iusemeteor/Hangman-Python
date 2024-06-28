import random

with open('words.txt', 'r') as file:
    words = file.readlines()

random_word = random.choice(words).strip()
word = '_' * len(random_word)
incorrect_letters = []

VERSION = "v1.0.0"
AUTHOR = "meteor"

CHEAT = False

attempts = 6
tries = 0

def startup():
    print(f"Hangman Game | {VERSION}")
    print(f"Author: {AUTHOR}")
    print("Status: ✅")
    if CHEAT == True:
        print(f"Word: {random_word}")
    else:
        print(f"Word: {word}")
    print("")


def game():
    global attempts, word, tries
    while True:
        if word == random_word and tries == 0:
            print("Wow, you beat that in only one attempt.")
            input()
            exit()
        elif word == random_word:
            print(f"Congratulations, you won in only {tries} tries!")
            input()
            exit()
        elif attempts == 0:
            print(f"You lost! The word was {random_word}.")
            input()
            exit()

        letter = input("Enter a letter or the entire word: ")
        if len(letter) != 1 and letter != random_word:
            print("Please enter one letter or the entire word.")
        elif not letter.isalpha() and letter != random_word:
            print("Please enter a letter or the entire word.")
        elif letter in incorrect_letters or letter in word:
            print("You already guessed that!")

        elif letter in random_word:
            word = random_word if letter == random_word else ''.join(
                [letter if random_word[i] == letter else word[i] for i in range(len(random_word))])
            print(f"Correct! The word is now {word}.")
        else:
            attempts -= 1
            tries += 1
            print(f"Incorrect! You have {attempts} attempts left!")
            incorrect_letters.append(letter)


if __name__ == '__main__':
    startup()
    game()

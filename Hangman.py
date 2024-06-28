import random

with open('../../Downloads/Hangman-Python-main/Hangman-Python-main/words.txt', 'r') as file:
    words = file.readlines()

random_word = random.choice(words).strip()
word = '_' * len(random_word)

VERSION = "v1.0.0"
AUTHOR = "meteor"

CHEAT = False

attempts = 6

print(f"Hangman Game | {VERSION}")
print(f"Author: {AUTHOR}")
print("Status: ✅")
if CHEAT == True:
    print(f"Word: {random_word}")
else:
    print(f"Word: {word}")
print("")
def game():
    global attempts, word
    incorrect_letters = []
    while True:
        if word == random_word:
            print("Congratulations, you won!")
            input()
            exit()
        elif attempts == 0:
            print(f"You lost! The word was {random_word}.")
            input()
            exit()

        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Please enter one letter.")
        elif not letter.isalpha():
            print("Please enter a letter.")
        elif letter in incorrect_letters or letter in word:
            print("You already guessed that!")

        elif letter in random_word:
            word = ''.join([letter if random_word[i] == letter else word[i] for i in range(len(random_word))])
            print(f"Correct! The word is now {word}.")
        else:
            print(f"Incorrect! You have {attempts} attempts left!")
            incorrect_letters.append(letter)
            attempts -= 1

if __name__ == '__main__':
    game()

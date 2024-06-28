# Hangman Game

This is a simple Hangman game I made in python. The program randomly selects a word from a list and the player attempts to guess the word by suggesting letters. The game provides feedback on correct and incorrect guesses and tracks the number of attempts left.

## Features

- Randomly selects a word from a provided list.
- Player guesses letters to uncover the hidden word.
- Tracks remaining attempts.
- Option to reveal the word in cheat mode.

## Configuration

- **IMPOSSIBLE**: If set to `True`, gets the words from a url. Default is `False`.
- **CHEAT**: If set to `True`, reveals the selected word at the start of the game. Default is `False`.

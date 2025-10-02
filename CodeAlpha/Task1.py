'''
Task:1 HANGMAN GAME

KEY CONCEPTS USED:
random, while loop, if-else loop, strings, lists.     

'''

print("HANGMAN GAME")

import random

# Word list
words = ["papaya","apple","oranges","grapes","mango"]
word = random.choice(words)

# Game setup
tries = 6
guessed = ""

# Game loop
while tries > 0:
    blanks = ""
    for letter in word:
        if letter in guessed:
            blanks += letter
        else:
            blanks += "_"

    print("Word:", blanks)

    if blanks == word:
        print("You win!")
        break

    guess = input("Guess a letter: ")[0]
    guessed += guess

    if guess not in word:
        tries -= 1
        print("Wrong! Tries left:", tries)

# Game over
if tries == 0:
    print("You lose! The word was:", word)

# fix: pause the window from closing
input("\nPress Enter to exit...")

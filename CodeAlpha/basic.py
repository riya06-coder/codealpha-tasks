# import random

# # Word list
# words = ["apple", "banana", "oranges", "grapes", "mango", "straberry","pineapple"]
# word = random.choice(words)

# # Game setup
# tries = 5
# guessed = ""

# # Game loop
# while tries > 0:
#     blanks = ""
#     for letter in word:
#         if letter in guessed:
#             blanks += letter
#         else:
#             blanks += "_"

#     print("Word:", blanks)

#     if blanks == word:
#         print("You win!")
#         break

#     guess = input("Guess a letter: ")
#     guessed += guess

#     if guess not in word:
#         tries -= 1
#         print("Wrong! Tries left:", tries)

# # Game over
# if tries == 0:
#     print("You lose! The word was:", word)


print("random number guessing game")

import random
num = random.randint(1,50)

tries = 0

while True:
    a = int(input("Guess a number between 1 and 50:- "))

    if num==a:
        tries +=1
        print(f"you guessed it right in {tries} tries.")
        break

    elif num<a:
        tries +=1
        print(f"the number is little smaller then {a}")

    elif num>a:
        tries +=1
        print(f"the number is little bigger then {a}")    

        
    else:
        tries +=1
        print("you guessed it wrong")

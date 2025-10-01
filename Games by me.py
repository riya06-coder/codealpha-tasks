# print("random number guessing game")

# import random
# num = random.randint(1,10)

# tries = 0

# while True:
#     a = int(input("Guess a number between 1 and 10:- "))

#     if num==a:
#         tries +=1
#         print(f"you guessed it right in {tries} tries.")
#         break

#     elif num<a:
#         tries +=1
#         print(f"the number is little smaller then {a}")

#     elif num>a:
#         tries +=1
#         print(f"the numer is little bigger then {a}")    

        
#     else:
#         tries +=1
#         print("you guessed it wrong")




print("A ramdom number guessing game")

import random

num = random.randint(1,50)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 50 :- "))

    if num==guess:
        print(f"Congrats You guessed it right in {tries} tries.")
        tries +=1
        break

    elif num>guess:
        print("go little higher")
        tries +=1

    elif num<guess:
        print("go little lower")
        tries +=1

    else:
        print("you guessed it wrong")
        tries +=1
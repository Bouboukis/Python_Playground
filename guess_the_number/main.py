""" This is Guess the Number game. It is a basic program that I wrote to improve my knowledge of Python.
    The game will choose a number from 0 - 20 and then the player has 6 guesses to find out.
    Of Course there will be some help.
    The game will inform the player if he is higher or lower than the chosen number.
    """

import random

gusses_taken = 0

player_name = input("Hello and welcome to guess the number game!\n What is your name player?\n")

chosen_number = random.randint(0, 20)

print("Well, {} I am thinking a number between 1 and 20.\n "
      "Now it is the time to try your luck.\n"
      "Can you guess  the number in less than 7 tries?\n".format(player_name))

for i in range(6):

    print("This is your try No {}!\n".format(i+1))
    guess = int(input("Take a guess:\n"))

    gusses_taken += 1

    if guess == chosen_number:
        print("Good job {}! \nYou have guessed the number in {} guesses.".format(player_name, gusses_taken))
        break
    elif guess < chosen_number:
        print("{} your guess is too low.\n".format(player_name))
        print("{}, you have {} tries left!\n".format(player_name, 6 - gusses_taken))
    else:
        print("Your guess is too high.\n")
        print("{}, you have {} tries left!\n".format(player_name, 6 - gusses_taken))

if guess != chosen_number:
    print("{}, you failed miserably, prepare to face the consequences.".format(player_name))
else:
    print("Have a nice day and hope to play the game again in the future.")


"""
This program will prompt the user to input their choice of rock, paper, or scissors. 
It will then randomly select one of the options for the computer's choice, and compare the two choices 
to determine the winner. If the user inputs an invalid choice, the program will prompt the user again
to enter a valid choice. You can also add more functionality to the application, like adding a game 
loop to play multiple rounds, storing the score and displaying it, adding more options or even 
making it a multiplayer game.

Please let me know if you have any questions or if you need help with anything else.
"""
import random

#list of options
options = ["rock", "paper", "scissors"]

#user input
user_choice = input("Please choose rock, paper or scissors: ").lower()

#computer choice
computer_choice = random.choice(options)

#compare choices and determine winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock beats Scissors")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Paper beats Rock")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors beats Paper")
else:
    print("You lose! {} beats {}".format(computer_choice, user_choice))
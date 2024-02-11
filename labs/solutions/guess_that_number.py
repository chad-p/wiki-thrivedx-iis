import random

computer_choice = random.randrange(1, 10)
user_choice = int(input("I'm thinking of a number between 1-10, what is it? "))

if user_choice == computer_choice:
    print(f"You guess correctly!  The number was {computer_choice}")
else:
    print(f"Sorry, the number was {computer_choice}.")
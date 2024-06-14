'''
Day 4 - Randomness (ROCK, PAPER, SCISSORS)
Author: MAAZ ALI
Program that plays rock, paper, scissors.
'''

import random

actions = ["rock", "paper", "scissors"]
player_action = input("Rock, Paper, or Scissors? ").lower()
computer_action = actions[random.randint(0, len(actions) - 1)]
print(f"You chose {player_action} and the computer chose {computer_action}!")
if player_action == computer_action:
    print("Draw!")
elif player_action == "rock":
    if computer_action == "scissors":
        print("You win!")
    elif computer_action == "paper":
        print("You lose!")
elif player_action == "scissors":
    if computer_action == "paper":
        print("You win!")
    elif computer_action == "rock":
        print("You lose!")
elif player_action == "paper":
    if computer_action == "rock":
        print("You win!")
    elif computer_action == "scissors":
        print("You lose!")
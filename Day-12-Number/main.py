'''
Day 11: Number Guessing
Author: Maaz Ali
Date: May 12
A Number Guessing Game.
'''

import art
import random

def difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff == 'easy':
        return 10
    elif diff == 'hard':
        return 5

if __name__ == '__main__':
    print(art.logo)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
    randnum = random.randint(1,100)
    print(f"The correct number is {randnum}")
    lives = difficulty()
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == randnum:
            print(f"You got it! The answer is {randnum}.")
            break
        elif guess<randnum:
            print("Too low.")
            print("Guess again.")
            lives -= 1
        else:
            print("Too high.")
            print("Guess again.")
            lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose.")    
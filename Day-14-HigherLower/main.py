'''
Day 14: Higher or Lower Game
Author: Maaz Ali
Date: May 12 2024
Program to play higher or lower.
'''

import art
import game_data
import random
     
if __name__ == '__main__':
    print(art.logo)
    pick1 = random.choice(game_data.data)
    game = True
    score = 0
    while game:
        pick2 = random.choice(game_data.data)
        while pick1 == pick2:
            pick2 = random.choice(game_data.data)
        print(f"Compare A: {pick1['name']}, a {pick1['description']}, from {pick1['country']}")
        print(art.vs)
        print(f"Compare B: {pick2['name']}, a {pick2['description']}, from {pick2['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice == 'A' and pick1['follower_count'] > pick2['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
            pick1 = pick2
        elif choice == 'B' and pick2['follower_count'] > pick1['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
            pick1 = pick2
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            game = False
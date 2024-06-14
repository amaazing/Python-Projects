'''
Author: Maaz Ali
Date: May 11 2024
Program that plays a basic game of blackjack
Infinite cards
'''
import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def initGame(player_hand, dealer_hand):
    deal(player_hand)
    deal(dealer_hand)
    deal(player_hand)
    deal(dealer_hand)

def calculate(hand_list):
    sum = 0
    for cards in hand_list:
        if cards == 11:
            if sum + cards >21: #Optimizing Ace draws to handle >21 edge cases
                cards = 1
        sum += cards
    return sum

def deal(hand_list):
    hand_list.append(random.choice(cards))

def endGame(player_hand, dealer_hand, player_total, dealer_total):
    print("Player cards:", end=" ")
    for card in player_hand:
        print(card, end=" ")
    print(f"\nPlayer Total: {player_total}")
    print("Dealer Hand:", end=" ")
    for card in dealer_hand:
        print (card, end=" ")
    print(f"\nDealer Total: {dealer_total}")
    exit()


if __name__ == '__main__':
    print(art.logo)
    continue_deal = True
    player_cards = []
    dealer_cards = []
    initGame(player_cards, dealer_cards)
    player_total = calculate(player_cards)
    dealer_total = calculate(dealer_cards)
    if dealer_total == 21:
        print("Dealer wins. Blackjack!")
        endGame(player_cards, dealer_cards, player_total, dealer_total)
    elif player_total == 21:
        print("Player wins. Blackjack")
        endGame(player_cards, dealer_cards, player_total, dealer_total)
    while continue_deal:
        print("Player Cards:", end="")
        for card in player_cards:
            print(card, end=" ")
        print()
        if player_total > 21:
            print("Player total over 21. You Lose!")
            endGame(player_cards, dealer_cards, player_total, dealer_total)
        for card in range(len(dealer_cards)):
            if card == 0:
                print(f"Dealer Cards:{dealer_cards[card]}", end=" ")
            else: 
                print("*", end=" ")
        print()
        if not input("Press 'y' if you want to draw another card: ") == 'y':
            continue_deal = False
        else:
            deal(player_cards)
            player_total = calculate(player_cards)
    while dealer_total < 16:
        deal(dealer_cards)
        for card in range(len(dealer_cards)):
            if card == 0:
                print(f"Dealer Cards:{dealer_cards[card]}", end=" ")
            else: 
                print("*", end=" ")
        print()
        dealer_total = calculate(dealer_cards)
        if dealer_total > 21:
            print("Dealer total over 21. You win!")
            endGame(player_cards, dealer_cards, player_total, dealer_total)
    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("You lose!")
    else:
        print("It's a Draw!")
    endGame(player_cards, dealer_cards, player_total, dealer_total)


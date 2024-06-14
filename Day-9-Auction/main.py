'''
Author: Maaz Ali
Date: May 9 2024
A program that manages a blind auction.
'''

import os
import art

def add_buyer(name_entry, bid_entry, data_dictionary):
    data_dictionary[name_entry] = int(bid_entry)
    return data_dictionary

def find_highest_bidder(bid_dictionary):
    max_bid = 0
    for name in bid_dictionary:
        if data_dict[name] > max_bid:
            max_bid = data_dict[name]
            max_bidder = name
    print(f"{max_bidder} won the auction with a bid of ${max_bid}!")


if __name__ == '__main__':
    data_dict = {}
    print(art.logo)
    bid_ongoing = True
    while bid_ongoing:
        name = input("Enter your name:\n")
        bid = input("Enter your bid:\n$")
        data_dict = add_buyer(name,bid,data_dict)
        print(data_dict)
        ongoing = input("Does someone else want to bid[Yes/No]?\n").lower()
        if ongoing == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break    
    find_highest_bidder(data_dict)

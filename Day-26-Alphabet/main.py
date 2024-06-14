'''
Day 26
Phonetic Alphabet
Maaz Ali
'''
import pandas 

#TODO 1. Create a dictionary in this format:
nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alpha.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
solution = [nato_dict[letter] for letter in user_input]
print(solution)
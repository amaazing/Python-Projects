'''
Author: Maaz Ali
Date: May 8 2024
Enciphers/deciphers text.
'''
import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

def caesar():    
    command = input("Enter encode/decode to encode/decode a text:\n").lower()
    end_text = ""
    if command == "encode":
        encode = input("Enter the text you want to encrypt:\n").lower()
        key = int(input("How much do you want to shift by?\n"))
        for letter in encode:
            index = alphabet.index(letter)
            letter = alphabet[(index+key)%26]
            end_text += letter
        print(end_text)
        return
    if command == "decode":
        decode = input("Enter the text you want to decrypt:\n").lower()
        key = int(input("Enter the key needed to decrypt:\n"))
        decoded_plaintext = ""
        for letter in decode:
            index = alphabet.index(letter)
            letter = alphabet[(index-key)%26]
            decoded_plaintext += letter
        print(decoded_plaintext)
        return

if __name__ == "__main__":
    print(art.logo)
    caesar()
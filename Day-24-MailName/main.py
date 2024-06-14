'''
Maaz
A program to create Birthday letters
May 20 2024
'''

with open("./Input/Letters/starting_letter.txt") as letter_text:
    letter_text = letter_text.read()

with open ("./Input/Names/invited_names.txt") as name_text:
    name_text = name_text.readlines()
    name_text = [name.strip() for name in name_text]
    for name in name_text:
        new_letter = letter_text.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w") as output_file:
            output_file.write(new_letter)    
        
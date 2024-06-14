'''
Day 5 - Password Generator
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

current_letters = 0
current_symbols = 0
current_numbers = 0
passlength = nr_letters+nr_symbols+nr_numbers
password = ""
current_index = 0
for entry in range(1,passlength+1):
    if current_letters != nr_letters and current_symbols != nr_symbols and current_numbers != nr_numbers:
        password += random.choice(letters + numbers + symbols)
    elif current_letters != nr_letters and current_symbols != nr_symbols:
        password += random.choice(letters+symbols)
    elif current_letters != nr_letters and current_numbers != nr_numbers:
        password += random.choice(letters+numbers)
    elif current_symbols != nr_symbols and current_numbers != nr_numbers:
        password += random.choice(symbols + numbers)
    elif current_letters != nr_letters:
        password += random.choice(letters)
    elif current_numbers != nr_numbers:
        password += random.choice(numbers)
    elif current_symbols != nr_symbols:
        password += random.choice(symbols)
    if password[current_index] in letters:
        current_letters+=1
    elif password[current_index] in numbers:
        current_numbers+=1
    elif password[current_index] in symbols:
        current_symbols+=1
    current_index += 1
print(f"Your random password is: {password}")

    

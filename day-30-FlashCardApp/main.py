'''
Day 31: Tkinter Flashcard App
Author: Maaz
A flashcard quiz app.
'''

from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

def next_card():
    global current_card, timer
    window.after_cancel(timer) # Cancels the timer so we get the full 3 seconds for each card.
    current_card = random.choice(df_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    timer = window.after(3000, func=reveal)

# Reveals the answers in the card.
def reveal():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)
    
def known():
    global current_card
    df_dict.remove(current_card)
    data = DataFrame(df_dict)
    data.to_csv("./data/to_learn.csv", index = False)
    next_card()
    
try:
    df = read_csv("./data/to_learn.csv")
except FileNotFoundError:
    df = read_csv("./data/french_words.csv")
df_dict = df.to_dict(orient="records")
current_card = {}


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=reveal)

# Cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400,263, image= card_front)
canvas.grid(row=0, column = 0, columnspan=2)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 264, text="", font=("Ariel", 40, "bold"))
card_back = PhotoImage(file="./images/card_back.png")

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1,column=0)
next_card()

window.mainloop()





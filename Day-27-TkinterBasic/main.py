'''
Temperature Converter with GUI
Maaz Ali
'''

from tkinter import *

def calculate():
    fahrenheit = float(Fahrenheit_input.get())
    celsius = (fahrenheit-32) * (5/9)
    celsius_result_label.config(text=f"{celsius}")

window = Tk()
window.minsize(width = 200, height = 50)
window.title("Fahrenheit to Celsius")
Fahrenheit_input = Entry()
Fahrenheit_input.grid(column=1,row=0)
Fahrenheit_label = Label(text="Fahrenheit")
Fahrenheit_label.grid(column=2,row=0)
equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)
celsius_result_label = Label(text="0")
celsius_result_label.grid(column=1,row=1)
celsius_label = Label(text= "Celsius")
celsius_label.grid(column=2,row=1)
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1,row=3)








window.mainloop()
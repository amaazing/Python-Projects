import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
print(data_list)
pen = turtle.Turtle("blank")
pen.penup()
guessed_states = []

while len(guessed_states) < len(data_list):
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        break
    
    if answer_state in data_list:
        guessed_states.append(answer_state)
        state_coor = data[data.state == answer_state]
        pen.goto(int(state_coor.x), int(state_coor.y))
        pen.write(answer_state)

missed_states = []
for states in data_list:
    if states not in guessed_states:
        missed_states.append(states)
        
missed = pandas.DataFrame(missed_states)
missed.to_csv("missed_states.csv")

        
        
screen.exitonclick()
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+= 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg = RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Short Break" , fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text = "Work", fg = PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = count//60
    count_seconds = count%60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"
        check_marks.config(text=mark)
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width= 200, height = 225, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="reset", command = reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)









window.mainloop()
import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__ (self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.config(
                           padx=20,
                           pady=20,
                           bg= THEME_COLOR
                           )
        self.window.title("GUI Quiz")
        
        #Score
        self.score_label = tkinter.Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        #Canvas for question
        self.gui_canvas = tkinter.Canvas(height=250, width=300)
        self.question_text = self.gui_canvas.create_text(150,125,
                                                         text="Question Text",
                                                         font=("Arial", 20, "italic"),
                                                         fill=THEME_COLOR,
                                                         width = 270)
        self.gui_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        #Buttons
        wrong_image = tkinter.PhotoImage(file="./images/false.png")
        self.wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=self.false_command)
        self.wrong_button.grid(row=2, column=1)
        
        right_image = tkinter.PhotoImage(file= "./images/true.png")
        self.right_button = tkinter.Button(highlightthickness=0, image=right_image, command=self.true_command)
        self.right_button.grid(row=2, column=0)
        self.get_question()
        
        
        
        self.window.mainloop()
        
    def get_question(self):
        self.gui_canvas.config(bg="white")
        if self.quiz.still_has_questions():  
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.gui_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.gui_canvas.itemconfig(self.question_text, text="Quiz Over!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        
    def true_command(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def false_command(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.gui_canvas.config(bg="green")
        else:
            self.gui_canvas.config(bg="red")
        self.window.after(1000, self.get_question)
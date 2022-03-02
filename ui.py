import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): # To initialize data type of parameters

        # Variables
        self.quiz = quiz_brain

        # UI Setup
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.label = tkinter.Label(fg="White", font=("Arial", 15), text="Current Score = 0", bg=THEME_COLOR)
        self.label.grid(row=0, column=0)

        # Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some Question here",
                                                     fill=THEME_COLOR, font=("Arial", 20, "italic"))

        # Button
        correct_img = tkinter.PhotoImage(file="images/true.png")
        self.btn_correct = tkinter.Button( image=correct_img, highlightthickness=0, command=self.true_pressed)
        self.btn_correct.grid(row=2, column=0)

        incorrect_img = tkinter.PhotoImage(file="images/false.png")
        self.btn_incorrect = tkinter.Button( image=incorrect_img, highlightthickness=0, command=self.false_pressed)
        self.btn_incorrect.grid(row=2, column=1)

        self.get_next_question()
        # Mainloop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.btn_correct.config(state="disabled")
            self.btn_incorrect.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



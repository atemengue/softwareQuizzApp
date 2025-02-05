from tkinter import Tk, Canvas, StringVar, Label, Entry, Radiobutton, Button, messagebox, Menu, Frame
from tkinter.filedialog import  askopenfilename
from database import  get_questions_response
from home_game_page import HomeGamePage
from config_game_page import ConfigGamePage
from quizz_game_page import QuizzGamePage
from score_game_page import ScoreGamePage

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self) -> None:

        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("1000x630")
        self.score = 0
        self.question_no = 0
        self.current_question = None
        self.questions = []

        # title = Label(self, text="iQuiz Application", width=30, bg="green", fg="white", font=("ariel", 30, "bold"))
        # title.place(x=0, y=0)

        #creating container
        container = Frame()
        container.pack(side = "top", fill= "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #initialization frames to an empty array
        self.frames = {}

        for F in (HomeGamePage, ConfigGamePage, QuizzGamePage, ScoreGamePage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        # show frames
        self.show_frame(HomeGamePage)

        # Mainloop
        self.window.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
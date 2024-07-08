
import tkinter as tk
from tkinter import ttk
from quizz_game_page import QuizzGamePage

questions = []

LARGEFONT =("Verdana", 35)

class HomeGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Home Game Page", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Quizz Game Page", command=self.show_quizz_game_page)

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(2))

        # putting the button in its place by
        # using grid
        # button2.grid(row=2, column=1, padx=10, pady=10)

    def show_quizz_game_page(self):
        print("this is quizz game page")
        #quizz_ui_1 = QuizzGamePage(self,[])
        QuizzGamePage.init_questions_game(self)

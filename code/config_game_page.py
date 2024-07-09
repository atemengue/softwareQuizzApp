
import tkinter as tk
from quizz_game_page import QuizzGamePage
from tkinter import ttk, Label, Button, Toplevel, StringVar, Entry, IntVar, Radiobutton, Text
from database import  add_player


LARGEFONT =("Verdana", 35)


class ConfigGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = " "
        self.controller = controller
        self.parent = parent

        # label of frame Layout 2
        label = ttk.Label(self, text="Config Game Page", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        # label of frame Layout 2
        # label = ttk.Label(self, text="Home Game Page  QUIZZ APP", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        # label.grid(row=0, column=4, padx=10, pady=10)

        label = ttk.Label(self, text="Player Name")
        label.grid(row=1, column=0, padx=10, pady=10)

        self.name = StringVar()
        entry = Entry(self, textvariable=self.name)
        entry.grid(row=1, column=1, padx=10, pady=10)

        self.option = IntVar()
        option1 = Radiobutton(self, value=1, text="Lecturer 1", variable=self.option)
        option1.grid(row=3, column=1, padx=10, pady=10)
        option2 = Radiobutton(self, value=2, text="Lecturer 2", variable=self.option)
        option2.grid(row=4, column=1, padx=10, pady=1)


        button1 = Button(self, text="Start Game",command=self.start_game)

        # putting the button in its place by
        # using grid
        button1.grid(row=5, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(2))

        # putting the button in its place by
        # using grid
        # button2.grid(row=2, column=1, padx=10, pady=10)
    def start_game(self):

        # add player on database
        add_player(self.name.get())
        quizz_ui = QuizzGamePage(self.parent, self.controller)

        self.controller.show_frame(QuizzGamePage)

        # setConfigGame
        quizz_ui.get_config_game(self.name.get(), self.option.get())

        #show QUizzGamePage

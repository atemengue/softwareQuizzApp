import tkinter as tk
from tkinter import ttk, Label, Button, Toplevel, StringVar, Entry, IntVar, Radiobutton, Text, INSERT, END, RIGHT, LEFT
Title_Font = ("Helvetica", 16, "bold")
LARGEFONT = ("Verdana", 20, "bold")

class ScoreGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = Label(self, text="Score", width=40, bg="green", fg="white", font=("ariel", 30, "bold"))
        title.place(x=0, y=0)

        self.score = 0
        self.controller = controller

        self.player_name_label_frame = tk.LabelFrame(self, text="Player Name: ", font=Title_Font)
        self.player_name_label_frame.pack(padx=50, pady=100)

        self.player_name_label_frame = tk.Label(self.player_name_label_frame)
        self.player_name_label_frame.pack()

        self.score_label = Label(self)

    def get_score_player_name(self):
        self.score = self.controller.scrore

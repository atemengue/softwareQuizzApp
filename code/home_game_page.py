
import tkinter as tk
from tkinter import ttk, Label, Button, Toplevel, StringVar, Entry, IntVar, Radiobutton, Text, INSERT, END, RIGHT
from config_game_page import ConfigGamePage

questions = []

LARGEFONT =("Verdana", 30)

class HomeGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #label of frame Layout 2
        label = Label(self, text="WELCOME TO QUIZZ APP", font=LARGEFONT)

        #putting the grid in its place by using
        label.grid(row=0, column=4, padx=10, pady=10)


        button = Button(self, text="Start Game", command=lambda: controller.show_frame(ConfigGamePage))
        button.place(x=25, y=100)
        # putting the button in its place by
        # using grid
        button.grid(row=1, column=1, padx=10, pady=10)
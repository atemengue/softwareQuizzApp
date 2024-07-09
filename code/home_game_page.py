
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

        # label of frame Layout 2
        #label = ttk.Label(self, text="Home Game Page  QUIZZ APP", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        #label.grid(row=0, column=4, padx=10, pady=10)

        # input = StringVar()
        # entry = Entry(self, textvariable=input)
        # entry.grid(row=1, pady=30)
        #
        # option = IntVar()
        # option1 = Radiobutton(self, value=1, text="Lecturer 1", variable=option)
        # option1.grid(row=1, column=1, padx=10, pady=10)
        # option2 = Radiobutton(self, value=2, text="Lecturer 2", variable=option)
        # option2.grid(row=2, column=1, padx=10, pady=10)


        # #button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text="Page 2", command=self.btn_two_data)
        #
        # # putting the button in its place by
        # # using grid
        # button2.grid(row=4, column=1, padx=10, pady=10)

    def show_quizz_game_page(self):
        print("this is quizz game page")
    def btn_two_data(self):
        print(self.name)
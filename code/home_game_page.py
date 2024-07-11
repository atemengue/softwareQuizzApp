import tkinter as tk
from tkinter import ttk, Label, Button, Toplevel, StringVar, Entry, IntVar, Radiobutton, Text, INSERT, END, RIGHT, LEFT
from config_game_page import ConfigGamePage
LARGEFONT = ("Verdana", 20, "bold")
class HomeGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = Label(self, text="iQuiz Application", width=40, bg="green", fg="white", font=("ariel", 30, "bold"))
        title.place(x=0, y=0)

        #label of frame Layout 2
        label = Label(self, text="WELCOME TO QUIZZ APP", font=LARGEFONT)
        label.place(x=250, y=250, anchor=tk.CENTER)

        about_game = Label(self, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n "
                                      "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n "
                               
                                      "when an unknown printer took a galley of type and scrambled it to make a type\n"
                                      "specimen book", font=('Aerial', 12))

        about_game.place(x=80, y=300)

        button = Button(self, text="Go to Config", command=lambda: controller.show_frame(ConfigGamePage), width=10,
                        bg="green", fg="white", font=("ariel", 16, "bold"))
        button.place(x=80, y=460)

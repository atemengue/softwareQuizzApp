
import tkinter as tk
from quizz_game_page import QuizzGamePage
from tkinter import ttk, Label, Button, Toplevel, StringVar, Entry, IntVar, Radiobutton, Text
from database import  add_player, get_lectures

LARGEFONT =("Verdana", 35)

class ConfigGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = StringVar()
        self.controller = controller
        self.parent = parent
        self.lectures =  []

        # label of frame Layout 2
        #label = ttk.Label(self, text="Config Game Page", font=LARGEFONT)

        title = Label(self, text="iQuiz Application", width=40, bg="green", fg="white", font=("ariel", 30, "bold"))
        title.place(x=0, y=0)

        label = ttk.Label(self, text="Player Name", width=50, font=("ariel", 10, "bold"))
        label.place(x=60, y=100)

        entry = Entry(self, textvariable=self.name, width=100)
        entry.place(x=200, y=100)

        # Declare a StringVar to store user's answer
        self.user_lecture_answer = StringVar()

        # Display 2 options (radio buttons)
        self.opts = self.radio_buttons()
        self.display_lectures()

        button = Button(self, text="Start Game",command=self.start_game, width=10,
                        bg="green", fg="white", font=("ariel", 16, "bold"))
        button.place(x=80, y=460)

    def radio_buttons(self):
        """To create four options (radio buttons)"""

        # initialize the list with an empty list of options
        lectures_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(lectures_list) < 3:
            # setting the radio button properties
            radio_btn = Radiobutton(self, text="", variable=self.user_lecture_answer,
                                    value='', font=("ariel", 14))

            # adding the button to the list
            lectures_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return lectures_list

    def display_lectures(self):
        val = 0
        #deselecting the options
        self.user_lecture_answer.set(None)
        lectures = get_lectures()
        print(lectures)

        #looping over the options to be displayed for the
        #text of the radio options
        for lecture in lectures:
            self.opts[val]['text'] = lecture[1]
            self.opts[val]['value'] = lecture[0]
            val += 1


    def start_game(self):
        # add player on database
        add_player(self.name.get())

        #set controllervalues
        self.controller.player_name = self.name.get()
        self.controller.id_lecture = self.user_lecture_answer.get()

        #start frame
        self.controller.frames[QuizzGamePage].correct_label()
        self.controller.show_frame(QuizzGamePage)

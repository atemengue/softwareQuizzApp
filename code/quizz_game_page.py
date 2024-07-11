import tkinter as tk
from tkinter import ttk, Canvas, StringVar, Label, Entry, Radiobutton, Button, messagebox, Menu, Frame
from tkinter.filedialog import  askopenfilename
from database import  get_questions_response, get_all_questions
import random

LARGEFONT =("Verdana", 35)
Title_Font = ("Helvetica", 16, "bold")
Label_Font = ("Helvetica", 10)
THEME_COLOR = "#375362"


class QuizzGamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.score = 0
        self.question_no = 0
        self.question_increment = 0
        self.current_question = None
        self.questions = []
        self.parent = parent

        self.player_name = ""
        self.controller = controller

        # set defaut id lectuer to 1
        self.id_lecture = 1

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()
        #
        # # set defaut id lectuer to 1
        # self.id_lecture = 0
        #
        # # label of frame Layout 2
        # label = Label(self, text="Quizz Game Page", font=LARGEFONT)
        # label.pack(padx=10, pady=10)
        game_name = Label(self, text="iQuiz Application", width=40, bg="green", fg="white", font=("ariel", 30, "bold"))
        game_name.place(x=0, y=0)

        self.label1 = Label(self)
        self.label1.pack(padx=10, pady=10)

        self.question_label = Label(self, text="", font=('Ariel', 15, 'italic'), bg="#375362", fg="white", width=680,)
        self.question_label.pack(padx=50, pady=100)

        self.player_name_label_frame = tk.LabelFrame(self, text="Player Name: ", font=Title_Font)
        self.player_name_label_frame.pack(padx=50, pady=100)

        self.player_name_label_frame = tk.Label(self.player_name_label_frame)
        self.player_name_label_frame.pack()


        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()


        # Next and Quit Button
        self.buttons()

    def get_config_game(self, name, id_lecture):
        self.player_name = name
        self.id_lecture = id_lecture
        self.questions = random.sample(get_all_questions(id_lecture), k=2)

        # self.label_question.pack(padx=50, pady=10)
        self.display_question()
        # Display four options(radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()
        # To show whether the answer is correct or wrong
        self.feedback = Label(self, pady=10, font=("ariel", 13, "bold"))
        self.feedback.place(x=80, y=490)

    def correct_label(self):
        #refresh to add player Name
        self.player_name_label_frame.config(text=self.controller.player_name)


        self.id_lecture = self.controller.id_lecture
        self.questions = random.sample(get_all_questions(self.controller.id_lecture), k=3)
        self.current_question = self.questions[0][0]

        # self.label_question.pack(padx=50, pady=10)
        self.display_question()
        #

        # Display four options(radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self, pady=10, font=("ariel", 13, "bold"))
        self.feedback.place(x=80, y=490)


    # def init_questions_game(self):
    #     print("Initialization game questions")
    #     test_hello()
    # def __init__(self, questions):
    #     self.window = Tk()
    #
    #     self.score = 0
    #     self.question_no = 0
    #     self.current_question = None
    #     self.questions = questions
    #     self.username = ''
    #
    #     print("Inside constructions with questions")
    #
    #
    #     # DisplayMenu
    #     self.display_menu()
    #
    #     # Display Title
    #     self.display_title()

        # self.display_username()

        # # Creating a canvas for question text, and dsiplay question
        # self.canvas = Canvas(width=800, height=250)
        # self.question_text = self.canvas.create_text(400, 125,
        #                                              text="Question here",
        #                                              width=680,
        #                                              fill=THEME_COLOR,
        #                                              font=(
        #                                                  'Ariel', 15, 'italic')
        #                                              )
        # self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        # self.display_question()
        #
        # # Declare a StringVar to store user's answer
        # self.user_answer = StringVar()
        #
        # # Display four options(radio buttons)
        # self.opts = self.radio_buttons()
        # self.display_options()
        #
        # # To show whether the answer is correct or wrong
        # self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        # self.feedback.place(x=300, y=380)
        #
        # # Next and Quit Button
        # self.buttons()

# def new_file(self):
#     print("New File!")
#
#
# def open_file(self):
#     name = askopenfilename()
#     print(name)
#
#
# def about_game(self):
#     print("This is a simple example of a menu")
#
#
# def display_menu(self):
#     menu = Menu(self.window)
#     self.window.config(menu=menu)
#     file_menu = Menu(menu)
#     menu.add_cascade(label="File", menu=file_menu)
#     file_menu.add_command(label="New", command=self.new_file)
#     file_menu.add_command(label="Open...", command=self.open_file)
#     file_menu.add_separator()
#     file_menu.add_command(label="Exit", command=self.window.quit)
#
#     help_menu = Menu(menu)
#     menu.add_cascade(label="Help", menu=help_menu)
#     help_menu.add_command(label="About...", command=self.about_game)
#
#
#     def display_title(self):
#         """To display title"""
#
#         print("Title")
#
#         # Title
#         title = Label(self.window, text="iQuiz Application",
#                       width=120, bg="green", fg="white", font=("ariel", 20, "bold"))
# #
#         # place of the title
#         title.place(x=0, y=2)

    # def display_username(self):
    #     global entry
    #     string = entry.get()
    #     Label.configure(text=string)
    #
    #      # Initialize a Label to display the User Input
    #
    #     label = Label(self.window, text="", font=("Courier 22 bold"))
    #     label.pack()
    #
    #      # Create an Entry widget to accept User Input
    #     entry = Entry(self, width=40)
    #     entry.focus_set()
    #     entry.pack()


    def display_question(self):
        q_text = self.next_question()
        self.question_label.config(text=q_text)
        #self.label2.configure(text=self.id_lecture)


    def next_question(self):
#     """Get the next question by incrementing the question number"""
        self.current_question = self.questions[self.question_increment]
        self.question_no = self.current_question[0]
        self.question_increment += 1
        description = self.current_question[1]
        return f"Q.{self.question_increment}: {description}"

#
    def radio_buttons(self):
        """To create four options (radio buttons)"""

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 3:
            # setting the radio button properties
            radio_btn = Radiobutton(self, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list
#
#
    def display_options(self):
        """To display four options"""

        val = 0

        # deselecting the options
        self.user_answer.set(None)
        # get responses  questions
        # looping over the options to be displayed for the
        # text of the radio buttons.
        responses = get_questions_response(self.question_no)

        for response in responses:
            self.opts[val]['text'] = response[1]
            self.opts[val]['value'] = response[1] + '/' + str(response[2])
            val += 1
#
#
    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        # Check if the answer is correct
        if self.check_answer():
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right Response is: {self.current_question[2]}')

        if self.question_increment < len(self.questions):
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()

            # destroys the self.window
            self.window.destroy()
#
#
    def buttons(self):
        """To show next button and quit button"""

        # The first button is the Next button to move to the
        # next Question

        next_button = Button(self, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # palcing the button  on the screen
        next_button.place(x=80, y=550)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self, text="Quit", command=self.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=550)
#
    def check_answer(self):
        correct_answer = self.user_answer.get().split('/')[1] == "1"
        if correct_answer:
            self.score += 1
            return True
        else:
            return False
#
#
    def get_score(self):
        """Get the number of correct answers, wrong answers and score percentage."""
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)
#
#
    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # Shows a message box to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
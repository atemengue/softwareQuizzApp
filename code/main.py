from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from database import  create_and_load_database, get_all_questions
from quizz_ui import QuizzInterface

if __name__ == "__main__":

    questions = []

    try:
        create_and_load_database()


    except:
        print("Database exits")

    #select all questions
    questions = get_all_questions()
    quizz_ui = QuizzInterface(questions)



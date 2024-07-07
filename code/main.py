from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from database import  create_database, import_database, get_all_questions, get_questions_response
from quizz_ui import QuizzInterface

if __name__ == "__main__":
    questions = []
    try:
        #create database
        create_database()

        #import database
        import_database()

    except:
        print("Database exits")

    #select all questions
    questions = get_all_questions()
    quizz_ui = QuizzInterface(questions)



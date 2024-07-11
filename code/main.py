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
    QuizzInterface()


import datetime
import sqlite3
import csv

CREATE_TABLE_GAME = """
CREATE TABLE IF NOT EXISTS game (
   idGame INTEGER PRIMARY KEY AUTOINCREMENT,
   score INTEGER,
   userIdUser INTEGER,
   date TIMESTAMP,
   FOREIGN KEY (userIdUser) REFERENCES users(idUser)
);
"""

CREATE_TABLE_LECTURE = """
CREATE TABLE IF NOT EXISTS lectures (
    idLecturer INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    date TIMESTAMP
);
"""

CREATE_TABLE_QUESTION = """
CREATE TABLE IF NOT EXISTS questions (
    idQuestion INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    explanation TEXT,
    lectureIdLecture INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (lectureIdLecture) REFERENCES lectures(idLecture)
);
"""

CREATE_TABLE_RESPONSE = """
CREATE TABLE IF NOT EXISTS responses (
    idResponse INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    state INT,
    questionIdQuestion INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (questionIdQuestion) REFERENCES questions(idQuestion)
);
"""

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TIMESTAMP
);
"""

ADD_USER = """
    INSERT INTO users (name, date)
    VALUES("regis", DATE('now'));
"""

ADD_LECTURE = """
    INSERT INTO lectures (title, description, date)
    VALUES
    ("Fundamentals of Software Engineering", "This is Software Engineering Course Lecturer", DATE('now')),
    ("Software Algorithms", "This is software Algorithms Lecturer", DATE('now')),
    ("Software Testing", "This is software testing Lecture", DATE('now'));
"""

ADD_QUESTION = """
    INSERT INTO questions (description, lectureIdLecture, date)
    VALUES("What is the main goal of software testing?", 1, DATE('now'));
"""

ADD_RESPONSES = """
    INSERT INTO responses (description, state, questionIdQuestion, date)
    VALUES
    ("To ensure the software performs as expected and to identify defects.", 1, 1, DATE('NOW')),
    ("To write the software code", 0, 1, DATE('NOW')),
    ("To design the Software architecture", 0, 1, DATE('now'))
"""

GET_ALL_QUESTIONS_WITH_RESPONSES = """
    SELECT
     responses.idResponse as idResponse,
     responses.description as description,
     responses.state as state,
     questions.idQuestion as idQuestion,
     questions.description as titleQuestion
FROM responses
INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion;

"""

GET_ALL_QUESTIONS = """
SELECT  *
FROM  questions;
"""

GET_ALL_RESPONSES_OF_ONE_QUESTIONS = """
SELECT
     responses.idResponse as idResponse,
     responses.description as description,
     responses.state as state,
     questions.idQuestion as idQuestion,
     questions.description as titleQuestion
FROM responses
INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion
WHERE responses.idResponse = 2
"""

GET_USER_ID = """
SELECT
    idUser
FROM users
WHERE name = 'regos'
"""


def add_player(name):
    sql = "INSERT INTO users(name, date) VALUES(?, ?);"
    values = (name, datetime.datetime.now())
    a = cursor.execute(sql, values)
    print(a)
    database.commit()


def add_gaming(score, iduser):
    sql = "INSERT INTO game(score, userIdUser, date) VALUES(?, ?, ?);"
    values = (score, iduser, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

def import_questions(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)
        rows = list(reader)
        print(rows)
        sql = "INSERT INTO questions VALUES (?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()
        print(f"Imported {len(rows)} investments from {csv_file}")


def import_responses(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)
        rows = list(reader)
        print(rows)
        sql = "INSERT INTO responses VALUES (?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()
        print(f"Imported {len(rows)} investments from {csv_file}")


def get_questions_response(idQuestion):
    sql = f"""SELECT
     responses.idResponse as idResponse,
     responses.description as description,
     responses.state as state,
     questions.idQuestion as idQuestion,
     questions.description as titleQuestion
     FROM responses
     INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion
     WHERE questionIdQuestion= {idQuestion} ;"""

    results = cursor.execute(sql).fetchall()
    return results

def get_user_id():
    sql = "SELECT idUser FROM users WHERE name = 'regos';"
    user = cursor.execute(sql).fetchone()
    return user[0]

if __name__ == "__main__":
    database = sqlite3.connect("quizz.db")
    cursor = database.cursor()
    cursor.execute(CREATE_TABLE_USER)
    cursor.execute(CREATE_TABLE_GAME)
    cursor.execute(CREATE_TABLE_LECTURE)
    cursor.execute(CREATE_TABLE_QUESTION)
    cursor.execute(CREATE_TABLE_RESPONSE)

    #load data Game
    cursor.execute(ADD_LECTURE)
    database.commit()

    import_questions("../files/questions.csv")
    import_responses("../files/responses.csv")

    # create payer
    name = input("Enter your player name: ")
    add_player(name)

    #add lecturer

    #cursor.execute(ADD_LECTURE)
    #database.commit()

    ##add questions
    #cursor.execute(ADD_QUESTION)
    #database.commit()

    #add responses
    #cursor.execute(ADD_RESPONSES)
    #database.commit()

    #import responses
    #import_csv("../files/lectures.csv")
    #import_csv("../files/quez.csv")

    #get all questions with responses
    #questions = cursor.execute(GET_ALL_QUESTIONS_WITH_RESPONSES).fetchall()
    #print(questions)

    #gameKJ
    isPlaying = True
    choice = 1
    game_responses = []


    while  isPlaying:

        print("Etes vous pret a jouer le jeu ?")
        choice = input("Choissessez 1 pour oui ou autre pour terminer la partie")

        if choice == '1':

            print("Vous pouvez commencer la partie")
            print("QUIZZ GAME")

            questions = cursor.execute(GET_ALL_QUESTIONS).fetchall()
            i = 0

            while i < len(questions):

                question = questions[i]
                idQuestion = question[3]
                description = question[1]

                print(f" Question:{i + 1} {description}")

                responses = get_questions_response(idQuestion)
                for index, response in enumerate(responses):
                    print(f"  {index}--->    {response[1]}")

                choice_response = input("Entrer votre response:")
                game_responses.append(responses[int(choice_response)])

                i = i + 1

        else:

            print("Recommencer ")
        isPlaying = False

        score = 0

        for game_response in game_responses:
            score = score + game_response[2]

        print(f" Score Final  {score}  |  {len(game_responses)}")

        idUser = get_user_id()
        add_gaming(score , idUser)

    print("Partie Terminee" )
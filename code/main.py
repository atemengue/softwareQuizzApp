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
VALUES("Software Algorithms", "This is software Algorithms Lecturer", DATE('now'));
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

def add_player(name) :
    sql = "INSERT INTO users(name, date) VALUES(?, ?);"
    values = (name, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

# def import_questions(csv_file):
#     with open(csv_file, "r") as f:
#         rdr = csv.reader(f, delimiter=",")
#         rows = list(rdr)
#         print(rows, 'the rows')
#         sql = "INSERT INTO questions VALUES (?, ?, ?, ?);"
#         cursor.executemany(sql, rows)
#         database.commit()
#
#         print(f"Imported {len(rows)} investments from {csv_file}")


if __name__ == "__main__":
    database = sqlite3.connect("quizz.db")
    cursor = database.cursor()
    cursor.execute(CREATE_TABLE_USER)
    cursor.execute(CREATE_TABLE_GAME)
    cursor.execute(CREATE_TABLE_LECTURE)
    cursor.execute(CREATE_TABLE_QUESTION)
    cursor.execute(CREATE_TABLE_RESPONSE)

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
   # import_questions("../files/questions.csv")

    #get all questions with responses
    questions = cursor.execute(GET_ALL_QUESTIONS_WITH_RESPONSES).fetchall()
    print(questions)

















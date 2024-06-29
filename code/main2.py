import datetime
import  sqlite3
import  csv

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

CREATE_TABLE_USER = """CREATE TABLE IF NOT EXISTS users (
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TIMESTAMP
);"""

ADD_USER = """
    INSERT INTO users (name, date)
    VALUES("cecile", DATE('now'));
"""

ADD_LECTURE = """
    INSERT INTO lectures (title, description, date)
    VALUES
    ("Fundamentals of Software Engineering", "This is Software Engineering Course Lecturer", DATE('now')),
    ("Software Algorithms", "This is software Algorithms Lecturer", DATE('now')),
    ("Software Testing", "This is software testing Lecture", DATE('now'));
"""

def import_questions(csv_file_path):
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)
        rows = list(reader)
        sql = "INSERT INTO questions VALUES (?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()
        print(f"Imported {len(rows)} investments from {csv_file_path}")
def import_responses(csv_file_path):
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader, None)
        rows = list(reader)
        sql = "INSERT INTO responses VALUES (?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()
        print(f"Imported {len(rows)} investments from {csv_file_path}")

def add_player(name):
    sql_user = "INSERT INTO users(name, date) VALUES(?, ?);"
    values_user = (name, datetime.datetime.now())
    cursor.execute(sql_user, values_user)
    database.commit()

def get_all_questions():
    sql_questions = "SELECT * FROM QUESTIONS"
    questions = cursor.execute(sql_questions).fetchall()
    return questions

if __name__ == "__main__":

#creation de la base de donnees
    database = sqlite3.connect("quizzapp.db")
    cursor = database.cursor()

#creation des tables
    cursor.execute(CREATE_TABLE_USER)
    cursor.execute(CREATE_TABLE_LECTURE)
    cursor.execute(CREATE_TABLE_GAME)
    cursor.execute(CREATE_TABLE_QUESTION)
    cursor.execute(CREATE_TABLE_RESPONSE)

# insertion des elements dans la BD
    #cursor.execute(ADD_USER)
   # database.commit()  # sauvergarde la modification

# insertion des lectures
   # cursor.execute(ADD_LECTURE)
    database.commit()

# insertion des questions et des responses

   # import_questions("../files/questions.csv")
   # import_responses("../files/responses.csv")

    name = input("Entrer votre nom")
    sql_user = "INSERT INTO users(name, date) VALUES(?, ?);"
    values_user = (name, datetime.datetime.now())
    cursor.execute(sql_user, values_user)
    database.commit()

    # recuperer toutes les questions
    sql_questions = "SELECT * FROM QUESTIONS"
    questions = cursor.execute(sql_questions).fetchall()
    #
    # for question in questions:
    #     description = question[1]
    #     print(description)

    index = 0
    game_responses = []
    while(index < len(questions)):

        question = questions[index]
        print(question)
        description = question[1]
        idQuestion = question[0]
        print(f" Question { index + 1} { description}")

        #recuperation des questions
        sql_get_responses_questions = f"""
        SELECT
             responses.idResponse as idResponse,
             responses.description as description,
             responses.state as state,
             questions.idQuestion as idQuestion,
             questions.description as titleQuestion
            FROM responses
            INNER JOIN questions ON responses.questionIdQuestion = questions.idQuestion
            WHERE idQuestion = {idQuestion}
        """
        responses_questions = cursor.execute(sql_get_responses_questions).fetchall()
        for response in responses_questions:
            print(f"  --->    {response[1]}")

        # pour chaque questions du recuperer les reponses.

        user_choice = input("tapez pour avancer")
        game_responses.append(responses_questions[int(user_choice)])

        index = index + 1

    print(game_responses)


# [(2, 'Response B: An early, simplified version used to demonstrate concepts and gather feedback.', 1, 1, 'What is a software prototype?'),
#  (4, 'Response A: System testing', 0, 2, 'What type of testing involves testing individual components of the software in isolation?'),
#  (8, 'Response B: Acceptance testing', 1, 3, 'Which testing technique involves running the system under a controlled environment to ensure it meets specified requirements?'),
#  (10, 'Response A: It focuses on the internal structure of the code.', 0, 5, 'What is a characteristic of black-box testing?'), (
# 15, 'Response C: Managing databases.', 0, 6, 'What does software engineering primarily deal with?')]

    score = 0
    idUser = 0
    for game_response in game_responses:
        score = score + game_response[2]

    print(f" Score Final  {score}  |  {len(game_responses)}")
    # afficher toutes les questions

    sql_id_user = f"SELECT idUser FROM users WHERE name = '{name}';"
    idUser = cursor.execute(sql_id_user).fetchone()[0]
    #(4,)

    #ajouter le score et le iduser dans la table game
    sql_add_score_user = "INSERT INTO game(score, userIdUser, date) VALUES(?, ?, ?);"
    values = (score, idUser, datetime.datetime.now())
    cursor.execute(sql_add_score_user, values)
    database.commit()

print("Partie Terminee")























